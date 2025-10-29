# AI-ACE Repository Branch Protection Setup 🛡️

## Setting up Branch Protection for Team Safety

Since your team members are new to Git/GitHub, protecting the master branch is crucial to prevent accidental overwrites.

### Step 1: Go to GitHub Repository Settings

1. Navigate to: `https://github.com/aiegoo/ai-ace`
2. Click on **Settings** tab (top right)
3. Click on **Branches** in the left sidebar

### Step 2: Add Branch Protection Rule

1. Click **Add rule** button
2. Enter branch name pattern: `master` or `main`
3. Enable these protection settings:

#### Recommended Settings for New Teams:
- ✅ **Require pull request reviews before merging**
  - Required approving reviews: 1
  - ✅ Dismiss stale PR reviews when new commits are pushed
  - ✅ Require review from code owners (if you have CODEOWNERS file)

- ✅ **Require status checks to pass before merging**
  - This prevents broken code from being merged

- ✅ **Require branches to be up to date before merging**
  - Ensures no conflicts with latest changes

- ✅ **Require conversation resolution before merging**
  - All review comments must be resolved

- ✅ **Restrict pushes that create files that contain secrets**
  - Prevents accidental API key commits

- ✅ **Do not allow bypassing the above settings**
  - Even admins must follow rules (recommended for learning)

- ❌ **Allow force pushes** (Keep disabled for safety)
- ❌ **Allow deletions** (Keep disabled for safety)

### Step 3: Create CODEOWNERS File (Optional)

Create `.github/CODEOWNERS` in your repository:

```
# Global code owners (you as the team lead)
* @aiegoo

# Specific folder owners (optional)
/team-projects/ @aiegoo
/shared-resources/ @aiegoo
```

## Team Member Workflow After Setup

### Initial Setup (One Time):
```bash
# Clone the repository
git clone git@github.com:aiegoo/ai-ace.git
cd ai-ace

# Switch to their personal branch
git checkout [their-branch-name]
```

### Daily Workflow:
```bash
# Always start by switching to their branch
git checkout [their-branch-name]

# Pull latest changes (good practice)
git pull origin [their-branch-name]

# Do their work...
# Create files, folders, etc.

# Save their work
git add .
git commit -m "Day X: Completed [task description]"
git push origin [their-branch-name]
```

### When They Need to Share Work:
1. Push their work to their branch (as above)
2. Create a Pull Request on GitHub:
   - From: `[their-branch]`
   - To: `master`
3. You review and merge when ready

## Benefits of This Setup:

### For New Team Members:
- ✅ Safe to experiment in their own branch
- ✅ Can't accidentally break the main codebase
- ✅ Learn proper Git workflow gradually
- ✅ Clear separation of individual work

### For Team Lead (You):
- ✅ Control over what goes into master
- ✅ Review all contributions before merging
- ✅ Teach best practices through PR reviews
- ✅ Maintain code quality standards

## Emergency Recovery:

If someone accidentally messes up their branch:
```bash
# Delete their local branch and start fresh
git branch -D [their-branch-name]
git checkout master
git pull origin master
git checkout -b [their-branch-name] origin/[their-branch-name]
```

## Team Training Commands:

Share these safe commands with new team members:
```bash
# Check current branch (always good to know where you are)
git branch

# See what files have changed
git status

# See what changes were made
git diff

# Save work safely
git add .
git commit -m "Description of what I did"
git push origin [my-branch-name]
```

This setup ensures a safe learning environment while teaching proper collaborative development practices! 🎉