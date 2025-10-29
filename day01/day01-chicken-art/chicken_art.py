#!/usr/bin/env python3
"""
🐔 ASCII Art Chicken Drawing - Day 1 Mission
============================================

Welcome to your first AI Track mission! 
Let's learn Python by creating ASCII art chickens.

Run this file with: python chicken_art.py
"""

import time
import os

# Color codes for terminal output
class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_mission_header():
    """Display the mission welcome message"""
    print("🎨" + "=" * 48 + "🎨")
    print("🐔  ASCII ART CHICKEN DRAWING - DAY 1 MISSION  🐔")
    print("🎨" + "=" * 48 + "🎨")
    print()
    print("Welcome to your first AI Track mission!")
    print("Today we'll learn Python by creating ASCII art chickens.")
    print()

def draw_simple_chicken():
    """Method 1: Simple chicken using basic print statements"""
    print("🐔 Method 1: Simple Chicken Design")
    print("-" * 35)
    print()
    print("    ,-^-.")
    print("   /  o  \\")
    print("  (   v   )")
    print("   \\  ~  /")
    print("    \\___/")
    print("     | |")
    print("    _| |_")
    print()

def draw_pattern_chicken():
    """Method 2: Chicken using string multiplication and patterns"""
    print("🐔 Method 2: Pattern-Based Chicken")
    print("-" * 35)
    print()
    
    # Head with crown
    print("    " + "^" * 3)
    print("   /" + "o" * 3 + "\\")
    print("  |  " + "." + " " + "." + "  |")
    print("  |   " + "v" + "   |")
    print("   \\" + "_" * 3 + "/")
    
    # Body with feathers
    body_width = 7
    for i in range(3):
        feathers = '"' * (2 + i)
        spaces = ' ' * (body_width - len(feathers))
        print("  " + feathers + spaces + feathers)
    
    # Legs
    print("    |   |")
    print("   /|   |\\")
    print("  " + "-" * 2 + "   " + "-" * 2)
    print()

def draw_detailed_chicken():
    """Method 3: Multi-line string chicken (most detailed)"""
    print("🐔 Method 3: Detailed ASCII Chicken")
    print("-" * 35)
    
    chicken = '''
       ,-"-.
      /       \\
     |  ^   ^  |
     |    >    |
      \\   v   /
       |  ~  |
    .--|  _  |--.
   /   |     |   \\
  |  \\" | \\"\\"\\" | \\"  |
  |    |     |    |
   \\___|_____|___/
      |       |
      |   |   |
     /|   |   |\\
    | |___|___| |
    |_|       |_|
     -         -
    '''
    print(chicken)

def draw_colorful_chicken():
    """Method 4: Colorful chicken with ANSI colors"""
    print("🌈 Method 4: Colorful ASCII Chicken")
    print("-" * 35)
    print()
    
    # Colorful chicken design
    print(f"       {Colors.YELLOW},-\"\"-. {Colors.END}")
    print(f"      {Colors.YELLOW}/       \\{Colors.END}")
    print(f"     {Colors.YELLOW}|  {Colors.RED}^   ^{Colors.YELLOW}  |{Colors.END}")
    print(f"     {Colors.YELLOW}|    {Colors.RED}>{Colors.YELLOW}    |{Colors.END}")
    print(f"      {Colors.YELLOW}\\   {Colors.RED}v{Colors.YELLOW}   /{Colors.END}")
    print(f"       {Colors.YELLOW}|  ~  |{Colors.END}")
    print(f"    {Colors.WHITE}.--{Colors.YELLOW}|  _{Colors.WHITE}  |--. {Colors.END}")
    print(f"   {Colors.WHITE}/{Colors.GREEN}   {Colors.YELLOW}|     |{Colors.GREEN}   \\{Colors.END}")
    print(f"  {Colors.WHITE}|{Colors.GREEN}  \" {Colors.YELLOW}| \"\"\" |{Colors.GREEN} \"  {Colors.WHITE}|{Colors.END}")
    print(f"  {Colors.WHITE}|{Colors.GREEN}    {Colors.YELLOW}|     |{Colors.GREEN}    {Colors.WHITE}|{Colors.END}")
    print(f"   {Colors.WHITE}\\__{Colors.GREEN}_{Colors.YELLOW}|_____|{Colors.GREEN}_{Colors.WHITE}__/{Colors.END}")
    print(f"      {Colors.BLUE}|       |{Colors.END}")
    print(f"      {Colors.BLUE}|   |   |{Colors.END}")
    print(f"     {Colors.BLUE}/{Colors.MAGENTA}|   |   |{Colors.BLUE}\\{Colors.END}")
    print(f"    {Colors.BLUE}| {Colors.MAGENTA}|___|___|{Colors.BLUE} |{Colors.END}")
    print(f"    {Colors.BLUE}|_{Colors.MAGENTA}|       |{Colors.BLUE}_|{Colors.END}")
    print(f"     {Colors.MAGENTA}-         -{Colors.END}")
    print()

