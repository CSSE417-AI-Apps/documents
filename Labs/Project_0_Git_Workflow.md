# Project 0: Git Workflow

> **DRAFT.** These instructions are still being written.

## Overview

Before you build AI systems as a team, you need a team workflow that works. In this short project your team of 3 sets up a repo in the course org, protects `main`, and practices the full loop: branch, commit, pull request, code review, merge, plus one merge conflict on purpose.

You'll also start on Project 1: each of you proposes podcasts your team could build the [Podcast Agent](Project_1_Podcast_Agent.md) around.

**Team size:** 3. Sign up your team in the team sign-up spreadsheet on Moodle.

**Repo name:** `git-workflow-team<NN>` (see [picking the repo name](../Guides/GitHub_New_Repo.md#1-pick-the-repo-name)).

**Assigned:** Day 1 (Monday, Nov 30). **Due:** Day 3 (Thursday, Dec 3).

## Learning objectives

- Set up a protected GitHub repo where every change to `main` needs an approved pull request
- Use GitHub Desktop to branch, commit, push and open pull requests
- Review a teammate's code with help from Claude Code and the GitHub MCP, and write review comments in your own words
- Resolve a merge conflict with Claude Code's help

---

## Part 1: Individual setup (everyone)

1. [Join the course org](../Guides/GitHub_Org_Setup.md) and install GitHub Desktop.
2. [Set up the GitHub MCP](../Guides/GitHub_MCP_Setup.md) in Claude Code.

## Part 2: Create the team repo (one person, everyone watches)

Follow [Making a new repo](../Guides/GitHub_New_Repo.md) to create `git-workflow-team<NN>`: public, with a README, all three teammates added, and the `protect main` ruleset on.

Then **everyone** clones it in GitHub Desktop.

## Part 3: Prove `main` is protected (everyone)

1. In GitHub Desktop, **on `main`**, make a small edit to `README.md` and commit it to `main`.
2. Click **Push origin**. GitHub should **reject** the push, because `main` requires a pull request.
3. Take a screenshot of the error for your team's README (see Part 6).
4. Undo your local commit: **History** tab → right-click the commit → **Undo Commit**. Then discard the change.

If the push **succeeds**, your ruleset isn't working. Go back to [Protect `main`](../Guides/GitHub_New_Repo.md#4-protect-main) and fix it.

## Part 4: Your first PRs (everyone)

Follow [the PR workflow](../Guides/GitHub_PR_Workflow.md) for each of these.

### 4a. Add the CLAUDE.md (one person)

Add the `CLAUDE.md` from [Making a new repo](../Guides/GitHub_New_Repo.md#5-clone-it-and-add-a-claudemd) on a branch, open a PR, and have a teammate review and approve it before it's merged.

### 4b. Podcast proposals (each person)

Each of you, on your own branch:

1. Create `podcasts/<your-github-username>.md` with **2 podcasts** your team could use for Project 1. For each, give:
   - The name and a link
   - Why it would make an interesting Podcast Agent
   - Where transcripts could come from (published transcripts, YouTube captions, or audio you'd transcribe yourself)

   Use Claude to research, but check its claims: make sure the podcast exists and the transcript source is real.
2. Commit, push and open a PR.
3. **Review rotation:** each person reviews the next person's PR (A reviews B, B reviews C, C reviews A).
4. Reviewers: use Claude and the GitHub MCP to draft comments, as in [Review a teammate's PR](../Guides/GitHub_PR_Workflow.md#4-review-a-teammates-pr). Then post **at least two comments in your own words**. Request at least one change.
5. Authors: reply to each comment, push a fix, get re-approved, and merge.

## Part 5: A merge conflict on purpose (everyone)

1. Add a `## Our pick for Project 1` section to `README.md` through a PR, with one placeholder line: `TBD`. Merge it.
2. **Two** teammates each make a branch from that `main` and replace the `TBD` line with a *different* podcast choice. Both open PRs.
3. Review and merge the first PR.
4. The second PR now has a conflict. Its author resolves it with Claude, following [Merge conflicts](../Guides/GitHub_PR_Workflow.md#7-merge-conflicts). Make the resolved text show the team's real final pick, then push, get re-approved, and merge.

## Part 6: Wrap up (one person, through a PR)

Update `README.md` so it contains:

- Your team number. Use GitHub usernames, not real names; the repo is public.
- The screenshot from Part 3, in an `images/` folder
- A list of your merged PR links, with the author and the reviewer of each
- 2-3 sentences: what did Claude's review drafts catch, and what did they miss or get wrong?

## Deliverables

Submit your repo URL *(TODO: add link)*. By the due date, your repo should have:

- [ ] The `protect main` ruleset, active, with an empty bypass list
- [ ] A `CLAUDE.md` with the course git rules, merged through a PR
- [ ] One `podcasts/<username>.md` PR per teammate, each approved by a different teammate, each with at least two review comments and a follow-up fix
- [ ] A PR with a resolved merge conflict
- [ ] The wrap-up README from Part 6
- [ ] No commits pushed straight to `main`. Every change arrived through a merged PR.

## Grading

- *(TODO)*
