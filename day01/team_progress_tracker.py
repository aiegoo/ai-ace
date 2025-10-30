#!/usr/bin/env python3
"""
AI-ACE Team Progress Tracker
Team Leader Tool by Tony Lee (@aiegoo)

Monitor team member progress across all branches and missions.
"""

import subprocess
import json
from datetime import datetime

class TeamProgressTracker:
    def __init__(self):
        self.team_members = {
            "changminis": {
                "name": "장수민 (ChangMin)",
                "korean_name": "장수민",
                "branch": "changminis",
                "email": "changminis@naver.com",
                "status": "Active"
            },
            "heozico": {
                "name": "허지호 (Heozico)", 
                "korean_name": "허지호",
                "branch": "heozico",
                "email": "heozico@naver.com",
                "role": "Team Scriber",
                "status": "Active"
            },
            "joonii93-ops": {
                "name": "이상준 (Joonii93)",
                "korean_name": "이상준",
                "branch": "joonii93-ops",
                "email": "joonii93@gmail.com", 
                "role": "Operations Expert",
                "status": "Active"
            },
            "jsmin2080-afk": {
                "name": "정수민 (Jsmin2080)",
                "korean_name": "정수민",
                "branch": "jsmin2080-afk",
                "course": "생성AI 7회차", 
                "status": "Active"
            },
            "weisheit129": {
                "name": "고준 (Weisheit129)",
                "korean_name": "고준",
                "branch": "weisheit129",
                "email": "weisheit129@gmail.com",
                "focus": "Wisdom & Deep Learning",
                "status": "Active"
            }
        }
        
    def check_branch_activity(self, branch_name):
        """Check recent activity on a specific branch"""
        try:
            # Get latest commit info for the branch
            cmd = f"git log origin/{branch_name} --oneline -n 3"
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            
            if result.returncode == 0:
                commits = result.stdout.strip().split('\n')
                return {
                    "status": "Active",
                    "latest_commits": commits[:3] if commits[0] else [],
                    "commit_count": len([c for c in commits if c.strip()])
                }
            else:
                return {
                    "status": "No Activity",
                    "latest_commits": [],
                    "commit_count": 0
                }
        except Exception as e:
            return {
                "status": "Error",
                "error": str(e),
                "latest_commits": [],
                "commit_count": 0
            }

    def check_day01_progress(self, branch_name):
        """Check if team member has day01 folder and files"""
        try:
            # Check if day01 folder exists
            cmd = f"git ls-tree origin/{branch_name} day01/"
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            
            if result.returncode == 0:
                files = result.stdout.strip().split('\n')
                return {
                    "day01_exists": True,
                    "files": [f.split('\t')[-1] for f in files if f.strip()],
                    "file_count": len([f for f in files if f.strip()])
                }
            else:
                return {
                    "day01_exists": False,
                    "files": [],
                    "file_count": 0
                }
        except Exception as e:
            return {
                "day01_exists": False,
                "error": str(e),
                "files": [],
                "file_count": 0
            }

    def check_day02_progress(self, branch_name):
        """Check if team member has day02 folder and advanced Python files"""
        try:
            # Check if day02 folder exists
            cmd = f"git ls-tree origin/{branch_name} day-2/"
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            
            if result.returncode == 0:
                files = result.stdout.strip().split('\n')
                file_list = [f.split('\t')[-1] for f in files if f.strip()]
                
                # Check for specific Day 2 learning files
                expected_files = [
                    "README.md",
                    "advanced_print_methods.py", 
                    "variables_guide.py",
                    "data_types_tutorial.py",
                    "practice_exercises.py"
                ]
                
                completed_files = [f for f in expected_files if f"day-2/{f}" in '\n'.join(file_list)]
                
                return {
                    "day02_exists": True,
                    "files": file_list,
                    "file_count": len(file_list),
                    "completed_files": completed_files,
                    "completion_rate": len(completed_files) / len(expected_files) * 100
                }
            else:
                return {
                    "day02_exists": False,
                    "files": [],
                    "file_count": 0,
                    "completed_files": [],
                    "completion_rate": 0
                }
        except Exception as e:
            return {
                "day02_exists": False,
                "error": str(e),
                "files": [],
                "file_count": 0,
                "completed_files": [],
                "completion_rate": 0
            }

    def generate_progress_report(self):
        """Generate comprehensive progress report"""
        print("="*70)
        print("📊 AI-ACE TEAM PROGRESS REPORT")
        print(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70)
        
        total_members = len(self.team_members)
        active_members = 0
        day01_completed = 0
        day02_completed = 0
        
        for branch, member in self.team_members.items():
            print(f"\n👤 {member['name']} ({branch})")
            print("-" * 50)
            
            # Check branch activity
            activity = self.check_branch_activity(branch)
            print(f"🔄 Branch Status: {activity['status']}")
            print(f"📝 Recent Commits: {activity['commit_count']}")
            
            if activity['latest_commits']:
                print("📋 Latest Activity:")
                for commit in activity['latest_commits'][:2]:
                    if commit.strip():
                        print(f"   • {commit[:60]}...")
            
            # Check Day 1 progress
            day01 = self.check_day01_progress(branch)
            if day01['day01_exists']:
                print(f"✅ Day 1 Progress: Completed ({day01['file_count']} files)")
                day01_completed += 1
            else:
                print("❌ Day 1 Progress: Not started")
            
            # Check Day 2 progress  
            day02 = self.check_day02_progress(branch)
            if day02['day02_exists']:
                completion = day02['completion_rate']
                if completion >= 80:
                    status_emoji = "🌟"
                    status_text = "Excellent"
                elif completion >= 60:
                    status_emoji = "✅"
                    status_text = "Good"
                elif completion >= 40:
                    status_emoji = "🔄"
                    status_text = "In Progress"
                else:
                    status_emoji = "🔶"
                    status_text = "Started"
                    
                print(f"{status_emoji} Day 2 Progress: {status_text} ({completion:.0f}% complete)")
                print(f"   📚 Advanced Python: {len(day02['completed_files'])}/5 files")
                
                if completion >= 60:
                    day02_completed += 1
            else:
                print("❌ Day 2 Progress: Not started")
            
            # Additional info
            if 'role' in member:
                print(f"🎯 Role: {member['role']}")
            if 'email' in member:
                print(f"📧 Contact: {member['email']}")
            
            if activity['status'] == "Active":
                active_members += 1
        
        # Summary
        print("\n" + "="*70)
        print("📈 TEAM SUMMARY")
        print("="*70)
        print(f"👥 Total Team Members: {total_members}")
        print(f"🟢 Active Members: {active_members}")
        print(f"🐔 Day 1 Completed: {day01_completed}")
        print(f"� Day 2 Progressing: {day02_completed}")
        print(f"📊 Overall Progress: {((day01_completed + day02_completed)/(total_members * 2))*100:.1f}%")
        
        # Learning milestones
        print(f"\n📚 LEARNING MILESTONES:")
        print(f"   🐣 Python Basics (Day 1): {day01_completed}/{total_members}")
        print(f"   🔥 Advanced Print & Variables (Day 2): {day02_completed}/{total_members}")
        
        # Team health indicator
        health_score = (active_members + day01_completed + day02_completed) / (total_members * 3) * 100
        if health_score >= 80:
            print(f"🌟 Team Health: EXCELLENT ({health_score:.1f}%)")
        elif health_score >= 60:
            print(f"✅ Team Health: GOOD ({health_score:.1f}%)")
        elif health_score >= 40:
            print(f"⚠️  Team Health: NEEDS ATTENTION ({health_score:.1f}%)")
        else:
            print(f"🚨 Team Health: NEEDS SUPPORT ({health_score:.1f}%)")
            
        # Day 2 specific encouragement
        if day02_completed < total_members:
            print(f"\n💡 NEXT STEPS:")
            print(f"   🎯 Focus on Day 2: Advanced print methods and variables")
            print(f"   📖 Key topics: f-strings, ANSI colors, data types")
            print(f"   🤝 Encourage peer learning and code sharing")

    def show_quick_links(self):
        """Display quick GitHub links for team monitoring"""
        print("\n🔗 QUICK TEAM MONITORING LINKS")
        print("="*50)
        print("📊 Repository Overview:")
        print("  https://github.com/aiegoo/ai-ace")
        print("\n🌿 All Branches:")
        print("  https://github.com/aiegoo/ai-ace/branches")
        print("\n📈 Team Activity:")
        print("  https://github.com/aiegoo/ai-ace/pulse")
        print("\n👥 Individual Branches:")
        
        for branch, member in self.team_members.items():
            print(f"  {member['name']}: https://github.com/aiegoo/ai-ace/tree/{branch}")

    def show_encouragement_tips(self):
        """Show leadership tips for encouraging the team"""
        tips = [
            "🌟 Celebrate small wins - every commit matters!",
            "💬 Check in regularly via Discord or comments",
            "🤝 Pair struggling members with confident ones",
            "📚 Share additional resources for common challenges", 
            "🎯 Focus on learning, not just completion",
            "🔄 Encourage experimentation and creativity",
            "💪 Remind them that mistakes are part of learning"
        ]
        
        print("\n💡 LEADERSHIP TIPS")
        print("="*40)
        for tip in tips:
            print(f"  {tip}")

def main():
    """Main function to run team progress tracking"""
    tracker = TeamProgressTracker()
    
    print("🚀 AI-ACE Team Progress Tracker")
    print("👨‍💼 Team Leader Dashboard")
    
    while True:
        print("\n📊 Progress Tracking Options:")
        print("1. 📈 Generate Full Progress Report")
        print("2. 👥 List Team Members") 
        print("3. 🔗 Show Quick Monitoring Links")
        print("4. 💡 Show Leadership Tips")
        print("5. 🚪 Exit")
        
        choice = input("\n👨‍💼 Choose an option (1-5): ").strip()
        
        if choice == '1':
            tracker.generate_progress_report()
        elif choice == '2':
            print("\n👥 AI-ACE Team Members:")
            for branch, member in tracker.team_members.items():
                status = "🟢" if member['status'] == 'Active' else "🔴"
                print(f"  {status} {member['name']} ({branch})")
        elif choice == '3':
            tracker.show_quick_links()
        elif choice == '4':
            tracker.show_encouragement_tips()
        elif choice == '5':
            print("\n🎯 Keep leading with empathy and encouragement! 🚀")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()