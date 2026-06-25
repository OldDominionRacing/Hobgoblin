#!/usr/bin/env python3
"""A tiny local web viewer for Hobgoblin annotations.

    python examples/annotate_server.py          # then open http://localhost:8000

Paste text, hit Annotate, and the page draws a pill around every entity and item.
Hover a pill for a tooltip (its type / what it's associated to); click an entity
pill to see its full element breakdown (verb, count, dates, unit, associations).

No web framework — just the standard library plus Hobgoblin. The page talks to a
single JSON endpoint, POST /api/extract {"text": "..."} -> {text, entities, items}.
"""

import argparse
import html
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from hobgoblin import extract, item_index, ANCHORS

DEFAULT_TEXT = (
    "On 14 March 2025, Colonel John Smith reported that the 3rd Brigade and "
    "I Corps moved roughly 12 HMMWV trucks to Fort Bragg. "
    "B Battery held the depot at 35.139, -79.006 with about 3 vehicles. "
    "Contact the TOC at 555-867-5309 between 2 and 4 patrols per day."
)

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hobgoblin — annotations</title>
<style>
  :root { --bg:#0f1115; --panel:#171a21; --ink:#e7e9ee; --muted:#9aa3b2;
          --line:#2a2f3a; --accent:#7bbf6a; }
  * { box-sizing: border-box; }
  body { margin:0; font:15px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;
         background:var(--bg); color:var(--ink); }
  header { padding:14px 20px; border-bottom:1px solid var(--line);
           display:flex; align-items:center; gap:12px; }
  header h1 { font-size:16px; margin:0; font-weight:650; }
  header h1 .g { color:var(--accent); }
  .wrap { display:grid; grid-template-columns: 1fr 360px; gap:0; height:calc(100vh - 53px); }
  .left { padding:18px 20px; overflow:auto; }
  textarea { width:100%; height:90px; background:var(--panel); color:var(--ink);
             border:1px solid var(--line); border-radius:8px; padding:10px; resize:vertical;
             font:14px/1.5 ui-monospace,Menlo,monospace; }
  .row { display:flex; gap:10px; align-items:center; margin:10px 0 16px; }
  button { background:var(--accent); color:#0b0d10; border:0; border-radius:7px;
           padding:8px 14px; font-weight:650; cursor:pointer; }
  button.ghost { background:transparent; color:var(--muted); border:1px solid var(--line); }
  #doc { font-size:16px; line-height:2.1; }
  .legend { color:var(--muted); font-size:12px; margin-left:auto; }
  .pill { border-radius:999px; padding:1px 8px; cursor:pointer; white-space:nowrap;
          border:1px solid transparent; }
  .pill.item { border-style:dashed; }
  .pill.sel { outline:2px solid var(--ink); }
  aside { background:var(--panel); border-left:1px solid var(--line); padding:16px 18px; overflow:auto; }
  aside h2 { font-size:13px; text-transform:uppercase; letter-spacing:.04em;
             color:var(--muted); margin:0 0 6px; }
  .ent-title { font-size:18px; font-weight:650; margin:2px 0 2px; }
  .sub { color:var(--muted); font-size:12px; margin-bottom:12px; }
  .field { margin:8px 0; }
  .k { color:var(--muted); font-size:12px; }
  .tag { display:inline-block; background:#222836; border:1px solid var(--line);
         border-radius:6px; padding:1px 7px; margin:2px 4px 2px 0; font-size:12px; }
  .assoc { border:1px solid var(--line); border-radius:8px; padding:8px 10px; margin:6px 0; }
  .assoc .w { float:right; color:var(--accent); font-variant-numeric:tabular-nums; }
  .empty { color:var(--muted); font-style:italic; }
  #tip { position:fixed; pointer-events:none; z-index:9; max-width:300px;
         background:#0b0d10; border:1px solid var(--line); border-radius:8px;
         padding:8px 10px; font-size:12.5px; color:var(--ink); display:none;
         box-shadow:0 6px 24px rgba(0,0,0,.5); }
  #tip b { color:var(--accent); }
</style></head>
<body>
<header><h1><span class="g">Hob</span>goblin annotations</h1>
  <span class="legend">solid = entity · dashed = item · click an entity for details</span>
</header>
<div class="wrap">
  <div class="left">
    <textarea id="input"></textarea>
    <div class="row">
      <button id="go">Annotate</button>
      <button class="ghost" id="reset">Reset text</button>
      <span id="status" class="legend"></span>
    </div>
    <div id="doc"></div>
  </div>
  <aside id="panel"><p class="empty">Click an entity pill to inspect its elements.</p></aside>
