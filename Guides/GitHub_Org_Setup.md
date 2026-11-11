# GitHub Setup: Join the Course Org

Every line of code you write in CSSE 417 lives in a git repo in the course's GitHub organization, [CSSE417-AI-Apps](https://github.com/CSSE417-AI-Apps). This guide gets you into the org and sets up the tools you'll use all term.

1. [Create or check your GitHub account](#1-create-or-check-your-github-account)
2. [Keep your email private](#2-keep-your-email-private)
3. [Join the CSSE417-AI-Apps org](#3-join-the-csse417-ai-apps-org)
4. [Install GitHub Desktop](#4-install-github-desktop)
5. [Clone the course documents repo](#5-clone-the-course-documents-repo)

Next guides:
- [Making a new repo](GitHub_New_Repo.md): what to do every time your team starts a project
- [GitHub MCP setup](GitHub_MCP_Setup.md): let Claude Code read PRs and issues
- [The pull request workflow](GitHub_PR_Workflow.md): the branch → PR → review → merge loop you'll use all term

---

## The course rules for git

These rules apply to every project, all term:

1. **All code goes in a git repo in the CSSE417-AI-Apps org.** No personal repos, and no code that lives only on your laptop.
2. **All repos are public.**
3. **Nothing goes into `main` without a pull request (PR) that a teammate approves.** You can't approve your own PR.
4. **Humans commit, push and create PRs, using GitHub Desktop.** Claude Code writes and fixes code, explains diffs, resolves merge conflicts and drafts review comments. Claude Code does **not** commit, push, or create, approve or merge PRs.

Why: code review is one of the most important habits a software engineer has, and it matters more when an AI writes much of the code. Your approval says "I read this and I vouch for it."

---

## 1. Create or check your GitHub account

- If you already have a GitHub account, use it. Your username will appear on public repos, so pick a professional one.
- If you don't have one, sign up at [github.com/signup](https://github.com/signup). A personal email keeps working after you graduate. You can add your Rose-Hulman email as a second address.
- Turn on two-factor authentication: **Settings → Password and authentication**.

## 2. Keep your email private

All course repos are public, and every commit records an email address. Use GitHub's private "noreply" address in commits:

1. Go to **Settings → Emails** on github.com.
2. Check **Keep my email addresses private**.
3. Copy the address shown there. It looks like `12345678+username@users.noreply.github.com`. You'll use it in [step 4](#4-install-github-desktop).
4. Also check **Block command line pushes that expose my email**.

## 3. Join the CSSE417-AI-Apps org

1. Go to Moodle and add your GitHub username to the team sign-up spreadsheet.
2. You'll get an email invitation from GitHub. Accept it, or go to [github.com/orgs/CSSE417-AI-Apps/invitation](https://github.com/orgs/CSSE417-AI-Apps/invitation) while signed in.
3. Check that you can see the org's repos at [github.com/CSSE417-AI-Apps](https://github.com/CSSE417-AI-Apps).

## 4. Install GitHub Desktop

1. Download and install GitHub Desktop from [desktop.github.com](https://desktop.github.com).
2. Sign in to GitHub.com:
   - Mac: **GitHub Desktop → Settings → Accounts**
   - Windows: **File → Options → Accounts**
3. Set your commit identity under **Settings/Options → Git**:
   - **Name:** your real name, or your GitHub username
   - **Email:** choose the `@users.noreply.github.com` address from [step 2](#2-keep-your-email-private)
4. Set VS Code as your editor under **Settings/Options → Integrations → External Editor**. Then **Repository → Open in Visual Studio Code** opens the repo where Claude Code can work on it.

> **Why GitHub Desktop and not Claude?** Committing is the moment you decide "this change is ready." Desktop shows you every changed line before you commit. Make that a habit.

## 5. Clone the course documents repo

1. In GitHub Desktop: **File → Clone repository → GitHub.com**.
2. Pick **CSSE417-AI-Apps/documents** and choose where to save it.
3. Click **Clone**, then **Repository → Open in Visual Studio Code**.

To get Dr. Fisher's latest updates later, click **Fetch origin**, then **Pull origin**.

You're done when you're a member of the org, GitHub Desktop is signed in and uses your noreply email, and the documents repo is cloned.
