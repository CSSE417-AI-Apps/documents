# Slides conventions

Decks are Marp-flavored Markdown. Students present them in VS Code (Marp extension) **and** read them directly on github.com, so every deck must read well in both places:

- Start with front matter: `marp: true` and `paginate: true`. Keep the front matter minimal, because GitHub renders it as a table at the top.
- Separate slides with `---`. On GitHub these show up as horizontal rules.
- Put speaker notes and Marp directives (e.g. `<!-- _class: lead -->`) in HTML comments. GitHub hides them.
- **Don't** use Marp background-image syntax (`![bg ...]`) or image sizing like `![w:300]`. GitHub shows those as full-size inline images. Use `<img src="..." width="...">` instead.
- Don't use custom themes or `<style>` blocks.
- File naming: `DayNN_Short_Topic.md`, where NN is the calendar's Day number. Images go in `Slides/images/`.
- Link each deck from its row in the root `README.md` calendar.
