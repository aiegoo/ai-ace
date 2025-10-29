#!/usr/bin/env python3
"""
Day 1 Reference Solution: Creative Chicken Art
==============================================

This is the CREATIVE solution - let your imagination fly! 🎨

Learning objectives:
- Creative problem solving
- Interactive programming
- File operations
- Advanced ASCII techniques
- Having fun with code!

Author: AI-ACE Team Reference
"""

import random
import time
import os
from datetime import datetime

class ChickenFarm:
    """
    A creative chicken farm with multiple chickens and interactive features!
    """
    
    def __init__(self):
        self.chickens = []
        self.farm_name = "Happy Chicken Farm"
        self.colors = {
            'yellow': '\033[93m', 'red': '\033[91m', 'green': '\033[92m',
            'blue': '\033[94m', 'magenta': '\033[95m', 'cyan': '\033[96m',
            'white': '\033[97m', 'reset': '\033[0m', 'bold': '\033[1m'
        }
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def colorize(self, text, color, bold=False):
        """Add color and optional bold to text."""
        result = text
        if bold:
            result = f"{self.colors['bold']}{result}"
        if color in self.colors:
            result = f"{self.colors[color]}{result}{self.colors['reset']}"
        return result
    
    def create_chicken_family(self):
        """Create a family of chickens with different personalities."""
        print(self.colorize("🏠 Creating the Chicken Family!", "yellow", bold=True))
        print()
        
        # Baby chicken
        self.draw_baby_chicken()
        
        # Mama chicken
        self.draw_mama_chicken()
        
        # Papa rooster
        self.draw_papa_rooster()
        
        # Grandma chicken
        self.draw_grandma_chicken()
    
    def draw_baby_chicken(self):
        """Draw an adorable baby chicken."""
        print(self.colorize("🐣 Baby Peep:", "cyan"))
        print()
        print("        •")
        print("       ^^^")
        print("      ( o )")  
        print("       \\_/")
        print("        |")
        print("       /|\\") 
        print("      -- --")
        print()
    
    def draw_mama_chicken(self):
        """Draw a caring mama chicken."""
        print(self.colorize("🐔 Mama Hen:", "magenta"))
        print()
        print("       ♥♥♥")
        print("      /---\\")
        print("     | o o |")
        print("     |  v  |") 
        print("      \\___/")
        print("       |||")
        print("     \"\"   \"\"")
        print("    \"\"\"   \"\"\"")
        print("       | |")
        print("      -- --")
        print()
    
    def draw_papa_rooster(self):
        """Draw a proud papa rooster."""
        print(self.colorize("🐓 Papa Rooster:", "red"))
        print()
        print("      ★★★★★")
        print("     /-----\\")
        print("    | O   O |")
        print("    |   >   |")
        print("     \\  ~  /")
        print("      \\___/")
        print("       ||||")
        print("     \"\"\"\"\"\"\"\"")
        print("       || ||")
        print("      --- ---")
        print()
    
    def draw_grandma_chicken(self):
        """Draw a wise grandma chicken with glasses."""
        print(self.colorize("👵 Grandma Chicken:", "green"))
        print()
        print("       ^^^")
        print("      /---\\")
        print("     |◯   ◯|")  # Glasses
        print("     |  v  |")
        print("      \\___/")
        print("       |||")
        print("     ··   ··")  # Polka dots
        print("       | |")
        print("      ·· ··")
        print()
    
    def create_chicken_scene(self):
        """Create a complete barnyard scene."""
        print(self.colorize("🌅 Sunrise at the Chicken Farm", "yellow", bold=True))
        print()
        
        # Sky and sun
        print(self.colorize("                    ☀️", "yellow"))
        print(self.colorize("         ☁️              ☁️", "cyan"))
        print()
        
        # Chickens in the yard
        print("    🐓              🐔        🐣")
        print("     |               |         |")
        print("    ---             ---       ---")
        print()
        
        # Ground with feed
        print(self.colorize("🌱🌾🌱🌾🌱🌾🌱🌾🌱🌾🌱🌾🌱🌾", "green"))
        print(self.colorize("         • • •    (chicken feed)", "yellow"))
        print()
        
        # Barn
        print(self.colorize("         🏠 Chicken Coop 🏠", "red"))
        print(self.colorize("        /|\\    /|\\    /|\\", "red"))
        print()
    
    def interactive_chicken_creator(self):
        """Let the user create their own custom chicken."""
        print(self.colorize("🎨 Create Your Own Chicken!", "cyan", bold=True))
        print()
        
        # Get user preferences
        print("Choose features for your chicken:")
        
        # Eyes
        eye_options = ["o o", "• •", "O O", "^ ^", "* *", "@ @"]
        print("Eyes options:", " | ".join(eye_options))
        eyes = input("Choose eyes (or press Enter for random): ").strip()
        if not eyes:
            eyes = random.choice(eye_options)
        
        # Comb
        comb_options = ["^^^", "~~~", "***", "♦♦♦", "♠♠♠"]
        print("Comb options:", " | ".join(comb_options))
        comb = input("Choose comb (or press Enter for random): ").strip()
        if not comb:
            comb = random.choice(comb_options)
        
        # Color
        color_options = list(self.colors.keys())[:-2]  # Exclude 'reset' and 'bold'
        print("Color options:", " | ".join(color_options))
        color = input("Choose color (or press Enter for random): ").strip()
        if not color or color not in self.colors:
            color = random.choice(color_options)
        
        # Name
        name = input("Give your chicken a name: ").strip()
        if not name:
            name = "Custom Chicken"
        
        # Draw the custom chicken
        print()
        print(self.colorize(f"🎉 Meet {name}!", color, bold=True))
        print()
        
        chicken_art = f"""      {comb}
     /-----\\
    | {eyes} |
    |   v   |
     \\-----/
      |||
    \"\"   \"\"
      | |
     -- --"""
        
        print(self.colorize(chicken_art, color))
        print()
        
        # Save to file option
        save = input("Save your chicken to a file? (y/n): ").strip().lower()
        if save == 'y':
            self.save_chicken_to_file(name, chicken_art, color)
    
    def save_chicken_to_file(self, name, art, color):
        """Save the chicken art to a text file."""
        try:
            filename = f"my_chicken_{name.replace(' ', '_').lower()}.txt"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"My Custom Chicken: {name}\n")
                f.write(f"Created on: {timestamp}\n")
                f.write(f"Color: {color}\n")
                f.write("=" * 30 + "\n\n")
                f.write(art)
                f.write("\n\n" + "=" * 30)
                f.write("\nCreated with AI-ACE Chicken Creator!")
            
            print(f"✅ Chicken saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving file: {e}")
    
    def chicken_parade(self):
        """Animated parade of chickens walking across the screen."""
        print(self.colorize("🎪 Chicken Parade!", "yellow", bold=True))
        print("Watch the chickens march! (Press Ctrl+C to stop)")
        print()
        
        chickens = [
            "🐓", "🐔", "🐣", "🐤", "🐥"
        ]
        
        try:
            for position in range(50):
                self.clear_screen()
                print(self.colorize("🎪 Chicken Parade!", "yellow", bold=True))
                print()
                
                # Create the parade line
                parade_line = " " * position
                for i, chicken in enumerate(chickens):
                    if position + i * 3 < 50:
                        parade_line += chicken + "  "
                
                print(parade_line)
                print("_" * 50)  # Ground
                print()
                print("Press Ctrl+C to stop the parade...")
                
                time.sleep(0.2)
                
        except KeyboardInterrupt:
            print("\n🎉 Parade finished! The chickens are tired.")
    
    def chicken_ascii_gallery(self):
        """Display a gallery of different ASCII chicken styles."""
        print(self.colorize("🖼️  Chicken Art Gallery", "magenta", bold=True))
        print()
        
        styles = {
            "Minimalist": [
                "  o",
                " /|\\",
                " / \\"
            ],
            "Geometric": [
                "  ▲▲▲",
                " ◆   ◆",
                "   ▼",
                "  |||",
                " ─┴─┴─"
            ],
            "Emoji Style": [
                " 🟨🟨🟨",
                "🟨 👁️ 👁️ 🟨",
                " 🟨 👄 🟨",
                "  🟨🟨🟨",
                "   🦵🦵"
            ],
            "Unicode Art": [
                "   ♪♪♪",
                "  ◕   ◕",
                "    ◊",
                "   ═══",
                "   ║ ║",
                "  ╚═ ═╝"
            ]
        }
        
        for style_name, art_lines in styles.items():
            print(self.colorize(f"📸 {style_name} Chicken:", "cyan"))
            for line in art_lines:
                print(f"    {line}")
            print()
    
    def main_menu(self):
        """Interactive main menu for the chicken farm."""
        while True:
            self.clear_screen()
            print(self.colorize("🐔 Welcome to the Creative Chicken Farm! 🐔", "yellow", bold=True))
            print()
            print("Choose an option:")
            print("1. 👨‍👩‍👧‍👦 Meet the Chicken Family")
            print("2. 🌅 View Barnyard Scene") 
            print("3. 🎨 Create Your Own Chicken")
            print("4. 🎪 Watch Chicken Parade")
            print("5. 🖼️  Visit Art Gallery")
            print("6. 🚪 Exit Farm")
            print()
            
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                self.clear_screen()
                self.create_chicken_family()
                input("\nPress Enter to continue...")
            elif choice == "2":
                self.clear_screen()
                self.create_chicken_scene()
                input("\nPress Enter to continue...")
            elif choice == "3":
                self.clear_screen()
                self.interactive_chicken_creator()
                input("\nPress Enter to continue...")
            elif choice == "4":
                self.chicken_parade()
                input("\nPress Enter to continue...")
            elif choice == "5":
                self.clear_screen()
                self.chicken_ascii_gallery()
                input("\nPress Enter to continue...")
            elif choice == "6":
                print(self.colorize("🐔 Thanks for visiting the farm! Goodbye! 🐔", "green"))
                break
            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)

