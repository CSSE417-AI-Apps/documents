# GitHub Setup: Making a New Repo

Do this **every time your team starts a project**. One person on the team creates the repo; everyone helps check it. It takes about 10 minutes.

1. [Pick the repo name](#1-pick-the-repo-name)
2. [Create the repo in the org](#2-create-the-repo-in-the-org)
3. [Add your teammates](#3-add-your-teammates)
4. [Protect `main`](#4-protect-main)
5. [Clone it and add a CLAUDE.md](#5-clone-it-and-add-a-claudemd)

Before this, finish [joining the course org](GitHub_Org_Setup.md).

---

## 1. Pick the repo name

Every repo uses the same naming pattern:

```text
<project-name>-team<NN>
```

- `<project-name>` comes from the project instructions. For example, Project 0 uses `git-workflow` and Project 1 uses `podcast-agent`.
- `<NN>` is your **two-digit team number**. For your first project, look at the [org's repos](https://github.com/CSSE417-AI-Apps?q=git-workflow) and take the **lowest number no other team has used yet**. Keep that number all term if your team stays together. If teams change, pick a new unused number.
- Use lowercase and hyphens only.

Examples: `git-workflow-team03`, `podcast-agent-team03`.

## 2. Create the repo in the org

1. Go to [github.com/organizations/CSSE417-AI-Apps/repositories/new](https://github.com/organizations/CSSE417-AI-Apps/repositories/new).
2. **Owner:** CSSE417-AI-Apps (not your personal account).
3. **Repository name:** the name from step 1.
4. **Visibility:** **Public**.
5. Check **Add a README file**. The repo needs a first commit on `main` before you can protect `main`.
6. **Add .gitignore:** pick the template for your language (for example, **Python**), if the project instructions name one.
7. Click **Create repository**.

## 3. Add your teammates

The person who created the repo is its admin. Add everyone else:

1. On the repo page: **Settings → Collaborators and teams → Add people**.
2. Add each teammate by GitHub username with the **Write** role.
3. Each teammate accepts the invitation from their email, or from the repo page.

## 4. Protect `main`

This turns the course rule "every change to `main` goes through an approved PR" into something GitHub enforces.

1. On the repo page: **Settings → Rules → Rulesets → New ruleset → New branch ruleset**.
2. **Ruleset name:** `protect main`.
3. **Enforcement status:** **Active**.
4. **Bypass list:** leave it **empty**. Nobody, not even an admin, skips review.
5. **Target branches:** **Add target → Include default branch**.
6. Under **Rules**, make sure these are checked:
   - **Restrict deletions**
   - **Block force pushes**
   - **Require a pull request before merging**. Expand it and set:
     - **Required approvals:** `1`
     - Check **Dismiss stale pull request approvals when new commits are pushed**
     - Check **Require conversation resolution before merging**
7. Click **Create**.

To check it worked, look for `protect main` with status **Active** under **Settings → Rules → Rulesets**. In [Project 0](../Labs/Project_0_Git_Workflow.md) you'll prove it by trying to push straight to `main` and watching GitHub refuse.

## 5. Clone it and add a CLAUDE.md

Everyone on the team:

1. In GitHub Desktop: **File → Clone repository → GitHub.com**, then pick your new repo.
2. **Repository → Open in Visual Studio Code**.

One person, on a branch (see the [PR workflow](GitHub_PR_Workflow.md)), adds a `CLAUDE.md` at the top of the repo with the course git rules. Start with this and add project details below it as you go:

```markdown
# <repo name>

<One or two sentences on what this project is.>

## Git rules (CSSE 417)

- Never run `git commit` or `git push`, and never create, approve or merge pull requests. The humans on this team do those in GitHub Desktop and on github.com.
- Read-only git commands (`status`, `diff`, `log`, `fetch`) are fine.
- You may resolve merge conflicts by editing the conflicted files. If you start a merge yourself, use `git merge --no-commit` so a human makes the merge commit.
- When asked to review a pull request, write the review comments in chat for a human to edit and post. Do not post them.
```

That `CLAUDE.md` change is your team's first pull request.
