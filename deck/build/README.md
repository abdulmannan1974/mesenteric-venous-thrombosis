# Rebuilding the MVT teaching deck

Built with the Blood Doctor HTML deck skill (`blood-doctor-html-deck`), template
`knowledge-arch-blueprint`, theme `blueprint`. All clinical content is from ESVS 2025
Chapter 7 (Eur J Vasc Endovasc Surg 2025;70:153–218, CC BY). The teaching case is
constructed, not a real patient.

- `slides.html` — the 22 `<section class="slide">` blocks, with speaker notes
- `override.css` — brand layer: fixed 1920×1080 canvas scaled to the window,
  pinned footer, projector-sized type, components

```bash
python3 <skill>/scripts/build_deck.py --template knowledge-arch-blueprint --theme blueprint \
  --slides slides.html --brand-overrides override.css \
  --output ../index.html --title "Mesenteric Venous Thrombosis · Teaching Slides"
```

Keys: arrows/space navigate · S presenter window · O overview · N notes · F full screen.