def animate_chicken():
    """Method 5: Animated chicken with simple frames"""
    print("🎮 Method 5: Animated Chicken")
    print("-" * 35)
    print("Watch the chicken flap its wings! (3 second animation)")
    print()
    
    frames = [
        # Frame 1 - Standing
        """
       ,-"-.
      /  o  \\
     |   v   |
      \\  ~  /
       \\___/
        | |
       _| |_
        """,
        
        # Frame 2 - Flapping
        """
    \\  ,-"-.  /
     \\/  o  \\/
     |   v   |
      \\  ~  /
       \\___/
        | |
       _| |_
        """,
    ]
    
    # Animate for 3 cycles
    print("🎮 Animation starting...")
    for cycle in range(3):
        for i, frame in enumerate(frames):
            print(f"Frame {i+1}:")
            print(frame)
            time.sleep(0.8)  # Wait between frames
            if i < len(frames) - 1:  # Don't clear after last frame
                print("\n" * 2)  # Some space between frames
    
    print("🎉 Animation complete!")

def draw_cute_chicken():
    """Method 6: Super cute chicken with special style"""
    print("🥰 Method 6: Cute Chicken (Special Style!)")
    print("-" * 35)
    print()
    
    print("      8c")
    print("   __/~\\__")
    print("  (((\_/)))")
    print("    _) (_")
    print("           elbee&")
    print()
    print("💝 This cute design shows creative ASCII art!")

def show_team_name():
    """Display our AI-ACE team name in ASCII art"""
    print("🏆" + "=" * 48 + "🏆")
    print("🎯  OUR TEAM - AI-ACE (AI TRACK 7회차)  🎯")
    print("🏆" + "=" * 48 + "🏆")
    print()
    
    print(" ▄▄▄· ▪       ▄▄▄·  ▄▄· ▄▄▄ .")
    print("▐█ ▀█ ██     ▐█ ▀█ ▐█ ▌▪▀▄.▀·")
    print("▄█▀▀█ ▐█·    ▄█▀▀█ ██ ▄▄▐▀▀▪▄")
    print("▐█ ▪▐▌▐█▌    ▐█ ▪▐▌▐███▌▐█▄▄▌")
    print(" ▀  ▀ ▀▀▀     ▀  ▀ ·▀▀▀  ▀▀▀ ")
    print()
    print("🎯 AI-ACE Team - AI Track 7회차")
    print("👥 6 members strong and coding together!")
    print("📅 October 29 - November 27, 2025 (30 days)")
    print("🚀 Let's master AI development step by step!")
    print()

def create_custom_chicken():
    """Template for students to create their own chicken"""
    print("🎨 YOUR TURN: Custom Chicken Design")
    print("-" * 35)
    print()
    print("Use this function to create your own unique chicken!")
    print("Experiment with different characters and patterns.")
    print()
    
    # Example custom chicken - students can modify this
    print("Example custom chicken (modify this!):")
    print()
    print("    🌤️  <- Add weather!")
    print()
    print("       ,-\"\"-.")
    print("      /  ^_^  \\   <- Happy expression!")
    print("     |    v    |")
    print("      \\   ∪   /   <- Smile!")
    print("       \\____/")
    print("        |  |")
    print("       _|  |_")
    print("    ___________   <- Ground!")
    print()
    print("🌟 Now create your own version above!")

