# Project 2: Pilot Guide

> **DRAFT.** Part of [Project 2: CSSE120 AI TA](Project_2_CSSE120_AI_TA.md).

The pilot is where you find out whether your TA helps real students. Simulated students are useful, but they don't get frustrated, give up, or misread hints the way people do.

## Ground rules

- **Past homework only.** Participants work on a CSSE120 homework that has already been graded *(TODO: Dr. Fisher picks the homework)*. Nothing in the pilot counts toward their CSSE120 grade.
- **Volunteers only.** Participation is optional, and anyone can stop at any time.
- **Privacy:**
  - Logs use random IDs, not names or emails.
  - Logs stay in your private store, never in your public repo.
  - Logs are deleted at the end of the term.
  - Quotes in your report must be short and anonymous.
- **Recruiting goes through Dr. Fisher.** Don't contact CSSE120 students or instructors on your own.

## Before the session

- [ ] Your TA is deployed, and Rose login works for an account that isn't on your team.
- [ ] The cost cap and per-user message limit are on.
- [ ] The pilot homework and its solution are loaded, and your eval report shows a low leak rate on that homework.
- [ ] Each participant gets a starting file with realistic bugs, so they have something to fix. Use the same file for everyone.
- [ ] You've done a full dry run with someone from another team as the "student."
- [ ] Your survey is ready (below).

## The session (about 45 minutes)

| Time | What happens |
|---|---|
| 5 min | Welcome. Read the script below. |
| 30 min | Participants work on the homework using **only** your TA for help. You watch but don't help. Take notes on where they get stuck, ignore hints, or try to get the answer. |
| 10 min | Survey and a short conversation. |

**Script to read at the start** (adapt as needed):

> Thanks for helping. We're CSSE417 students testing an AI TA we built for CSSE120. You'll work on a homework you've already done. It won't affect your grade. Use the TA however you'd normally use help, including trying to get it to just give you the answer if that's what you'd really do. We're testing the TA, not you. Your chat is saved with a random ID, not your name, and we'll delete it at the end of the term. You can stop at any time.

## Survey

Keep it short. Use a 1–5 scale (1 = strongly disagree, 5 = strongly agree) for these:

1. The TA helped me make progress.
2. The TA's hints were clear.
3. The TA understood my actual problem.
4. I felt like I figured it out myself.
5. The TA was frustrating to use.
6. I'd use a TA like this on real homework.

Open-ended:

7. What was the most helpful thing it did?
8. What was the most annoying thing it did?
9. Did you try to get it to give you the answer? What happened?

## After the session

Put these in `REPORT.md`:

- How many participants, and how many finished the problem
- Survey results (with so few participants, report the actual counts, not just averages)
- Leaks or near misses seen in the real logs. Re-run your grader on the pilot conversations.
- **Simulated vs. real:** What did real students do that your personas never did? Which persona was most realistic? Add at least one new persona or test case based on what you saw.
- What you'd change before letting students use the TA on live homework
