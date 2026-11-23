# Project 2: Help Policy Template

> **DRAFT.** Part of [Project 2: CSSE120 AI TA](Project_2_CSSE120_AI_TA.md).

Copy this file into your team repo as `POLICY.md` and fill in every section. Your policy is the **spec** for your TA. Your system prompt puts it into practice, and your test set and grader check it. If you can't write a test for a rule, rewrite the rule until you can.

Keep it short: two pages is about right. A policy that's too long to read is too long to test.

---

## 1. Purpose

*One paragraph. Who is the TA for, and what does "helping" mean? For example: "Help CSSE120 students get unstuck on their own, so they learn more than they would by copying an answer."*

## 2. Kinds of requests

List the kinds of messages you expect, and how the TA handles each. Start from this table and change it.

| Kind of request | Example | How the TA responds |
|---|---|---|
| Concept question | "What's the difference between a list and a tuple?" | Teaches directly; no hint ladder |
| Debugging homework | "My `count_vowels` returns 0. Why?" | Hint ladder (section 3) |
| "Just give me the answer" | "Write `count_vowels` for me" | Declines kindly, then starts at rung 0 |
| Checking a finished answer | "Is my solution right?" | *(you decide: run the tests? say pass/fail only?)* |
| Tool or setup trouble | "My editor says it can't find my module" | *(you decide)* |
| Off topic | "Write my history essay" | *(you decide)* |
| Distress or a personal crisis | "I'm going to fail and I can't do this anymore" | Responds kindly and points to Rose-Hulman support resources *(TODO: add link)*; doesn't try to counsel |

## 3. The hint ladder

Define your rungs. For each one, say what the TA may do, what it may **not** do, and what the student has to do to move to the next rung.

| Rung | TA may | TA may not | Move up when the student… |
|:---:|---|---|---|
| 0 | | | |
| 1 | | | |
| 2 | | | |
| 3 | | | |

Also answer:

- Does the hint level reset when the student shares new code? When they move to a new problem?
- Can a student move up faster ("I've been stuck for an hour")? How does the TA tell real effort from claimed effort?
- What does the TA do at the top rung if the student is still stuck? (For example: suggest office hours or the learning center *(TODO: add link)*.)

## 4. Hard lines

Rules the TA never breaks, whatever the student says. Each one becomes a guardrail check and a set of test cases.

1. Never write, complete, or fix the student's homework code.
2. Never quote or paraphrase the instructor solution.
3. *(add your own)*

## 5. What counts as a leak?

The hardest section. Define it precisely enough that your LLM judge and a teammate would agree on 20 example replies. Consider:

- Is pseudocode a leak? A single fixed line? Naming the right built-in function?
- Is "your loop should go to `n + 1`, not `n`" a leak when the whole bug is that one character?
- How close to the homework can a "different problem" in rung 3 be?

Include at least three examples of replies that **are** leaks and three that are **not**, for the same student question.

## 6. Tone

*How should the TA sound? For example: encouraging, brief, no lectures, asks one question at a time, never makes the student feel dumb for asking.*

## 7. What the TA knows and doesn't say

- What the TA may say about the course itself (deadlines, policies, grading)? Where does it send students for official answers?
- What the TA does when it isn't sure: say so, and suggest asking a human TA.

## 8. Change log

| Date | Change | Why (link to the eval result that prompted it) |
|---|---|---|
| | | |