def run_creative_demo():
    """Run the creative chicken art demonstration."""
    farm = ChickenFarm()
    
    print("🎨 Starting Creative Chicken Art Demo...")
    print("This is the CREATIVE solution - full of fun features!")
    print()
    input("Press Enter to begin...")
    
    farm.main_menu()

if __name__ == "__main__":
    run_creative_demo()

"""
🎨 CREATIVE LEARNING NOTES:

1. INTERACTIVE PROGRAMMING:
   - input() gets user responses
   - while True: creates infinite loops (use break to exit)
   - Menus make programs user-friendly

2. FILE OPERATIONS:
   - open() and with statements handle files safely
   - 'w' mode writes to files
   - encoding='utf-8' handles special characters

3. EXCEPTION HANDLING:
   - try/except prevents crashes
   - Handle specific errors gracefully
   - Always provide user feedback

4. ADVANCED ASCII:
   - Unicode characters: ◆ ♪ ◕ ╚ ═
   - Emojis in code: 🐔 🌅 ⭐
   - Combine characters for complex art

5. ANIMATION TECHNIQUES:
   - Clear screen and redraw for animation
   - time.sleep() controls speed
   - Loops create movement

6. CODE ORGANIZATION:
   - Classes group related functionality
   - Methods break complex tasks into steps
   - Clear naming makes code readable

💭 CREATIVE REFLECTION:
- How does interactivity change the user experience?
- What other creative features could you add?
- How would you make this into a game?
- What real applications use similar techniques?

🚀 ULTIMATE CHALLENGES:
- Add sound effects (system beeps)
- Create chicken personality traits
- Build a chicken breeding game
- Add weather effects to the scene
- Create chicken adventures/stories
- Build a multiplayer chicken farm
- Add achievements and scoring
- Create different farm locations

🎉 MOST IMPORTANT:
Remember - creativity in programming is about solving problems
in new and interesting ways. There are no wrong answers when
you're being creative! Have fun and experiment!
"""