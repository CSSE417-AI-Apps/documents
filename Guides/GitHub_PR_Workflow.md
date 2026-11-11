# The Pull Request Workflow

This is the loop you'll use for every change in every project, all term:

```text
branch → code (with Claude) → commit → push → PR → teammate review → merge → sync
```

1. [Start a branch](#1-start-a-branch)
2. [Write code, then commit](#2-write-code-then-commit)
3. [Push and open a PR](#3-push-and-open-a-pr)
4. [Review a teammate's PR](#4-review-a-teammates-pr)
5. [Respond to review, then merge](#5-respond-to-review-then-merge)
6. [Sync and clean up](#6-sync-and-clean-up)
7. [Merge conflicts](#7-merge-conflicts)

Before this, set up your repo with [Making a new repo](GitHub_New_Repo.md).

**Who does what:**

| Step | Who | Where |
|---|---|---|
| Branch, commit, push | You | GitHub Desktop |
| Write and fix code, explain diffs, resolve conflicts | Claude Code (you check its work) | VS Code |
| Open a PR | You | GitHub Desktop → github.com |
| Draft review comments | Claude Code, through the [GitHub MCP](GitHub_MCP_Setup.md) | VS Code |
| Edit and post review comments, approve | Your teammate | github.com |
| Merge | The PR's author, after approval | github.com |

---

## 1. Start a branch

1. In GitHub Desktop, click **Fetch origin**. If it changes to **Pull origin**, click that too, so you start from the latest `main`.
2. **Current Branch → New Branch**. Base it on `main`.
3. Give it a short name that says what it's for: `add-transcript-loader`, `fix-search-crash`.

One branch for each change. Small PRs get better reviews than big ones.

## 2. Write code, then commit

1. Work with Claude Code in VS Code as usual.
2. In GitHub Desktop, read **every changed line** in the **Changes** tab. If you can't explain a change, ask Claude about it, or undo it.
3. Write a commit summary that says what changed ("Load transcripts from GCS bucket"), then click **Commit to `<branch>`**.

Commit as often as you like. Each commit is a save point.

## 3. Push and open a PR

1. Click **Publish branch** (the first time) or **Push origin**.
2. Click **Create Pull Request** (or **Branch → Create Pull Request**). Your browser opens on github.com.
3. Check that the PR merges **into `main`**, then write a description:
   - **What** changed, and **why**
   - **How to test it:** what your reviewer should run or click
   - Anything you're unsure about, so your reviewer knows where to look hardest

   Claude can draft this for you: `Summarize the changes on this branch compared to main, for a PR description.` Edit what it writes before you paste it.
4. Under **Reviewers**, request a review from a teammate, then click **Create pull request**.

## 4. Review a teammate's PR

Reviewing is a real job, not a rubber stamp. **Your approval is your name on the code.**

1. Read the PR description and the **Files changed** tab on github.com.
2. Ask Claude for help. It reads the PR through the [GitHub MCP](GitHub_MCP_Setup.md):

   ```text
   Use the GitHub MCP to review PR #7 in CSSE417-AI-Apps/podcast-agent-team03.
   Summarize what it changes, then draft review comments: bugs, missing error
   handling, unclear names, missing tests, and questions I should ask the author.
   For each comment, give the file and line. Don't post anything.
   ```

3. To run the code, check out the branch in GitHub Desktop (**Current Branch** → pick it) and try it.
4. Decide which of Claude's comments you agree with. Rewrite them in your own words and add your own. Claude misses things and sometimes flags problems that aren't real.
5. On github.com, click a line in **Files changed** to comment on it. When you're done, click **Review changes** and choose:
   - **Request changes** if something needs fixing before merge
   - **Comment** if you only have questions or suggestions
   - **Approve** if you've read it, understand it, and would be happy to maintain it

## 5. Respond to review, then merge

1. Reply to every comment. Fix the code (Claude can help: paste in the comment), then commit and push to the **same branch**. The PR updates by itself.
2. New pushes **dismiss earlier approvals**, so ask your reviewer to look again.
3. When the PR is approved and every conversation is resolved, the **author** clicks **Merge pull request** on github.com, then **Delete branch**.

## 6. Sync and clean up

1. In GitHub Desktop, switch to `main` and click **Fetch origin**, then **Pull origin**.
2. Delete your old local branch: **Branch → Delete**.
3. Start your next change with a fresh branch from step 1.

## 7. Merge conflicts

A conflict happens when your branch and `main` both changed the same lines. GitHub won't merge the PR until you fix it. Fix it on **your branch**, on your laptop:

1. In GitHub Desktop, on your branch, click **Fetch origin**.
2. **Branch → Update from main**. If there's a conflict, Desktop lists the conflicted files.
3. Leave that dialog open. In VS Code, ask Claude:

   ```text
   I'm merging main into my branch and have conflicts. Resolve the conflict
   markers in the conflicted files, keeping both sides' intent. Explain each
   choice. Don't commit.
   ```

4. Read Claude's changes. Make sure the code still runs.
5. Back in GitHub Desktop, the files show as resolved. Click **Continue merge** to make the merge commit, then **Push origin**. The PR on github.com updates.

Because you pushed, your reviewer needs to approve again.
