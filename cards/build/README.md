# Rebuilding the MVT flashcards

`cards_data.py` is the single source of truth. Every card is transcribed from
ESVS 2025 Chapter 7 (Eur J Vasc Endovasc Surg 2025;70:153–218, CC BY).

```bash
python3 cards_data.py    # writes ../cards.json
python3 build_page.py    # writes ../index.html from template.html
python3 build_apkg.py    # writes ../mvt-esvs-2025.apkg (needs: pip install genanki)
```

Anki note GUIDs are derived from each card's stable `id`, so re-importing an
updated `.apkg` updates existing notes and keeps review history.
