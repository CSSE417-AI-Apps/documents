# CSSE 417 Course Plan (working notes)

Instructor-facing planning doc. It changes often, and students aren't expected to read it.

## Projects

### Project 1: Podcast Agent website (first project; gets students started with AI tools)
- Each team picks a podcast.
- They build a vector database from its transcripts.
- They build a custom AI interface that lets people search the podcast and discuss its content.
- Platform: GCP / Vertex AI / Gemini.
- The implementation lives in a separate repo; this repo holds only the instructions.

### Project 2: CSSE120_AI_TA (idea stage)
- Load in the course material from CSSE120 (lectures, homeworks, etc.).
- Design and build an AI TA bot that CSSE120 students can use freely.
- The bot limits how much it helps and uses sound learning techniques (hints, Socratic questions), so it doesn't hand out solutions.
- Ways it builds on Project 1, rather than repeating it:
  - Guardrails and a help policy (how much help is too much?)
  - Evals: a test set of student questions, including attempts to get the bot to give away the answer
  - Possibly agentic tools, such as running or checking student code
  - Production concerns: Rose-Hulman login, rate limits and cost caps, logging and privacy
- Decisions so far:
  - Proof of concept only. Dr. Fisher will talk to the CSSE120 instructors, but nobody expects them to adopt it.
  - Pilot: CSSE120 students work through a *prior* homework with the bot as a guided exercise (no live coursework, so no integrity risk).
  - Project 1 is the retrieval project. Project 2 is about agent behavior and evaluation.
- Draft architecture:
  - Course knowledge: try long context (load the whole CSSE120 corpus into Gemini with context caching) instead of RAG. This contrasts with Project 1, and the question "RAG vs. long context, when?" is a lesson on its own.
  - Help policy as an explicit hint ladder: (0) ask what they've tried → (1) Socratic question → (2) point to the relevant lecture/concept → (3) a worked example on a *different* problem → never the solution. The bot tracks which level each student is on.
  - The bot sees the instructor solutions (hidden from students) so it can find the student's actual bug.
  - Output guardrail: a second check (LLM judge and/or similarity to the solution code) blocks any reply that leaks the solution.
  - Agent tools: run the student's code in a sandbox, run the unit tests, look up a lecture or slide.
  - Framework: probably Google ADK on GCP (fits the Vertex/Gemini platform).
  - Evals: simulated students (an LLM playing a confused student, a lazy student, a jailbreaker) chat with the TA. An LLM judge scores each chat for leaks, correctness, and helpfulness. Then the human pilot plus a survey.
- Draft milestones: (1) help policy doc + test set → (2) baseline bot (long context + system prompt) → (3) hint ladder + guardrail → (4) tools → (5) automated eval report → (6) pilot with CSSE120 students + final report
- Still open: one shared bot vs. one per team; which CSSE120 materials and homeworks to load

### Later projects
- TBD

## Weekly topic outline
- TBD (39 meetings: see CLAUDE.md for the date structure)

## Git and GitHub policy (decided Nov 2026)
- Every project is team work: teams of 3 (2 at minimum). There are no solo assignments, so every PR has a teammate who can review it.
- All code lives in a **public** repo in the [CSSE417-AI-Apps](https://github.com/CSSE417-AI-Apps) org. No GitHub Education or paid plan; public repos get rulesets for free.
- Repo names follow `<project-name>-team<NN>`. Teams pick the lowest unused number themselves (no central assignment).
- `main` is protected by a per-repo ruleset that each team creates: PR required, 1 approval, stale approvals dismissed. Students do this in [GitHub_New_Repo.md](Guides/GitHub_New_Repo.md).
- Humans commit, push and open PRs in GitHub Desktop. Claude Code may resolve conflicts and use read-only git. This is enforced with words (each repo's `CLAUDE.md`), not `.claude/settings.json` deny rules, for now.
- GitHub MCP: read-only fine-grained token (resource owner: the student, "Public repositories"), so no org token-approval step for Dr. Fisher. Claude **drafts** review comments; students post them. Consider loosening this after Project 1.
- Project 0 (git workflow) introduces all of this. It also collects podcast proposals for Project 1.

### One-time org setup (Dr. Fisher)
- Invite students by GitHub username, taken from the team sign-up spreadsheet on Moodle.
- Org **Settings → Member privileges**: allow members to create **public** repositories; base permission **No permission**. Public repos are readable by everyone anyway, and this keeps any private instructor repo in the org hidden from students.
- Instructor repos (`documents`, demos, starter code) have no ruleset; the PR rule is for student work. Solutions live outside the course org, in a private repo under Dr. Fisher's personal account.
- Next year: repo names would collide with this year's. Use a new org, or add a term prefix to the naming pattern.

## Open decisions
- Grading breakdown
- Google Cloud Teaching Credits: applied, waiting on a decision
