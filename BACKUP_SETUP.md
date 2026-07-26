# Backup Setup Guide

## 1. OneDrive (Primary — do this first)

1. Open OneDrive from your system tray (cloud icon near clock)
2. Sign in with your Microsoft account
3. Click "Browse" and select: `C:\Users\DELL\research`
4. Let it sync — all files now backed up to the cloud

If OneDrive is not signed in: Start > Search "OneDrive" > Sign in

## 2. Git + GitHub (Secondary — version history)

### Step A: Install Git
1. Go to https://git-scm.com/download/win
2. Download and run the installer (leave all defaults)
3. Restart your terminal after installation

### Step B: Create GitHub Account
1. Go to https://github.com/signup
2. Create a free account with your email

### Step C: Set Up Repository
After Git is installed, run these commands in your terminal (in the research folder):

```powershell
git init
git add .
git commit -m "Initial commit — AI Law Research Project"
```

Then create a repo on GitHub (click "+" > "New repository") named `ai-law-research`, don't tick any boxes. Then run:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/ai-law-research.git
git branch -M main
git push -u origin main
```

## 3. How to Save After Each Session

After significant work, run:

```powershell
git add .
git commit -m "Session YYYY-MM-DD: brief description"
git push
```

This saves everything with version history.
