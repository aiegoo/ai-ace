#!/usr/bin/env python3
"""
Day 1 Reference Solution: Basic Chicken Art
===========================================

This is the BASIC solution - perfect for beginners!

Learning objectives:
- Understanding print() statements
- Creating simple ASCII art
- Using basic Python syntax
- Building confidence with coding

Author: AI-ACE Team Reference
"""

def show_team_name():
    """Display our AI-ACE team name in ASCII art"""
    print("🏆 Our Team:")
    print()
    print(" ▄▄▄· ▪       ▄▄▄·  ▄▄· ▄▄▄ .")
    print("▐█ ▀█ ██     ▐█ ▀█ ▐█ ▌▪▀▄.▀·")
    print("▄█▀▀█ ▐█·    ▄█▀▀█ ██ ▄▄▐▀▀▪▄")
    print("▐█ ▪▐▌▐█▌    ▐█ ▪▐▌▐███▌▐█▄▄▌")
    print(" ▀  ▀ ▀▀▀     ▀  ▀ ·▀▀▀  ▀▀▀ ")
    print()
    print("🎯 AI-ACE Team - AI Track 7회차")
    print("👥 6 members strong and coding together!")
    print()

def draw_simple_chicken():
    """
    The simplest possible chicken using just print statements.
    Great for absolute beginners!
    """
    print("🐔 Basic Chicken:")
    print()
    print("    o o")      # Eyes
    print("   < v >")     # Beak pointing down
    print("    ^^^")      # Feathers/comb
    print("   |   |")     # Neck
    print("  -----")      # Body
    print("   | |")       # Legs
    print("  -- --")      # Feet
    print()

def draw_medium_chicken():
    """
    A slightly more detailed chicken - still very simple!
    """
    print("🐔 Medium Chicken:")
    print()
    print("     ,-^-.")    # Head with comb
    print("    /  o  \\")   # Head with eyes
    print("   |   v   |")  # Beak
    print("    \\  ~  /")   # Smile
    print("     \\___/")    # Head bottom
    print("      | |")     # Neck
    print("     _| |_")    # Body
    print("    |     |")   # Body
    print("     -----")    # Body bottom
    print("      | |")     # Legs
    print("     -- --")    # Feet
    print()

def draw_cute_chicken():
    """
    A cute chicken with personality!
    Uses simple characters but more detailed design.
    """
    print("🐔 Cute Chicken:")
    print()
    print("      ^^^")      # Comb
    print("     ( o o )")   # Eyes in parentheses
    print("      \\ v /")    # Beak
    print("       \\_/")     # Chin
    print("        |")      # Neck
    print("      /|||\\")    # Body with feathers
    print("     |  |  |")   # Body
    print("      \\| |/")    # Body bottom
    print("       | |")     # Legs
    print("      _| |_")    # Feet
    print()

def draw_special_chicken():
    """
    A special cute chicken - simple but charming!
    """
    print("🥰 Special Cute Chicken:")
    print()
    print("      8c")
    print("   __/~\\__")
    print("  (((\_/)))")
    print("    _) (_")
    print("           elbee&")
    print()

def main():
    """
    Main function - runs all our chicken drawings!
    """
    # Show our team first!
    show_team_name()
    
    print("=" * 50)
    print("🎨 DAY 1: ASCII CHICKEN ART - BASIC SOLUTIONS")
    print("=" * 50)
    print()
    
    # Draw all four chickens
    draw_simple_chicken()
    draw_medium_chicken()
    draw_cute_chicken()
    draw_special_chicken()  # Our new cute chicken!
    
    print("🎉 Great job! You've created ASCII art!")
    print("💡 Try modifying the characters to create your own design!")
    print()

# This is what makes the program run when you execute the file
if __name__ == "__main__":
    main()

"""
📚 LEARNING NOTES:

1. PRINT STATEMENTS:
   - print("text") displays text on screen
   - print() with no arguments creates a blank line
   - You can print special characters like emojis 🐔

2. STRINGS:
   - Text goes inside quotes: "hello" or 'hello'
   - Use backslash to escape special characters: \\

3. FUNCTIONS:
   - def function_name(): starts a function
   - Functions help organize your code
   - Call functions by typing their name with ()

4. COMMENTS:
   - Lines starting with # are comments
   - Comments help explain your code
   - \"\"\"Triple quotes\"\"\" for longer explanations

5. ASCII ART TIPS:
   - Start simple - even basic shapes work!
   - Use characters that create clear outlines
   - Don't worry about making it perfect
   - Have fun and be creative!

💭 REFLECTION QUESTIONS:
- Which chicken design do you like best?
- What characters create the best chicken features?
- How would you make your chicken look different?
- What other animals could you draw with ASCII?

🚀 NEXT STEPS:
- Try changing the characters in each chicken
- Add more details like wings or tail feathers
- Create your own unique chicken design
- Experiment with different layouts
"""