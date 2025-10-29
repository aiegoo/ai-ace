#!/usr/bin/env python3
"""
AI-ACE Creative Examples - Advanced Chicken Art Inspiration
Team Leader Collection by Tony Lee (@aiegoo)

This file contains advanced examples and creative variations
to inspire team members and demonstrate advanced concepts.
"""

import time
import random
import os
from datetime import datetime

class CreativeChickenExamples:
    
    def animated_chicken(self):
        """Animated chicken that changes expressions"""
        expressions = [
            # Happy chicken
            '''
                    🌟
                  ╭─────╮
                 ╱       ╲
                ╱  ◕   ◕  ╲
               ╱     ω     ╲
              ╱  ╲       ╱  ╲
             ╱    ╲_____╱    ╲
            ╱_______________╲
           ▕      😊        ▏
           ▕   ╲   ╱ ╲   ╱   ▏
           ▕    ╲ ╱   ╲ ╱    ▏
            ╲               ╱
             ╲    ◣   ◢    ╱
              ╲  ╱ ╲ ╱ ╲  ╱
               ╲╱   ╱   ╲╱
            ''',
            # Surprised chicken
            '''
                    ⚡
                  ╭─────╮
                 ╱       ╲
                ╱  ◯   ◯  ╲
               ╱     ▲     ╲
              ╱  ╲       ╱  ╲
             ╱    ╲_____╱    ╲
            ╱_______________╲
           ▕      😮        ▏
           ▕   ╲   ╱ ╲   ╱   ▏
           ▕    ╲ ╱   ╲ ╱    ▏
            ╲               ╱
             ╲    ◣   ◢    ╱
              ╲  ╱ ╲ ╱ ╲  ╱
               ╲╱   ╱   ╲╱
            ''',
            # Coding chicken
            '''
                    💻
                  ╭─────╮
                 ╱       ╲
                ╱  ◉   ◉  ╲
               ╱     ▼     ╲
              ╱  ╲       ╱  ╲
             ╱    ╲_____╱    ╲
            ╱_______________╲
           ▕      🤓        ▏
           ▕   ╲   ╱ ╲   ╱   ▏
           ▕    ╲ ╱   ╲ ╱    ▏
            ╲               ╱
             ╲    ◣   ◢    ╱
              ╲  ╱ ╲ ╱ ╲  ╱
               ╲╱   ╱   ╲╱
            '''
        ]
        
        print("🎬 Animated Chicken Demo:")
        for i, expression in enumerate(expressions):
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
            print(f"Frame {i+1}/3")
            print(expression)
            time.sleep(1.5)

    def rainbow_chicken(self):
        """Chicken with colorful ASCII art using ANSI colors"""
        # ANSI color codes
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'reset': '\033[0m'
        }
        
        chicken = f'''
            {colors['yellow']}🌈 Rainbow Coding Chicken 🌈{colors['reset']}
                    {colors['red']}╭─────╮{colors['reset']}
                   {colors['red']}╱       ╲{colors['reset']}
                  {colors['yellow']}╱  ◕   ◕  ╲{colors['reset']}
                 {colors['green']}╱     ω     ╲{colors['reset']}
                {colors['cyan']}╱  ╲       ╱  ╲{colors['reset']}
               {colors['blue']}╱    ╲_____╱    ╲{colors['reset']}
              {colors['magenta']}╱_______________╲{colors['reset']}
             {colors['red']}▕   🎨 AI-ACE 🎨   ▏{colors['reset']}
             {colors['yellow']}▕   ╲   ╱ ╲   ╱   ▏{colors['reset']}
             {colors['green']}▕    ╲ ╱   ╲ ╱    ▏{colors['reset']}
              {colors['cyan']}╲               ╱{colors['reset']}
               {colors['blue']}╲    ◣   ◢    ╱{colors['reset']}
                {colors['magenta']}╲  ╱ ╲ ╱ ╲  ╱{colors['reset']}
                 {colors['red']}╲╱   ╱   ╲╱{colors['reset']}
        '''
        return chicken

    def coding_chicken_with_progress(self):
        """Interactive chicken that shows coding progress"""
        progress_stages = [
            ("🤔 Thinking...", "Planning the solution"),
            ("💡 Got an idea!", "Designing the algorithm"), 
            ("⌨️  Coding...", "Writing the implementation"),
            ("🐛 Debugging...", "Fixing those pesky bugs"),
            ("✅ Success!", "Code is working perfectly!")
        ]
        
        base_chicken = '''
                  ╭─────╮
                 ╱       ╲
                ╱  {eyes}  ╲
               ╱     {mouth}     ╲
              ╱  ╲       ╱  ╲
             ╱    ╲_____╱    ╲
            ╱_______________╲
           ▕   {status}   ▏
           ▕   ╲   ╱ ╲   ╱   ▏
           ▕    ╲ ╱   ╲ ╱    ▏
            ╲               ╱
             ╲    ◣   ◢    ╱
              ╲  ╱ ╲ ╱ ╲  ╱
               ╲╱   ╱   ╲╱
        '''
        
        eye_states = ["◔ ◔", "◉ ◉", "● ●", "◐ ◑", "★ ★"]
        mouth_states = ["ω", "▼", "◡", "□", "♦"]
        
        print("🎭 Coding Progress Chicken:")
        for i, (stage, description) in enumerate(progress_stages):
            print(f"\n{stage}")
            print(f"📝 {description}")
            
            chicken = base_chicken.format(
                eyes=eye_states[i],
                mouth=mouth_states[i], 
                status=stage[:12]  # Truncate for display
            )
            print(chicken)
            time.sleep(2)

    def team_collaboration_chicken(self):
        """Chicken representing team collaboration"""
        return '''
            👥 Team Collaboration Power! 👥
                    ╭─────╮
                   ╱   🤝   ╲
                  ╱  ◕   ◕  ╲
                 ╱     ▽     ╲
                ╱  ╲   💪   ╱  ╲
               ╱    ╲_____╱    ╲
              ╱_______________╲
             ▕  ChangMin 👋    ▏
             ▕  Heozico 📝     ▏
             ▕  Joonii93 ⚙️    ▏
             ▕  Jsmin2080 🤖   ▏
             ▕  Weisheit129 🧠 ▏
             ▕  Tony 👨‍💼        ▏
              ╲               ╱
               ╲    ◣   ◢    ╱
                ╲  ╱ ╲ ╱ ╲  ╱
                 ╲╱   ╱   ╲╱
                  ▕▔▔▔▔▔▔▔▏
                  ▕  🚀   ▏
                  ▕▁▁▁▁▁▁▁▏
        '''

    def motivational_chicken(self):
        """Chicken with inspirational coding quotes"""
        quotes = [
            "🌟 'Code is poetry in logic!'",
            "💪 'Every expert was once a beginner!'", 
            "🚀 'Debug your fears, deploy your dreams!'",
            "🎯 'Commit to learning, push to grow!'",
            "🔥 'Iterate, don't give up!'",
            "⭐ 'Your only limit is your imagination!'"
        ]
        
        quote = random.choice(quotes)
        
        return f'''
            💬 Motivational Coding Chicken 💬
                    ╭─────╮
                   ╱       ╲
                  ╱  ◕   ◕  ╲
                 ╱     ω     ╲
                ╱  ╲       ╱  ╲
               ╱    ╲_____╱    ╲
              ╱_______________╲
             ▕      😊        ▏
             ▕   ╲   ╱ ╲   ╱   ▏
             ▕    ╲ ╱   ╲ ╱    ▏
              ╲               ╱
               ╲    ◣   ◢    ╱
                ╲  ╱ ╲ ╱ ╲  ╱
                 ╲╱   ╱   ╲╱
                  ▕▔▔▔▔▔▔▔▏
                  ▕ 🎈 💝 ▏  
                  ▕▁▁▁▁▁▁▁▏
            
            {quote}
        '''

    def interactive_demo(self):
        """Run an interactive demonstration of all examples"""
        print("🎨 Creative Chicken Art Gallery")
        print("="*50)
        
        examples = {
            "1": ("🎬 Animated Chicken", self.animated_chicken),
            "2": ("🌈 Rainbow Chicken", lambda: print(self.rainbow_chicken())),
            "3": ("⌨️  Coding Progress", self.coding_chicken_with_progress),
            "4": ("👥 Team Collaboration", lambda: print(self.team_collaboration_chicken())),
            "5": ("💬 Motivational Quote", lambda: print(self.motivational_chicken()))
        }
        
        while True:
            print("\n🎨 Creative Examples Menu:")
            for key, (name, _) in examples.items():
                print(f"{key}. {name}")
            print("6. 🚪 Back to main menu")
            
            choice = input("\n🎯 Choose an example (1-6): ").strip()
            
            if choice in examples:
                examples[choice][1]()
                input("\n⏸️  Press Enter to continue...")
            elif choice == "6":
                break
            else:
                print("❌ Invalid choice. Please try again.")

def main():
    """Main function to showcase creative examples"""
    examples = CreativeChickenExamples()
    
    print("🎨 AI-ACE Creative Chicken Art Examples")
    print("👨‍💼 Leader's Inspiration Collection")
    print("="*60)
    
    examples.interactive_demo()

if __name__ == "__main__":
    main()