def learning_summary():
    """Display what students learned in this mission"""
    print("📚" + "=" * 48 + "📚")
    print("🎓  MISSION COMPLETE - WHAT YOU LEARNED TODAY  🎓")
    print("📚" + "=" * 48 + "📚")
    print()
    
    skills = [
        "✅ Python print() function and string output",
        "✅ String manipulation and concatenation", 
        "✅ String multiplication for patterns",
        "✅ Multi-line strings with triple quotes",
        "✅ Functions for organizing code",
        "✅ Basic loops (for repetition)",
        "✅ ANSI color codes for terminal styling",
        "✅ Simple animation with time delays",
        "✅ ASCII art creation techniques",
        "✅ Creative problem-solving with code"
    ]
    
    print("🐍 Python Skills Gained:")
    for skill in skills[:5]:
        print(f"  {skill}")
    print()
    
    print("🎨 Creative Programming Skills:")
    for skill in skills[5:]:
        print(f"  {skill}")
    print()
    
    print("🏆 Achievement Unlocked: ASCII Artist! 🏆")
    print("🚀 Ready for your next AI Track mission!")

def main():
    """Main function - run all the chicken drawing methods"""
    # Start with our team name!
    show_team_name()
    input("Press Enter to begin the chicken art mission...")
    
    print_mission_header()
    
    # Wait for user to press Enter between each method
    print("Press Enter to see each chicken design...")
    input()
    
    draw_simple_chicken()
    input("Press Enter for next design...")
    
    draw_pattern_chicken()
    input("Press Enter for next design...")
    
    draw_detailed_chicken()
    input("Press Enter for next design...")
    
    draw_colorful_chicken()
    input("Press Enter for next design...")
    
    draw_cute_chicken()  # Our new cute chicken!
    input("Press Enter for animation...")
    
    animate_chicken()
    input("Press Enter for custom design template...")
    
    create_custom_chicken()
    input("Press Enter for learning summary...")
    
    learning_summary()
    
    print()
    print("🎉 Congratulations on completing Day 1! 🎉")
    print("🐔 Your ASCII chickens are amazing! 🐔")
    print()
    print("💡 Next steps:")
    print("   1. Modify the create_custom_chicken() function")
    print("   2. Create your own unique chicken designs")
    print("   3. Experiment with different characters")
    print("   4. Share your creations!")
    print()
    print("🌟 Save this file and show off your chickens! 🌟")

# Interactive mode - let user choose what to run
def interactive_mode():
    """Let the user choose which chicken to display"""
    # Show team name first
    show_team_name()
    
    while True:
        print("\n🐔 ASCII Chicken Art Gallery 🐔")
        print("=" * 35)
        print("Choose a chicken to display:")
        print("1. Simple Chicken")
        print("2. Pattern Chicken") 
        print("3. Detailed Chicken")
        print("4. Colorful Chicken")
        print("5. Cute Chicken (New!)")
        print("6. Animated Chicken")
        print("7. Custom Chicken Template")
        print("8. Show All Chickens")
        print("9. Show Team Name")
        print("10. Learning Summary")
        print("11. Exit")
        print()
        
        choice = input("Enter your choice (1-11): ").strip()
        
        if choice == '1':
            draw_simple_chicken()
        elif choice == '2':
            draw_pattern_chicken()
        elif choice == '3':
            draw_detailed_chicken()
        elif choice == '4':
            draw_colorful_chicken()
        elif choice == '5':
            draw_cute_chicken()
        elif choice == '6':
            animate_chicken()
        elif choice == '7':
            create_custom_chicken()
        elif choice == '8':
            main()
            break
        elif choice == '9':
            show_team_name()
        elif choice == '10':
            learning_summary()
        elif choice == '11':
            print("🐔 Thanks for using ASCII Chicken Art! Goodbye! 🐔")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    print("🐔 ASCII Chicken Art - Day 1 Mission 🐔")
    print()
    print("How would you like to run this program?")
    print("1. Interactive mode (choose individual chickens)")
    print("2. Full demo (see all chickens in sequence)")
    print()
    
    mode = input("Enter 1 or 2: ").strip()
    
    if mode == '1':
        interactive_mode()
    elif mode == '2':
        main()
    else:
        print("Running in interactive mode by default...")
        interactive_mode()