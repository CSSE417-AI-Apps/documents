# Slides conventions

Decks are Marp-flavored Markdown. Students present them in VS Code (Marp extension) **and** read them directly on github.com, so every deck must read well in both places:

- Start with front matter: `marp: true` and `paginate: true`. Keep the front matter minimal, because GitHub renders it as a table at the top.
- Separate slides with `---`. On GitHub these show up as horizontal rules.
- Put speaker notes and Marp directives (e.g. `<!-- _class: lead -->`) in HTML comments. GitHub hides them.
- **Don't** use Marp background-image syntax (`![bg ...]`) or image sizing like `![w:300]`. GitHub shows those as full-size inline images. Use `<img src="..." width="...">` instead.
- Don't use custom themes or `<style>` blocks.
- File naming: `DayNN_Short_Topic.md`, where NN is the calendar's Day number. Images go in `Slides/images/`.
- Link each deck from its row in the root `README.md` calendar.

## Images

- Diagrams are hand-written SVGs in `images/`, in one flat icon style: wordless icons with a bold label under each, gray arrows between them. Palette: orange `#E8572A`, charcoal `#1F2937`, gold `#E0A800`, blue `#4A90E2`, green `#2BB673`, gray `#9CA3AF`. Font: Helvetica/Arial (Menlo for filenames).
- "You are here" = a dashed orange rounded rectangle (`fill #FFF4EF`, `stroke #E8572A`, `stroke-dasharray 10 8`) behind the item, with its label turned orange.
- `phase0_stages.svg` is the base Phase 0 strip. `python3 make_highlights.py` (run in `images/`) regenerates its highlighted copies (`phase0_stage1_…` through `phase0_stage6_…`, `phase0_part1_data`, `phase0_part2_vectors`). Edit the base, then rerun.
- Use Mermaid only when a diagram really needs it. Marp doesn't render Mermaid code blocks, so render it to SVG first with `npx -p @mermaid-js/mermaid-cli mmdc`.
- To preview an SVG without a browser: `qlmanage -t -s 1000 -o <dir> file.svg` (pad the viewBox to a square first, or Quick Look crops it).
- In slides, link search-result times to the mp3 with `#t=SECONDS` so they can be clicked during a live demo.

