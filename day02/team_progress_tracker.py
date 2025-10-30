#!/usr/bin/env python3
"""
Team Progress Tracker for Day 2: Age Calculator Bot Mission
Monitors team member progress across branches
"""

import subprocess
import os
from datetime import datetime

def get_git_info():
    """Get basic git repository information"""
    try:
        # Get current repository status
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, cwd='/workspaces/ai-track/ai-ace')
        return "Git repository accessible" if result.returncode == 0 else "Git issues detected"
    except:
        return "Git not available"

def check_team_branches():
    """Check status of team member branches"""
    try:
        # Get list of all branches
        result = subprocess.run(['git', 'branch', '-a'], 
                              capture_output=True, text=True, cwd='/workspaces/ai-track/ai-ace')
        
        if result.returncode == 0:
            branches = result.stdout.strip().split('\n')
            team_branches = [b.strip().replace('* ', '').replace('remotes/origin/', '') 
                           for b in branches if 'origin/' in b and 'HEAD' not in b]
            return list(set(team_branches))  # Remove duplicates
        return []
    except:
        return []

def check_day02_files():
    """Check if Day 2 files exist in current branch"""
    day02_path = '/workspaces/ai-track/ai-ace/day02'
    if not os.path.exists(day02_path):
        return "Day 2 folder not found"
    
    files = os.listdir(day02_path)
    essential_files = ['README.md', 'age_calculator_bot.ipynb']
    
    status = {
        'total_files': len(files),
        'has_readme': 'README.md' in files,
        'has_notebook': 'age_calculator_bot.ipynb' in files,
        'files': files
    }
    
    return status

def main():
    print("🤖 AI-ACE Team Progress Tracker - Day 2")
    print("=" * 60)
    print(f"📅 Check Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Git status
    print("🔧 Repository Status:")
    git_status = get_git_info()
    print(f"   {git_status}")
    print()
    
    # Team branches
    print("👥 Team Branches:")
    branches = check_team_branches()
    if branches:
        for branch in branches:
            if branch != 'master' and branch != 'main':
                print(f"   📂 {branch}")
    else:
        print("   ⚠️  No team branches found")
    print(f"   📊 Total team branches: {len([b for b in branches if b not in ['master', 'main']])}")
    print()
    
    # Current branch Day 2 status
    print("📁 Current Branch (aiegoo-lead) Day 2 Status:")
    day02_status = check_day02_files()
    if isinstance(day02_status, dict):
        print(f"   📝 README.md: {'✅' if day02_status['has_readme'] else '❌'}")
        print(f"   📓 age_calculator_bot.ipynb: {'✅' if day02_status['has_notebook'] else '❌'}")
        print(f"   📊 Total files: {day02_status['total_files']}")
        print("   📄 Files in day02/:")
        for file in day02_status['files']:
            print(f"      • {file}")
    else:
        print(f"   ⚠️  {day02_status}")
    print()
    
    # Mission readiness
    print("🎯 Mission Readiness Check:")
    if isinstance(day02_status, dict):
        readiness = day02_status['has_readme'] and day02_status['has_notebook']
        print(f"   🚀 Ready for Day 2 Mission: {'✅ YES' if readiness else '❌ NO'}")
    else:
        print("   🚀 Ready for Day 2 Mission: ❌ NO (missing files)")
    print()
    
    # Next steps
    print("📋 Recommended Actions:")
    if isinstance(day02_status, dict) and day02_status['has_readme'] and day02_status['has_notebook']:
        print("   1. ✅ All essential files present")
        print("   2. 🚀 Ready to support team members")
        print("   3. 📊 Monitor team progress throughout day")
        print("   4. 🤝 Provide guidance on Python fundamentals")
    else:
        print("   1. ⚠️  Ensure all Day 2 files are in place")
        print("   2. 📝 Check README.md exists")
        print("   3. 📓 Verify age_calculator_bot.ipynb is available")
        print("   4. 🔄 Run this tracker again after setup")
    print()
    
    print("🎉 Team Leadership Tips for Today:")
    print("   • Help with input() function usage")
    print("   • Explain str() and int() conversion")
    print("   • Demonstrate string concatenation")
    print("   • Encourage experimentation")
    print("   • Celebrate small victories!")
    print()
    print("Happy teaching! 🌟")

if __name__ == "__main__":
    main()