"""Ready-made anchor packs so you don't hand-build term lists.

``MILITARY_ANCHORS`` is a categorized anchor dict (unit / facility / equipment /
name) seeded with echelon words, common abbreviations, and frequent misspellings.
Pass it straight to ``extract(text, anchors=MILITARY_ANCHORS)``, or copy and extend.

These lists are intentionally non-exhaustive starting points — extend them for your
corpus. Abbreviations are upper-case so they match exactly (no fuzzy collisions);
spelled-out words match fuzzily, so most typos are caught without listing them all.
"""

from .anchors import NAME

MILITARY_ANCHORS = {
    "unit": [
        # echelons (matched fuzzily — typos tolerated)
        "army", "corps", "division", "brigade", "regiment", "battalion",
        "company", "battery", "squadron", "platoon", "troop", "section",
        "squad", "detachment", "team", "element", "task force",
        # common misspellings worth pinning explicitly
        "brigdae", "batallion", "battallion", "regimnet", "squardron",
        # abbreviations (exact-match, upper-case)
        "BDE", "BN", "CO", "BTRY", "BTY", "BAT", "PLT", "REGT", "RGT",
        "DIV", "BCT", "TF", "DET", "SQDN", "SQN", "CAV", "INF", "ABN",
        "ARMD", "FA", "ADA", "MP", "EN", "SF",
    ],
    "facility": [
        "base", "barracks", "depot", "airfield", "airbase", "headquarters",
        "compound", "garrison", "outpost", "checkpoint", "bunker", "hangar",
        "armory", "armoury", "arsenal", "motor pool", "building", "facility",
        "installation", "post", "camp", "fort", "station",
        "HQ", "FOB", "COP", "TOC", "DFAC", "MWR",
    ],
    "equipment": [
        "tank", "rifle", "carbine", "pistol", "machine gun", "howitzer",
        "mortar", "artillery", "missile", "rocket", "launcher", "radar",
        "helicopter", "drone", "truck", "vehicle", "humvee", "transport",
        "grenade", "radio", "antenna", "generator",
        "HMMWV", "APC", "IFV", "MBT", "UAV", "MRAP", "SAM", "RPG",
        "IED", "NVG", "GPS",
    ],
    "name": NAME,
}
