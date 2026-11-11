# Claude Pro Setup

In CSSE 417 we all use the same AI coding assistant, **Claude Code**, inside VS Code. This guide walks you through:

1. [Signing up for Claude Pro](#1-sign-up-for-claude-pro)
2. [Installing the Claude Code extension in VS Code](#2-install-the-claude-code-extension)
3. [Signing in](#3-sign-in)
4. [Learning to use Claude in VS Code](#4-learning-to-use-claude-in-vs-code)
5. [Practice: explore this course repo with Claude](#5-practice-explore-this-course-repo-with-claude)

**Finish this before Day 2 (Tuesday, Dec 1).**

---

## Why everyone uses Claude Pro

A large part of this course is learning to build software *with* an AI agent, not just learning to build AI software. When everyone uses the same tool:

- Instructions, demos and in-class examples work the same on every laptop.
- We can share tips, prompts, project rules files (`CLAUDE.md`) and skills that work for everyone.
- Dr. Fisher builds the course materials with this same setup, so what you see in class is what you'll use.

### Cost

- **Claude Pro costs $20/month** if you pay monthly.
- Choose **monthly**, not annual. The annual plan is cheaper per month ($17) but bills $200 up front for the year.
- You need it for the length of the term (Nov 30 – Feb 25), about 3 months or **roughly $60 total**. You can cancel after the term, or keep it if you find it useful.
- If the cost is a hardship, please talk to Dr. Fisher privately.

---

## 1. Sign up for Claude Pro

1. Go to [claude.ai](https://claude.ai) and create an account, or log in if you already have one.
   - Use an email you'll keep. Your Rose-Hulman email is fine, but a personal email keeps working after you graduate.
2. Open the plan options at [claude.com/pricing](https://claude.com/pricing) (or **Settings → Billing** in claude.ai) and choose **Pro**.
3. Select **monthly** billing and complete the checkout.
4. Confirm your plan shows **Pro** under **Settings → Billing**.

> Already on Claude Max? That also works. A free account does **not** include Claude Code.

---

## 2. Install the Claude Code extension

You need VS Code **1.94 or newer**. Check under **Code → About Visual Studio Code** (Mac) or **Help → About** (Windows).

1. Open VS Code.
2. Open the Extensions view: `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows/Linux).
3. Search for **Claude Code**.
4. Install the one published by **Anthropic** (ID: `anthropic.claude-code`). There are lookalike extensions, so check the publisher.
5. If it doesn't appear after installing, open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`) and run **Developer: Reload Window**.

---

## 3. Sign in

1. Open Claude Code using any of these:
   - The **✻ Claude Code** item in the bottom-right status bar (works even with no file open)
   - The **spark icon** in the top-right of the editor (appears when a file is open)
   - The **spark icon** in the left Activity Bar
2. Click **Sign in** on the first-run screen.
3. Your browser opens. Log in to the Claude account you set up with Pro and approve the connection.
4. Go back to VS Code. You should see a prompt box ready for your first message.

You **don't** need an API key. Your Pro subscription covers Claude Code.

If you see **"Not logged in · Please run /login"**, the sign-in screen should reopen on its own. If it doesn't, run **Developer: Reload Window**.

---

## 4. Learning to use Claude in VS Code

### The basics

- **Open a folder, not just a file.** Claude works on the folder (project) you have open in VS Code, and it can read, search and edit files in it.
- **Type your request in plain English** and press Enter. Use `Shift+Enter` for a new line.
- **Claude sees what you select.** Highlight some code in the editor and the prompt box shows how many lines are selected. Ask "what does this do?" and Claude knows what "this" is.
- **Switch between the editor and Claude** with `Cmd+Esc` (Mac) or `Ctrl+Esc` (Windows/Linux).

### Point Claude at files with `@`

Type `@` followed by a file or folder name to hand Claude that content:

```text
Explain the logic in @app.py
What's in @Labs/ ?
Why does @app.py#20-35 crash when the list is empty?
```

- `Option+K` (Mac) / `Alt+K` (Windows/Linux) inserts an `@` reference to your current selection, line numbers included.
- `@terminal:<name>` gives Claude a terminal's output, so you don't have to copy and paste error messages.
- You can paste screenshots straight into the prompt box.

### Permission modes: how much Claude does on its own

The mode shows at the bottom of the prompt box. Click it to change it.

| Mode | What happens | When to use it |
|---|---|---|
| **Manual** | Claude asks before editing files and before most commands. Edits appear as a diff you **accept** or **reject**. | When you're learning, or in code you care about. **Start here.** |
| **Plan** | Claude describes what it will do and waits for your approval before changing anything. Type `/plan` to switch. | Bigger changes, where you want to agree on the approach first |
| **Edit automatically** | Claude edits files without asking. | Small, low-risk tasks you'll review afterward |
| **Auto** | A safety classifier approves most actions so Claude can keep working. | When you're comfortable and checking results with tests or git |

> **You are responsible for code you submit.** Read the diffs. If you can't explain a change, ask Claude to explain it, or reject it.

### Slash commands

Type `/` in the prompt box to see the commands. Useful ones:

- `/init`: Claude reads your project and writes a `CLAUDE.md` file describing it (see below).
- `/usage`: see how much of your Pro usage limit you've used.
- `/model`: switch which Claude model you're using.
- `/btw`: ask a quick side question without adding it to the conversation.

### `CLAUDE.md`: give Claude standing instructions

A `CLAUDE.md` file at the top of a project is read at the start of every conversation. It's where you record what the project is, how it's organized, and the rules to follow. This course's documents repo has one, and every project you build this term should too. We'll spend real class time on writing good ones.

### Skills: reusable procedures

A **skill** is a set of instructions for a task you do over and over, saved in `.claude/skills/<name>/SKILL.md`. You run one by typing `/<name>`, and Claude can also use it on its own when your request matches. For example, this repo has a `/calendar-edit` skill that Dr. Fisher uses to update the course calendar.

### Undo and history

- **Rewind:** hover over any of your earlier messages and choose **Rewind code to here** to undo Claude's changes after that point.
- **Fork:** **Fork conversation from here** tries a different direction without losing the original.
- **Session history:** the history button at the top of the Claude panel lets you resume past conversations.
- **Use git anyway.** Commit before asking for big changes, so `git diff` shows exactly what Claude did.

### Usage limits

Pro has usage limits that reset every few hours. To make them last:

- Start a **new conversation** for each new task. Long conversations use more of your limit.
- Be specific: point at files with `@` instead of saying "look through everything."
- Check `/usage` if you're about to start a big task.

---

## 5. Practice: explore this course repo with Claude

1. Clone this repo and open it in VS Code:

   ```bash
   git clone https://github.com/CSSE417-AI-Apps/documents.git
   code documents
   ```

2. Open Claude Code and make sure you're in **Manual** mode.
3. Try these prompts:
   - `What is this repo for? Read @CLAUDE.md`
   - `Using @README.md, how many class meetings are there, and which days have no class?`
   - `What do I need to do for Project 1? @Labs/Project_1_Podcast_Agent.md`
   - Select a few rows of the calendar table in `README.md` and ask: `Explain the Markdown syntax in my selection.`
4. Ask Claude to make a small change, such as `Add my name to the end of README.md`. Look at the diff, then **reject** it. (Don't push changes to the course repo. This is just practice.)

You're done when Claude answers questions about the repo and you've seen an edit diff.

---

*(TODO: add screenshots)*
