# Project 2: CSSE120 AI TA

> **DRAFT.** These instructions are still being written. Dates and grading weights may change.

## Overview

Build an AI teaching assistant for CSSE120 (Introduction to Software Development). Students should be able to use it freely, and it should **help them learn without doing their homework for them**.

Project 1 was about *finding* the right information. Project 2 is about *controlling behavior* and *proving that the control holds*. Your TA will have access to the full CSSE120 course, including the instructor solutions, but it must never hand a solution over. Doing that well is mostly a design and testing problem, not a coding problem.

At the end of the term you'll run a pilot: real CSSE120 students will work through a **past** homework with your TA, and you'll find out whether it actually helps.

> This is a proof of concept. CSSE120 isn't adopting it for its live course, and the pilot only uses homework that has already been graded.

## Team and repo

- **Team size:** 3.
- **Repo name:** `csse120-ai-ta-team<NN>`. Use your team number; see [picking the repo name](../Guides/GitHub_New_Repo.md#1-pick-the-repo-name).
- Set up the repo with [Making a new repo](../Guides/GitHub_New_Repo.md): public, in the CSSE417-AI-Apps org, with `main` protected.
- Every change goes through [the PR workflow](../Guides/GitHub_PR_Workflow.md), with a teammate's approval.

> [!CAUTION]
> **Your repo is public. Never commit CSSE120 course materials, homework solutions, or pilot chat logs to it.** Your code loads them at runtime from the private Google Cloud Storage bucket Dr. Fisher gives you *(TODO: add bucket name)*. Add the local copies' folder to `.gitignore` on day one. A solution leaked through GitHub is the worst way to fail this project.

## Learning objectives

By the end of this project you should be able to:

1. Turn a fuzzy goal ("help, but not too much") into a written policy that someone can test.
2. Choose between retrieval (RAG) and long context for a given corpus, and back up the choice with measurements.
3. Build an agent with tools using an agent framework (Google's Agent Development Kit, ADK).
4. Add a guardrail that checks a model's output before the user sees it.
5. Build an automated evaluation: a test set, simulated users, and a model that grades the conversations.
6. Run a small study with real users and report honestly on what you find.

## What you're building

```
 CSSE120 student
      │
      ▼
┌──────────────┐   ┌───────────────────────────────────────────────┐
│ Web chat UI  │──▶│ TA agent (ADK + Gemini)                       │
│ (Rose login) │   │  • system prompt = your help policy           │
└──────────────┘   │  • course knowledge (cached long context)     │
      ▲            │  • hidden solutions (never shown directly)    │
      │            │  • per-student state: hint level, attempts    │
      │            │  • tools: run_code, run_tests, find_lecture   │
      │            └──────────────────────┬────────────────────────┘
      │                                   │ draft reply
      │            ┌──────────────────────▼────────────────────────┐
      └────────────│ Leak guardrail: does this reply give away     │
     safe reply    │ the solution? If so, block and regenerate.    │
                   └───────────────────────────────────────────────┘
```

### 1. Course knowledge: long context, not RAG

The CSSE120 corpus (slides, readings, homework specs, and solutions) is small enough to fit in Gemini's context window. Your baseline loads **all of it** into the prompt, using Vertex AI **context caching** so you don't pay for those tokens on every turn.

You already built RAG in Project 1. Here you'll **measure** the trade-off: cost per conversation, latency, and answer quality with long context, compared with a simple retrieval version. That comparison goes in your final report. "It depends" is a fine conclusion if you can say *on what*.

### 2. The help policy: a hint ladder

Write your policy first, before any code, using the [help policy template](Project_2_Help_Policy_Template.md). At its core is a **hint ladder**: the TA climbs one rung at a time, and only after the student has shown some effort.

| Rung | The TA… | Example |
|:---:|---|---|
| 0 | Asks what the student has tried and what they expected | "What did you expect `range(1, n)` to give you when `n` is 5?" |
| 1 | Asks a guiding (Socratic) question | "How many times does your loop run? Can you trace it by hand?" |
| 2 | Points to the concept and the lecture or reading that covers it | "This is an off-by-one error. See Session 9's slides on `range`." |
| 3 | Shows a worked example on a **different** problem | Fixes a similar loop that sums squares, not the homework loop |
| — | **Never** writes or fixes the student's homework code | |

Concept questions ("what's the difference between a list and a tuple?") don't need the ladder. The TA can just teach. Your policy has to define where that line is.

The agent tracks a **hint level per student, per problem**, so a student can't skip to rung 3 by starting a new message.

### 3. Hidden solutions

The TA gets the instructor solutions so it can find a student's *actual* bug instead of guessing. That makes it more useful, and also more dangerous. Keep the solutions in a part of the prompt the policy tells the model never to quote, and rely on the guardrail (next section), not on the prompt alone.

### 4. The leak guardrail

Every draft reply goes through a check before the student sees it. Use at least **two** of these:

- **LLM judge:** a second Gemini call that answers "Does this reply contain or directly reveal the solution to problem X?", returning structured output (`leak: true/false`, `reason`).
- **Code similarity:** compare any code in the reply with the solution code (normalized tokens, or AST comparison with Python's `ast` module). Block replies above a threshold you choose and justify.
- **Rules:** for example, no code block longer than N lines that uses the homework's function names.

When a reply is blocked, regenerate it with the judge's reason attached. Log every block; the counts go in your eval report.

### 5. Agent tools

Build these as ADK tools:

| Tool | What it does | Notes |
|---|---|---|
| `run_code(code)` | Runs the student's code and returns its output or traceback | Must run in a sandbox: Gemini's built-in code execution, or a locked-down container on Cloud Run. **Never** `exec()` student code in your server process. Enforce time and memory limits. |
| `run_tests(problem_id, code)` | Runs the homework's unit tests against the student's code | Return *which* tests fail. Whether to show the test code is a policy decision. |
| `find_lecture(topic)` | Returns the session, slide, or reading that covers a topic | Supports hint rung 2. |

At least one more tool of your own design is required. Ideas: "explain this error message," "make a similar practice problem," "trace this loop step by step."

### 6. Production concerns

- **Login:** only `@rose-hulman.edu` users can use the TA. You choose how (for example Firebase Authentication or Identity-Aware Proxy).
- **Cost caps:** a per-user daily message limit, plus a budget alert on your GCP project.
- **Logging and privacy:** log conversations to a **private** store (Firestore or a private bucket), with each student identified by a random ID, not by name or email. Pilot logs are deleted at the end of the term.
- **Deployment:** Cloud Run, reachable at a stable URL.

### 7. Evaluation

Read the [evaluation guide](Project_2_Evaluation_Guide.md). In short:

- A **test set** of at least 40 cases, in your repo as `evals/test_cases.jsonl`, written *before* you tune the prompt.
- **Simulated students:** an LLM plays a student persona (confused beginner, lazy student, determined jailbreaker, and others) and chats with your TA for several turns.
- A **grader** (LLM judge) scores every conversation on the rubric: leaks, correctness, helpfulness, and following the policy.
- A single script runs everything and writes a report: `python -m evals.run`.
- Run it after every major change and keep the results. You'll show how the scores changed between versions.

### 8. Pilot with CSSE120 students

See the [pilot guide](Project_2_Pilot_Guide.md). A few CSSE120 students work through a past homework with your TA during a guided session, then fill out a short survey. Compare what real students did with what your simulated students did.

## Milestones

| # | Milestone | What's due | Due (tentative) |
|:---:|---|---|---|
| M1 | Policy and test set | `POLICY.md` (from the template), `evals/test_cases.jsonl` with at least 40 cases, repo set up with `.gitignore` for course data | Week 6 |
| M2 | Baseline TA | ADK agent with cached long context and your policy as the system prompt; command-line chat works; first eval run (even if manual) | Week 7 |
| M3 | Hint ladder and guardrail | Per-student hint-level state; leak guardrail with at least two checks; eval shows the leak rate before and after | Week 8 |
| M4 | Tools and deployment | `run_code`, `run_tests`, `find_lecture` and your own tool; web UI on Cloud Run with Rose login and cost caps | Week 9 |
| M5 | Automated eval | `python -m evals.run` runs simulated students and the grader end to end; eval report checked in | Week 9 |
| M6 | Pilot and final report | Pilot session run; final report; demo in class | Week 10 |

## Deliverables

All in your team repo unless noted:

- `POLICY.md`: your help policy
- `evals/`: the test set, personas, grader prompt, runner script, and one report per milestone (`evals/reports/`)
- The agent and web app source code, with a `README.md` explaining how to run it locally and how it's deployed
- The deployed URL (in the README)
- `REPORT.md`, the final report, covering:
  - Architecture and the main design decisions
  - Long context vs. RAG: your measurements and your recommendation
  - How eval scores changed from M2 to M5, and what changes caused the biggest improvements
  - Failures you didn't fix: the best jailbreaks against your TA
  - Pilot results, and where the simulated students and real students differed
  - Cost: what a CSSE120 section would cost per term at your measured usage
- A 10-minute demo in class

## Grading

| Component | Weight (draft) |
|---|---:|
| M1: Policy and test set | 10% |
| M2: Baseline TA | 10% |
| M3: Hint ladder and guardrail | 15% |
| M4: Tools and deployment | 15% |
| M5: Automated eval | 20% |
| M6: Pilot, final report, demo | 25% |
| Team PR practice (reviews, small PRs, everyone contributing) | 5% |

Your TA doesn't have to be unbreakable to earn a high grade. A TA with a 10% leak rate that you measured honestly and analyzed well beats one that claims 0% with a weak test set.

## Starting points

- [Google Agent Development Kit (ADK) documentation](https://google.github.io/adk-docs/)
- [Vertex AI context caching overview](https://cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview)
- CSSE120 course materials: private bucket *(TODO: add bucket name)*
