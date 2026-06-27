"""Ready-made anchor pack so you don't hand-build term lists.

``ANCHORS`` is a categorized anchor dict you can pass straight to
``extract(text, anchors=ANCHORS)``, or copy and extend. It is meant to be generic:
category keys are namespaced by domain (e.g. ``military_unit``) so you can mix in
your own categories — ``medical_facility``, ``legal_party``, ``vehicle``, etc. —
without collisions.

Each category maps to a list of terms; the special ``name`` category uses the
``NAME`` sentinel for rule-based person detection instead of a word list.

These lists are intentionally non-exhaustive starting points — extend them for your
corpus. Abbreviations are upper-case so they match exactly (no fuzzy collisions);
spelled-out words match fuzzily, so most typos are caught without listing them all.
"""

from .anchors import NAME, PLACE, ORG, GROUP, EVENT, PRODUCT, WORK

# Deterministic gazetteers — a backstop to spaCy's GPE/LOC NER (which degrades on
# all-caps / de-cased text). Full names only: 2-letter abbreviations like "OR"/"IN"
# would collide with common words under case-insensitive matching.
US_STATES = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
    "Washington", "Wisconsin", "Wyoming",
    "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
    "North Dakota", "Rhode Island", "South Carolina", "South Dakota",
    "West Virginia",
]
COUNTRIES = [
    "Afghanistan", "Argentina", "Australia", "Austria", "Bangladesh", "Belgium",
    "Brazil", "Canada", "Chile", "China", "Colombia", "Cuba", "Denmark", "Egypt",
    "England", "Ethiopia", "Finland", "France", "Germany", "Greece", "India",
    "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Japan", "Jordan",
    "Kenya", "Kuwait", "Lebanon", "Mexico", "Morocco", "Netherlands",
    "New Zealand", "Nigeria", "Norway", "Pakistan", "Peru", "Philippines",
    "Poland", "Portugal", "Qatar", "Romania", "Russia", "Saudi Arabia",
    "Scotland", "Singapore", "Somalia", "South Korea", "Spain", "Sweden",
    "Switzerland", "Syria", "Taiwan", "Thailand", "Turkey", "Ukraine",
    "United Kingdom", "United States", "Venezuela", "Vietnam", "Wales", "Yemen",
]

ANCHORS = {
    "military_unit": [
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
    # NER GPE/LOC rule first (cities + anything spaCy tags), gazetteer as backstop.
    "place": [PLACE] + COUNTRIES + US_STATES,
    # General-purpose scopes, free via spaCy NER (no word lists needed).
    "organization": [ORG],
    "group": [GROUP],
    "event": [EVENT],
    "product": [PRODUCT],
    "work": [WORK],
}
