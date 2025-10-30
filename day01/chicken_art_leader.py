#!/usr/bin/env python3
"""
AI-ACE Team - Day 1 Mission: ASCII Chicken Art
Team Leader Edition by Tony Lee (@aiegoo)

This is the team leader's example solution with enhanced features
to demonstrate advanced concepts for the team.
"""

import time
import random
from datetime import datetime

class ChickenArtLeader:
    def __init__(self):
        self.team_name = "AI-ACE"
        self.leader_name = "이병남 (Tony Lee)"
        self.team_members = [
            "장수민 (ChangMin)", "허지호 (Heozico)", "이상준 (Joonii93)", 
            "정수민 (Jsmin2080)", "고준 (Weisheit129)"
        ]

    def show_team_logo(self):
        """Display the AI-ACE team logo"""
        print("\n" + "="*50)
        print("   ▄▄▄  ▪      ▄▄▄·  ▄▄·▄▄▄ .")
        print("  ▐█ ▀█ ██     ▐█ ▀█ ▐█ ▌▪▀▄.▀·")
        print("  ▄█▀▀█ ▐█·    ▄█▀▀█ ██ ▄▄▐▀▀▪▄")
        print("  ▐█ ▪▐▌▐█▌    ▐█ ▪▐▌▐███▌▐█▄▄▌")
        print("   ▀  ▀ ▀▀▀     ▀  ▀ ·▀▀▀  ▀▀▀ ")
        print("\n🎯 AI-ACE Team - AI Track 7회차")
        print(f"👨‍💼 Team Leader: {self.leader_name}")
        print(f"👥 Team Members: {len(self.team_members)} strong!")
        print("📅 October 29 - November 27, 2025 (30 days)")
        print("="*50)

    def draw_leader_chicken(self):
        """Draw a special leadership chicken with crown"""
        chicken_art = '''
                     👑
                   ▄▄▄▄▄
                 ╱     ╲
                ╱  ◉   ◉ ╲
               ╱     ▼    ╲  
              ╱  ╲       ╱ ╲
             ╱    ╲_____╱   ╲
            ╱________________╲
           ▕        ●●        ▏
           ▕    ╲  ╱  ╲  ╱    ▏
           ▕     ╲╱    ╲╱     ▏
            ╲               ╱
             ╲    ▄   ▄    ╱
              ╲  ╱ ╲ ╱ ╲  ╱
               ╲╱   ╲╱   ╲╱
                ▕▔▔▔▔▔▔▔▏
                ▕   👔   ▏
                ▕▁▁▁▁▁▁▁▏
        '''
        return chicken_art

    def draw_team_chicken(self):
        """Draw a team collaboration chicken"""
        chicken_art = '''
            🤝 Team Spirit Chicken 🤝
                   ╭─────╮
                  ╱       ╲
                 ╱  ◕   ◕  ╲
                ╱     ω     ╲
               ╱  ╲       ╱  ╲
              ╱    ╲_____╱    ╲
             ╱_______________╲
            ▕     🎯 AI-ACE   ▏
            ▕   ╲   ╱ ╲   ╱   ▏
            ▕    ╲ ╱   ╲ ╱    ▏
             ╲               ╱
              ╲    ◣   ◢    ╱
               ╲  ╱ ╲ ╱ ╲  ╱
                ╲╱   ╱   ╲╱
                 ▕▔▔▔▔▔▔▔▏
                 ▕  💪   ▏
                 ▕▁▁▁▁▁▁▁▏
        '''
        return chicken_art

    def show_team_encouragement(self):
        """Show encouraging message for the team"""
        messages = [
            "🌟 Great job, team! Every expert was once a beginner!",
            "💪 Keep coding! You're building amazing skills!",
            "🚀 Each line of code is a step toward mastery!",
            "🎯 Focus on progress, not perfection!",
            "🔥 Your curiosity and effort inspire me every day!"
        ]
        
        print("\n" + "="*60)
        print("💌 Team Leader's Daily Encouragement:")
        print(random.choice(messages))
        print("="*60)

    def show_learning_goals(self):
        """Display today's learning objectives"""
        goals = [
            "🐍 Master Python basics (variables, functions, loops)",
            "🎨 Understand ASCII art and string manipulation", 
            "🔧 Practice problem-solving and debugging",
            "👥 Experience collaborative coding workflow",
            "📚 Build confidence in programming concepts"
        ]
        
        print("\n📚 Day 1 Learning Goals:")
        for goal in goals:
            print(f"  {goal}")

    def run_leader_demo(self):
        """Run the complete leader demonstration"""
        print("\n🎮 Starting AI-ACE Day 1 - Leadership Demo")
        time.sleep(1)
        
        # Show team branding
        self.show_team_logo()
        time.sleep(2)
        
        # Show learning goals
        self.show_learning_goals()
        time.sleep(2)
        
        # Display leadership chicken
        print(f"\n🐔 Leader Chicken by {self.leader_name}:")
        print(self.draw_leader_chicken())
        time.sleep(2)
        
        # Display team chicken
        print("\n🐔 Team Collaboration Chicken:")
        print(self.draw_team_chicken())
        time.sleep(2)
        
        # Show encouragement
        self.show_team_encouragement()
        
        # Show completion
        print(f"\n✅ Leadership demo completed!")
        print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("🎯 Ready to support the team through Day 1!")

def main():
    """Main function to run the leader's chicken art demo"""
    leader = ChickenArtLeader()
    
    print("="*60)
    print("🚀 AI-ACE Day 1: ASCII Chicken Art - Leadership Edition")
    print("="*60)
    
    while True:
        print("\n🎯 Leadership Demo Options:")
        print("1. 👑 Show Leader Chicken")
        print("2. 🤝 Show Team Chicken") 
        print("3. 🌟 Show Team Encouragement")
        print("4. 🎮 Run Complete Demo")
        print("5. 👥 List Team Members")
        print("6. 🚪 Exit")
        
        choice = input("\n👨‍💼 Leader, choose an option (1-6): ").strip()
        
        if choice == '1':
            print(f"\n🐔 Leader Chicken by {leader.leader_name}:")
            print(leader.draw_leader_chicken())
        elif choice == '2':
            print("\n🐔 Team Collaboration Chicken:")
            print(leader.draw_team_chicken())
        elif choice == '3':
            leader.show_team_encouragement()
        elif choice == '4':
            leader.run_leader_demo()
        elif choice == '5':
            print(f"\n👥 AI-ACE Team Members:")
            for i, member in enumerate(leader.team_members, 1):
                print(f"  {i}. {member}")
            print(f"\n👨‍💼 Leader: {leader.leader_name}")
        elif choice == '6':
            print("\n🎯 Great leadership today! Keep inspiring the team! 🚀")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()