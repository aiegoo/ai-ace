#!/usr/bin/env python3
"""
Day 1 Reference Solution: Advanced Chicken Art
==============================================

This is the ADVANCED solution for experienced beginners!

Learning objectives:
- Object-oriented programming basics
- String manipulation techniques
- Code organization and reusability
- Error handling
- Advanced Python features

Author: AI-ACE Team Reference
"""

import random
import time

class ChickenArtist:
    """
    A class to create various chicken ASCII art designs.
    This demonstrates object-oriented programming concepts.
    """
    
    def __init__(self, name="Clucky"):
        """Initialize the chicken artist with a name."""
        self.name = name
        self.chickens_drawn = 0
        
        # Color codes for terminal output
        self.colors = {
            'yellow': '\033[93m',
            'red': '\033[91m', 
            'green': '\033[92m',
            'blue': '\033[94m',
            'white': '\033[97m',
            'reset': '\033[0m'
        }
    
    def colorize(self, text, color):
        """Add color to text using ANSI escape codes."""
        if color in self.colors:
            return f"{self.colors[color]}{text}{self.colors['reset']}"
        return text
    
    def draw_parametric_chicken(self, size="medium", style="classic"):
        """
        Draw a chicken with different sizes and styles.
        Demonstrates parameter handling and conditional logic.
        """
        self.chickens_drawn += 1
        
        print(f"🐔 {self.name}'s Chicken #{self.chickens_drawn} ({size}, {style})")
        print()
        
        # Adjust chicken features based on size
        if size == "small":
            head_width = 3
            body_lines = 2
            eye_char = "•"
        elif size == "large":
            head_width = 7
            body_lines = 4
            eye_char = "O"
        else:  # medium
            head_width = 5
            body_lines = 3
            eye_char = "o"
        
        # Style variations
        if style == "fancy":
            comb = "♦" * 3
            feathers = "~"
        elif style == "simple":
            comb = "^" * 3
            feathers = "\""
        else:  # classic
            comb = "^^^"
            feathers = "\""
        
        # Build the chicken dynamically
        self._draw_head(head_width, eye_char, comb)
        self._draw_body(body_lines, feathers)
        self._draw_legs()
        print()
    
    def _draw_head(self, width, eye_char, comb):
        """Helper method to draw chicken head."""
        padding = " " * (width // 2)
        
        print(f"{padding}  {comb}")
        print(f"{padding} /{'-' * width}\\")
        print(f"{padding}| {eye_char}   {eye_char} |")
        print(f"{padding}|   v   |")
        print(f"{padding} \\{'-' * width}/")
    
    def _draw_body(self, lines, feather_char):
        """Helper method to draw chicken body."""
        for i in range(lines):
            feathers = feather_char * (2 + i)
            spaces = " " * (lines - i)
            print(f"{spaces}{feathers}     {feathers}")
    
    def _draw_legs(self):
        """Helper method to draw chicken legs."""
        print("     |   |")
        print("    /|   |\\")
        print("   -- --- --")
    
    def draw_rainbow_chicken(self):
        """
        Create a colorful chicken using ANSI colors.
        Demonstrates advanced string formatting.
        """
        self.chickens_drawn += 1
        
        print(f"🌈 Rainbow Chicken #{self.chickens_drawn}")
        print()
        
        # Each part in different colors
        print(self.colorize("      ^^^", "red"))
        print(self.colorize("     /---\\", "yellow")) 
        print(self.colorize("    | o o |", "green"))
        print(self.colorize("    |  v  |", "blue"))
        print(self.colorize("     \\___/", "yellow"))
        print(self.colorize("      |||", "white"))
        print(self.colorize("    \"\"   \"\"", "red"))
        print(self.colorize("   \"\"\"   \"\"\"", "yellow"))
        print(self.colorize("      | |", "green"))
        print(self.colorize("     -- --", "blue"))
        print()
    
    def draw_animated_chicken(self, frames=3):
        """
        Create a simple animation by showing different poses.
        Demonstrates loops and timing.
        """
        print("🎬 Animated Chicken - Watch it flap!")
        print("(Animation will run for a few seconds)")
        print()
        
        poses = [
            # Pose 1: Wings down
            [
                "      ^^^",
                "     /o o\\",
                "    |  v  |",
                "     \\___/",
                "      | |",
                "     /| |\\",
                "    -- ---"
            ],
            # Pose 2: Wings up
            [
                "  \\   ^^^   /",
                "   \\ /o o\\ /",
                "    |  v  |", 
                "     \\___/",
                "      | |",
                "     /| |\\",
                "    -- ---"
            ]
        ]
        
        try:
            for _ in range(frames):
                for pose in poses:
                    # Clear screen (works on most terminals)
                    print("\033[2J\033[H", end="")
                    print("🎬 Animated Chicken:")
                    print()
                    for line in pose:
                        print(f"    {line}")
                    print()
                    time.sleep(0.8)
        except KeyboardInterrupt:
            print("\n🛑 Animation stopped by user")
        
        print("🎉 Animation complete!")
        print()
    
    def generate_random_chicken(self):
        """
        Generate a chicken with random features.
        Demonstrates random number generation and lists.
        """
        self.chickens_drawn += 1
        
        # Random feature options
        eyes = ["o o", "• •", "O O", "@ @", "^ ^"]
        beaks = ["v", ">", "<", "V", "∨"]
        combs = ["^^^", "♦♦♦", "~~~", "***"]
        bodies = ["|||", "┃┃┃", "│││"]
        
        # Randomly select features
        chosen_eyes = random.choice(eyes)
        chosen_beak = random.choice(beaks)
        chosen_comb = random.choice(combs)
        chosen_body = random.choice(bodies)
        
        print(f"🎲 Random Chicken #{self.chickens_drawn}")
        print()
        print(f"      {chosen_comb}")
        print(f"     /-----\\")
        print(f"    | {chosen_eyes} |")
        print(f"    |   {chosen_beak}   |")
        print(f"     \\-----/")
        print(f"      {chosen_body}")
        print(f"    \"\"     \"\"")
        print(f"      | |")
        print(f"     -- --")
        print()
    
    def get_stats(self):
        """Return statistics about chickens drawn."""
        return {
            'artist': self.name,
            'chickens_drawn': self.chickens_drawn,
            'expertise_level': 'Beginner' if self.chickens_drawn < 5 else 'Expert'
        }

def demonstrate_advanced_features():
    """
    Demonstrate all the advanced chicken art features.
    """
    print("=" * 60)
    print("🎨 DAY 1: ADVANCED CHICKEN ART SOLUTIONS")
    print("=" * 60)
    print()
    
    # Create a chicken artist
    artist = ChickenArtist("CodeChick")
    
    # Different chicken variations
    artist.draw_parametric_chicken("small", "simple")
    artist.draw_parametric_chicken("medium", "classic") 
    artist.draw_parametric_chicken("large", "fancy")
    
    # Special effects
    artist.draw_rainbow_chicken()
    artist.generate_random_chicken()
    
    # Show statistics
    stats = artist.get_stats()
    print("📊 Artist Statistics:")
    print(f"   👨‍🎨 Artist: {stats['artist']}")
    print(f"   🐔 Chickens drawn: {stats['chickens_drawn']}")
    print(f"   🏆 Level: {stats['expertise_level']}")
    print()
    
    # Optional animation (commented out by default)
    # Uncomment the next line to see animation
    # artist.draw_animated_chicken()
    
    print("🎉 Advanced chicken art complete!")
    print("💡 Try modifying the class to add your own features!")

if __name__ == "__main__":
    demonstrate_advanced_features()

"""
📚 ADVANCED LEARNING NOTES:

1. OBJECT-ORIENTED PROGRAMMING:
   - Classes group related functions and data together
   - self refers to the current instance of the class
   - __init__ is the constructor (runs when creating an object)
   - Methods are functions inside a class

2. STRING FORMATTING:
   - f"text {variable}" is an f-string (Python 3.6+)
   - Useful for inserting variables into text
   - More readable than "text " + variable

3. ANSI COLOR CODES:
   - \\033[93m makes text yellow
   - \\033[0m resets to normal color
   - Works in most terminals

4. ERROR HANDLING:
   - try/except blocks catch errors gracefully
   - KeyboardInterrupt catches Ctrl+C

5. IMPORTS:
   - import brings in external functionality
   - random module for random numbers
   - time module for delays

6. LISTS AND RANDOM:
   - Lists store multiple values: [1, 2, 3]
   - random.choice() picks random item from list

7. PRIVATE METHODS:
   - Methods starting with _ are "private"
   - Helps organize code into smaller pieces

💭 ADVANCED REFLECTION:
- How does OOP make code more organized?
- What other features could you add to the ChickenArtist class?
- How would you extend this to draw other animals?
- What real-world problems could this approach solve?

🚀 CHALLENGE EXTENSIONS:
- Add a method to save chickens to a file
- Create different chicken breeds with unique characteristics
- Add sound effects (using system beeps)
- Build a chicken farm with multiple chickens
- Add user input to customize chicken features
"""