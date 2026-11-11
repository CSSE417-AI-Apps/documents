---
name: calendar-edit
description: Edit the CSSE 417 course calendar table in the root README.md — add or change a day's topics and links, move content between days, cancel a class, or insert/remove a meeting — while keeping Day numbers, Week dividers, and weekday/date pairs correct. Use whenever the calendar's schedule or a day's contents change.
---

# Editing the course calendar

The calendar is the Markdown table under `## Calendar` in the root `README.md`. Columns: `Day | Date | Focus for the class day | References and links`.

## Row types

- **Meeting row:** `| 21 | Tuesday<br>Jan 19 | focus | links |`. Day is the meeting count (1..39). Date is the full weekday name, then `<br>`, then the abbreviated month and day (Nov, Dec, Jan, Feb).
- **Week divider:** `| **Week N** | | | |`, placed before the first meeting of each week.
- **Special rows:** `**Holiday Break**`, the MLK no-class row (blank Day cell), and `**Finals Week**`. These don't get Day numbers.
- **Institutional notes** go in italics after another `<br>` in the Date cell (e.g. `*Last day to add a class*`).

## Cell contents

- Separate multiple items in a cell with `<br>`, starting each with `• `. Markdown tables can't hold real lists.
- Use relative links: `[Project 1](Labs/Project_1_Podcast_Agent.md)`, `[Slides](Slides/Day05_Embeddings.md)`.
- Write due items as `**Due:** ...` and assignments as `**Assign:** ...` so they stand out.
- Escape any literal `|` inside a cell as `\|`.

## Procedure

1. Read the whole calendar table and the date table in the root `CLAUDE.md` first.
2. Make the requested change.
3. If meetings were added, removed or cancelled:
   - Renumber the Day column so it runs 1..N in order with no gaps. Cancelled days keep their row with a blank Day cell and an italic note.
   - Rename any slide files that use the old Day numbers (`Slides/DayNN_*.md`) and fix the links to them.
   - Check every "due on Day N" reference in `Labs/` against the new numbering.
4. Verify every weekday/date pair. Run this snippet and confirm it prints nothing:

   ```bash
   python3 - <<'PY'
   import re, datetime as dt
   for line in open("README.md"):
       m = re.search(r"\| (Monday|Tuesday|Wednesday|Thursday|Friday)<br>(\w+) (\d+)", line)
       if not m: continue
       wd, mon, d = m.groups()
       mi = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"].index(mon) + 1
       y = 2026 if mi >= 11 else 2027
       if dt.date(y, mi, int(d)).strftime("%A") != wd: print("MISMATCH:", line.strip())
   PY
   ```

5. Check that the class still meets only Mon, Tue, Thu and Fri, that there are no meetings Dec 21 – Jan 1 or on Jan 18, and that Week dividers stay at Weeks 1–10.
6. If the edit changed the term's structure (e.g. the meeting count), update the summary line in `CLAUDE.md`.
7. Report what changed in one or two lines. Don't commit unless asked.