</div>
<div id="tip"></div>
<script>
const DEFAULT_TEXT = __DEFAULT_TEXT__;
const CAT_COLORS = { name:"#caa24a", military_unit:"#6fa8dc", facility:"#7bbf6a",
  equipment:"#cd7be0", entity:"#3a4150" };
const ITEM_COLORS = { phone:"#e08a4a", email:"#e08a4a", url:"#e08a4a",
  address:"#7bbf6a", coordinate:"#7bbf6a", date:"#6fa8dc", time:"#6fa8dc",
  money:"#caa24a", percent:"#caa24a", default:"#5a6275" };
let state = { data:null, sel:null };

function esc(s){ const d=document.createElement("div"); d.textContent=s; return d.innerHTML; }

function entColor(e){ return CAT_COLORS[(e.anchors_matched||[])[0]] || CAT_COLORS.entity; }
function itemColor(it){ return ITEM_COLORS[it.type] || ITEM_COLORS.default; }

function buildRanges(d){
  const r=[];
  d.entities.forEach((e,i)=>r.push({s:e.span[0],e:e.span[1],kind:"entity",i}));
  d.items.forEach((it,i)=>r.push({s:it.span[0],e:it.span[1],kind:"item",i}));
  r.sort((a,b)=> a.s-b.s || (a.kind==="entity"?-1:1) || (b.e-b.s)-(a.e-a.s));
  const kept=[]; let last=-1;
  for(const x of r){ if(x.s>=last){ kept.push(x); last=x.e; } }
  return kept;
}

function tipForEntity(e){
  const cats=(e.anchors_matched||[]);
  let t = "<b>Entity</b> · head: "+esc(e.head)+"<br>type: "+(cats.length?cats.join(", "):"untyped");
  if(e.mil_unit){ const m=e.mil_unit;
    t += "<br>unit: "+esc(m.echelon)+" "+esc(""+m.designation)+" ("+m.designation_form+")"; }
  const n=(e.associations||[]).length;
  t += "<br>"+n+" associated item"+(n===1?"":"s");
  return t;
}
function tipForItem(it){
  const be=it.best_entity;
  let t = "<b>Item</b> · "+esc(it.type)+"<br>“"+esc(it.text)+"”";
  if(be) t += "<br>associated to <b>"+esc(be.head)+"</b> (w="+be.weight+")";
  return t;
}

function showTip(htmlStr, x, y){
  const tip=document.getElementById("tip");
  tip.innerHTML=htmlStr; tip.style.display="block";
  tip.style.left=Math.min(x+14, innerWidth-tip.offsetWidth-10)+"px";
  tip.style.top=(y+16)+"px";
}
function hideTip(){ document.getElementById("tip").style.display="none"; }

function renderDoc(){
  const d=state.data, doc=document.getElementById("doc"); doc.innerHTML="";
  let cur=0;
  for(const r of buildRanges(d)){
    if(r.s>cur) doc.appendChild(document.createTextNode(d.text.slice(cur,r.s)));
    const ref = r.kind==="entity" ? d.entities[r.i] : d.items[r.i];
    const span=document.createElement("span");
    span.className="pill "+r.kind;
    span.textContent=d.text.slice(r.s,r.e);
    const col = r.kind==="entity" ? entColor(ref) : itemColor(ref);
    span.style.background = col+"33"; span.style.borderColor = col;
    span.addEventListener("mousemove", ev =>
      showTip(r.kind==="entity"?tipForEntity(ref):tipForItem(ref), ev.clientX, ev.clientY));
    span.addEventListener("mouseleave", hideTip);
    if(r.kind==="entity"){
      span.addEventListener("click", ()=>{ state.sel=r.i; renderDoc(); renderPanel(ref); });
      if(state.sel===r.i) span.classList.add("sel");
    }
    doc.appendChild(span); cur=r.e;
  }
  if(cur<d.text.length) doc.appendChild(document.createTextNode(d.text.slice(cur)));
}

function field(k, v){ return '<div class="field"><span class="k">'+k+'</span><br>'+v+'</div>'; }

