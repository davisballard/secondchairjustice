# How to Push Second Chair to GitHub

## Quick Command

```bash
push secondchair
```

## If the alias doesn't work

Your terminal needs to load the alias. Do ONE of these:

### Option 1: Open a fresh terminal window
Just open a new terminal - it will automatically load the alias.

### Option 2: Refresh your current terminal
```bash
source ~/.zshrc
```

Then try again:
```bash
push secondchair
```

## What the script does

1. ✅ Syncs your Second_Chair folder to `~/secondchair-repo/`
2. ✅ Excludes: `.venv`, `.env`, `__pycache__`, `.pyc` files
3. ✅ Commits with timestamp
4. ✅ Force pushes to: https://github.com/davisballard/secondchairjustice.git
5. ✅ Takes 5-20 minutes depending on file changes

## Troubleshooting

**"command not found: push"**
→ Run `source ~/.zshrc` or open a new terminal

**GitHub blocks the push (secrets detected)**
→ The `.env` file is already excluded, but if you added new secrets, let Claude know

**Takes too long**
→ Large audio/image files take time to upload. First push may take longer depending on folder size.

---

*Script location: `Agency_Simulation_Root/06_Brands/Second_Chair/push-secondchair.sh`*
