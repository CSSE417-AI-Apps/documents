# GitHub Setup: The GitHub MCP for Claude Code

**MCP** (Model Context Protocol) is how you give an AI agent new tools. The GitHub MCP server lets Claude Code read GitHub directly: pull requests and their diffs, review comments, issues and CI results. Without it, Claude only sees the files on your laptop.

In this course you'll mostly use it to **help you review your teammates' pull requests**.

1. [Install the Claude Code command line](#1-install-the-claude-code-command-line)
2. [Create a read-only GitHub token](#2-create-a-read-only-github-token)
3. [Add the GitHub MCP server](#3-add-the-github-mcp-server)
4. [Check that it works](#4-check-that-it-works)

Before this, finish [Claude Pro setup](Claude_Pro_Setup.md) and [joining the course org](GitHub_Org_Setup.md).

---

## Why read-only?

The course rule is that **humans** create, review, approve and merge PRs. Claude can read anything and draft review comments, but you edit and post them yourself. We'll make the token read-only, so the MCP couldn't post or merge even if Claude tried.

Read-only also means Dr. Fisher doesn't need to approve anything: a read-only token for public repos works on every course repo right away.

## 1. Install the Claude Code command line

The VS Code extension doesn't add the `claude` command to your terminal, and you need it to add MCP servers. Install it:

- **Mac/Linux** (Terminal):
  ```bash
  curl -fsSL https://claude.ai/install.sh | bash
  ```
- **Windows** (PowerShell):
  ```powershell
  irm https://claude.ai/install.ps1 | iex
  ```

Close and reopen your terminal, then check that `claude --version` prints a version number. It uses the same Claude Pro login as the extension. If it asks, run `claude` once and sign in.

## 2. Create a read-only GitHub token

1. On github.com: **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. **Token name:** `csse417-mcp`.
3. **Expiration:** **Custom**, set to **Mar 1, 2027** (after the term ends).
4. **Resource owner:** your own account.
5. **Repository access:** **Public repositories**. This gives read-only access to every public repo on GitHub, including all course repos.
6. Click **Generate token** and copy it. It starts with `github_pat_`. You won't be able to see it again.

> **Treat the token like a password.** Never paste it into a file in a repo, a chat with a classmate, or a commit. If it leaks, delete it on the same GitHub page and make a new one.

## 3. Add the GitHub MCP server

In a terminal, run this as **one line**, with your token in place of `YOUR_TOKEN`:

```bash
claude mcp add --transport http --scope user github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_TOKEN" --header "X-MCP-Readonly: true"
```

- `--scope user` makes the MCP available in every project on your laptop. It's saved in your home folder, not in any repo.
- `X-MCP-Readonly: true` hides GitHub's write tools from Claude. The token is read-only anyway, so this just keeps Claude from trying.

Run `claude mcp list` to confirm `github` shows as connected.

## 4. Check that it works

1. In VS Code, run **Developer: Reload Window**, then open Claude Code.
2. Type `/mcp` and check that **github** is listed and connected.
3. Try these prompts:
   - `Use the GitHub MCP to list the repos in the CSSE417-AI-Apps org.`
   - `Use the GitHub MCP to show the open pull requests in CSSE417-AI-Apps/<your-repo>.`
   - `Summarize the last 5 commits on main in CSSE417-AI-Apps/documents.`

The first time Claude uses a GitHub tool, it asks permission. Read the request and approve it.

You're done when Claude can list the org's repos through the MCP.

## Using it for code review

See [Reviewing a pull request](GitHub_PR_Workflow.md#4-review-a-teammates-pr) in the PR workflow guide.
