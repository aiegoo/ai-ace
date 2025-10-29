# 🎯 AI-ACE Team Member Onboarding Guide

## Welcome to the AI-ACE Team! 🚀

This guide will help you get started with our collaborative learning environment.

## 📋 Prerequisites

### You Need:
- [ ] GitHub account (free)
- [ ] Git installed on your computer
- [ ] Basic terminal/command prompt access
- [ ] Your assigned branch name (given by team lead)

### Don't Worry If You're New To:
- Git/GitHub (we'll learn together!)
- Programming (everyone starts somewhere!)
- Command line (we'll show you the basics!)

## 🚀 Getting Started (Step by Step)

### Step 1: Clone the Repository
```bash
# Open terminal/command prompt and run:
git clone git@github.com:aiegoo/ai-ace.git

# Go into the project folder:
cd ai-ace
```

### Step 2: Switch to Your Branch
```bash
# Replace [YOUR-BRANCH-NAME] with the branch name assigned to you
git checkout [YOUR-BRANCH-NAME]

# Check that you're on the right branch:
git branch
# You should see a * next to your branch name
```

### Step 3: Start Your First Day
```bash
# Go to your day01 folder:
cd day01

# Create your first file (try this!):
echo "# My First Day in AI-ACE!" > my_notes.md
```

### Step 4: Save Your Work
```bash
# Add your changes:
git add .

# Save with a message:
git commit -m "Day 1: Added my first notes!"

# Upload to GitHub:
git push origin [YOUR-BRANCH-NAME]
```

## 📚 Daily Workflow

### Every Day, Follow These Steps:

1. **Start Your Session:**
   ```bash
   cd ai-ace
   git checkout [YOUR-BRANCH-NAME]
   git pull origin [YOUR-BRANCH-NAME]
   ```

2. **Do Your Work:**
   - Create files for daily challenges
   - Experiment with code
   - Take notes in markdown files
   - Ask questions in your daily log

3. **Save Your Progress:**
   ```bash
   git add .
   git commit -m "Day X: [what you accomplished]"
   git push origin [YOUR-BRANCH-NAME]
   ```

## 🔧 Essential Commands

### Check Your Status:
```bash
git status          # See what files changed
git branch          # See which branch you're on
git log --oneline   # See your recent work
```

### Safe Commands (These Won't Break Anything):
```bash
git status          # Always safe to check
git branch          # Always safe to check
git log             # Always safe to check
git diff            # See what changed
```

### Daily Commands:
```bash
git add .                               # Stage your changes
git commit -m "Your message here"       # Save your changes
git push origin [YOUR-BRANCH-NAME]      # Upload to GitHub
```

## 📁 Your Workspace Structure

Your branch will look like this:
```
ai-ace/
├── DAILY_LOG_[your-name].md    # Your personal learning log
├── day01/                      # Day 1 work
│   ├── README.md
│   └── [your files here]
├── day02/                      # Day 2 work (created as needed)
├── day03/                      # Day 3 work (created as needed)
└── ... etc
```

## 🆘 Getting Help

### If Something Goes Wrong:
1. **Don't panic!** Git is designed to be safe
2. Ask on our team chat/discussion
3. Share the error message you see
4. We'll help you fix it together!

### Common Issues:

**"I'm on the wrong branch"**
```bash
git checkout [YOUR-BRANCH-NAME]
```

**"I made changes to the wrong files"**
```bash
git status           # See what changed
git checkout .       # Undo all changes (if you want to start over)
```

**"I don't know what I did"**
```bash
git log --oneline    # See your recent commits
git status           # See current state
```

## 🎯 Learning Objectives

### Week 1 Goals:
- [ ] Successfully clone and access your branch
- [ ] Create your first files and commit them
- [ ] Complete Day 1 ASCII art challenge
- [ ] Ask at least one question to the team
- [ ] Help another team member with something

### By End of Month:
- [ ] Comfortable with basic Git commands
- [ ] Regular daily commits to your branch
- [ ] Contributing to team discussions
- [ ] Sharing your learning progress

## 🤝 Team Collaboration Rules

### Do's:
- ✅ Work in your own branch
- ✅ Commit your work daily
- ✅ Ask questions freely
- ✅ Share interesting discoveries
- ✅ Help teammates when you can
- ✅ Celebrate each other's progress

### Don'ts:
- ❌ Don't work in the master branch
- ❌ Don't be afraid to make mistakes
- ❌ Don't hesitate to ask for help
- ❌ Don't compare your progress to others
- ❌ Don't give up when things get challenging

## 🎉 You're Ready!

Remember: **Everyone starts as a beginner!** The goal is to learn together, support each other, and have fun while building awesome AI projects.

Your journey starts now! 🚀

---

**Questions?** Ask your team lead or post in our discussion area!
**Stuck?** Share your screen in our next team call!
**Excited?** Start with Day 1 and let's see what you create! 🎨