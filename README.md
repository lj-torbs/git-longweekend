# Long Weekend Git Challenge

Four days. One repository. Only the terminal: no IDE Git buttons, no GitHub Desktop, no "Upload files" on the website.

Your commit history is your proof of work. I will read it, so make it honest and readable.

## The rules

1. Work in **your own fork**, cloned to your computer. Never edit files on the GitHub website.
2. Commit **small and often**. A good day has at least 3 commits.
3. Every commit message says what the change does, in present tense ("Add farewell function"). Messages like "update", "fix", "asdf" lose points.
4. Run `git status` before every `git add`, and `git diff` before every `git commit`.
5. Every day: `git fetch upstream`, read what changed, then `git pull upstream main`. New tasks arrive that way. If you do not pull, you will not see them.
6. Push at the end of every day with `git push origin main`.
7. Do not copy a classmate's repository. Conflicts and timestamps make copying easy to spot.

## Day 1: Set up (about 30 minutes)

1. On GitHub, click **Fork** on this repository (keep the name): https://github.com/lj-torbs/git-longweekend
2. Clone **your fork**: `git clone <your-fork-url>`
3. `cd` into it and tell Git how to pull: `git config pull.rebase false`
4. Set your identity if you have not: `git config user.name "Your Name"` and `git config user.email "you@example.com"`
5. Link the instructor's repo: `git remote add upstream https://github.com/lj-torbs/git-longweekend.git` then run `git remote` and check you see `origin` and `upstream`.
6. Open `STUDENT.md` and fill in your details. Run `git status` and `git diff` to see your change before you `git add` it.
7. Commit with a proper message, then `git push origin main`.
8. Open `log/day1.md` and paste the output of your `git status` and `git log --oneline`. Commit and push that too.

Done when: your fork on GitHub shows your name in `STUDENT.md` and at least 2 commits from you.

## Days 2, 3, 4

Each morning I push a new file to `tasks/`. Get it with:

```
git fetch upstream
git diff main upstream/main
git pull upstream main
```

Then open `tasks/dayN.md` and follow it. Do your daily log in `log/dayN.md`.

## Handing in

Submit the URL of your fork. I will check the history, not just the final files.

## Quick reference (all from our lesson)

| Need | Command |
|---|---|
| Where am I? | `git status` |
| What did I change? | `git diff` |
| Stage | `git add file` |
| Save | `git commit -m "message"` |
| History | `git log --oneline` |
| Send mine | `git push origin main` |
| See theirs | `git fetch upstream` |
| Take theirs | `git pull upstream main` |
| Where are my remotes? | `git remote` |

Note: the lesson slides say `master`. This repository uses `main`.