function renderPanel(e){
  const c=e.context, p=document.getElementById("panel");
  let h = '<div class="ent-title">'+esc(e.entity)+'</div>';
  h += '<div class="sub">head “'+esc(e.head)+'” · '+esc(e.pattern)+' · '+esc(e.head_pos||"")+'</div>';
  if((e.anchors_matched||[]).length)
    h += field("categories", e.anchors_matched.map(a=>'<span class="tag">'+esc(a)+'</span>').join(""));
  if(e.mil_unit){ const m=e.mil_unit;
    h += field("military unit", esc(m.echelon)+" #"+esc(""+m.designation)+" ("+m.designation_form+")"
       + (m.branch? " · "+esc(m.branch):"")); }
  if(c.verb) h += field("governing verb", esc(c.verb.text)+' <span class="k">('+esc(c.verb.lemma)+')</span>');
  if(c.subject) h += field("subject", esc(c.subject.text));
  if(c.count){ const ct=c.count; let s="value "+ct.value;
    if(ct.range) s+=" · range ["+ct.range.join(", ")+"]";
    if(ct.approx) s+=" · approx “"+esc(ct.qualifier)+"”";
    if(ct.measure) s+=" · "+esc(ct.measure.text)+" "+esc(ct.helper.text);
    h += field("count", s); }
  if((c.dates||[]).length)
    h += field("dates", c.dates.map(d=>'<span class="tag">'+esc(d.text)+'</span>').join(""));
  if((e.modifiers||[]).length)
    h += field("modifiers", e.modifiers.map(m=>'<span class="tag">'+esc(m.text)+'</span>').join(""));

  h += '<h2 style="margin-top:16px">Associated items</h2>';
  if((e.associations||[]).length){
    for(const a of e.associations){
      const sig=a.signals||{};
      h += '<div class="assoc" data-tip="'+esc(JSON.stringify(a))+'">'
        + '<span class="w">w='+a.weight+'</span>'
        + '<b>'+esc(a.type)+'</b> · “'+esc(a.text)+'”'
        + '<div class="k">token dist '+sig.token_distance
        + ' · dep dist '+(sig.dep_distance==null?"—":sig.dep_distance)
        + ' · same sentence: '+sig.same_sentence+'</div></div>';
    }
  } else { h += '<p class="empty">none</p>'; }
  p.innerHTML=h;

  p.querySelectorAll(".assoc").forEach(el=>{
    const a=JSON.parse(el.getAttribute("data-tip"));
    el.addEventListener("mousemove", ev=> showTip(
      "<b>"+esc(a.type)+"</b> item<br>“"+esc(a.text)+"”<br>associated to <b>"+esc(e.head)
      +"</b> (w="+a.weight+")", ev.clientX, ev.clientY));
    el.addEventListener("mouseleave", hideTip);
  });
}

async function annotate(){
  const text=document.getElementById("input").value;
  const st=document.getElementById("status"); st.textContent="working…";
  const res=await fetch("/api/extract",{method:"POST",headers:{"Content-Type":"application/json"},
    body:JSON.stringify({text})});
  state.data=await res.json(); state.sel=null;
  st.textContent=state.data.entities.length+" entities · "+state.data.items.length+" items";
  renderDoc();
  document.getElementById("panel").innerHTML='<p class="empty">Click an entity pill to inspect its elements.</p>';
}

document.getElementById("go").addEventListener("click", annotate);
document.getElementById("reset").addEventListener("click", ()=>{
  document.getElementById("input").value=DEFAULT_TEXT; annotate(); });
document.getElementById("input").value=DEFAULT_TEXT;
annotate();
</script></body></html>
"""


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype):
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            page = PAGE.replace("__DEFAULT_TEXT__", json.dumps(DEFAULT_TEXT))
            self._send(200, page, "text/html; charset=utf-8")
        else:
            self._send(404, "not found", "text/plain")

    def do_POST(self):
        if self.path != "/api/extract":
            self._send(404, "not found", "text/plain")
            return
        length = int(self.headers.get("Content-Length", 0))
        payload = json.loads(self.rfile.read(length) or b"{}")
        text = payload.get("text", "")
        ents = extract(text, anchors=ANCHORS)
        result = {"text": text, "entities": ents, "items": item_index(ents)}
        self._send(200, json.dumps(result), "application/json")

    def log_message(self, *args):  # quiet
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()
    print("Loading spaCy model…")
    extract("warm up the model")  # so the first request is fast
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Hobgoblin viewer running at http://localhost:{args.port}  (Ctrl-C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")


if __name__ == "__main__":
    main()
