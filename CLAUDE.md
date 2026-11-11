# CSSE 417 — Designing and Building AI Systems (documents repo)

Course documents for CSSE 417 at Rose-Hulman, taught by Dr. Fisher. This is the flagship course of Rose-Hulman's new AI major, being offered for the first time as a special Winter 2026-2027 offering — so most content is being authored from scratch here.

Catalog description: developing AI applications with modern agentic frameworks; the full AI system design process from problem formulation through production testing; architecting, deploying, and evaluating real AI solutions; and using AI tools to generate code. Prereq: CSSE 316. ~24 students.

## What lives here (and what doesn't)

This repo holds **student-facing course documents only**, all in Markdown rendered on GitHub:

- The course calendar (the main entry point — see below)
- Setup/installation guides (e.g. getting Google Cloud / GCP teaching credits)
- Labs and project instructions (e.g. the Podcast Agent project), with full details of what is due and when
- Lecture slides, also in `.md`

**Code does not live here.** Project implementations (e.g. the Podcast Agent website) go in separate repos. Don't add app code to this repo.

### Layout

- `README.md`: course landing page and calendar
- `Guides/`: setup guides (GCP credits, tools)
- `Labs/`: labs and project instructions (`Project_1_Podcast_Agent.md`, ...)
- `Slides/`: Marp-flavored lecture decks. See `Slides/CLAUDE.md` for the format rules.
- `.claude/skills/`: project skills (`calendar-edit` for any change to the calendar)

Course design notes, open decisions, and the evolving plan live in `COURSE_PLAN.md` — read it before authoring new content. Keep this CLAUDE.md for stable rules; put changing plans there.

## The calendar

- The calendar is in the root `README.md`, so it's the first thing students see on GitHub. It's just "the calendar" for now; in future years it will be archived as the Winter 2026-2027 calendar.
- Format is a **Markdown table** modeled on Dr. Fisher's earlier HTML calendars (most recent: `/Users/davidfisher/Documents/Rose/github/course-calendars/ME435/fall_2026_2027.html`). No HTML pages — Markdown only.
- The class meets **Monday, Tuesday, Thursday, Friday**. Don't put the meeting time on the calendar.
- The `Day` column counts class meetings (1..39) and is separate from the `Week` divider rows. Keep meeting order intact when holidays make weeks irregular.
- Every displayed weekday must match its date. Check this (e.g. with `cal`) after any calendar edit.

### Winter 2026-2027 dates (source: Rose-Hulman 2026-27 academic calendar)

| Date | Event |
|---|---|
| Mon Nov 30, 2026 | Classes begin |
| Wed Dec 2 | Registration deadline |
| Fri Dec 4 | Last day to add a class |
| Fri Dec 18 | Holiday vacation begins after last class |
| Mon Jan 4, 2027 | Classes resume |
| Mon Jan 18 | MLK Day: no class |
| Tue Jan 19 | Midterm progress reports due (noon) |
| Jan 25-29 | Spring registration (classes in session) |
| Fri Feb 5 | Last day to drop with W |
| Feb 22-25 | Final exams |
| Mon Mar 1 | Final grades due 9:00 a.m.; term ends |

Meeting weeks: Weeks 1-3 = Nov 30 – Dec 18 (12 meetings), holiday break, Weeks 4-10 = Jan 4 – Feb 19 (Week 6 has 3 meetings because of MLK Day). **39 meetings total**, then finals week.

## Platform / tools

- Planned cloud platform: **Google Cloud (GCP), Vertex AI, and Gemini**, funded by Google Cloud Teaching Credits (applied for; decision pending as of Nov 2026). Guides should assume students use rose-hulman.edu accounts.

## Conventions

- Markdown that renders correctly on github.com. Use relative links between docs so they work on GitHub.
- Images go in an `images/` folder next to the doc that uses them, with descriptive filenames. Embed them with HTML `<img>` tags with an explicit `width` (same convention as the ME435 documents repo).
- If you rename a heading, update any links that point to its GitHub anchor slug.
- Don't guess at private Rose-Hulman or Moodle links. Mark them `*(TODO: add link)*`.
- Make focused edits, and don't commit unless asked.
