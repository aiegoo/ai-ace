#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🖨️ Advanced Print Methods - Day 2
Goorm AI Track 7th - October 30, 2025

Advanced techniques for the print() function in Python
"""

# =============================================================================
# 📚 BASIC PRINT REVIEW
# =============================================================================

print("=== Basic Print Review ===")
print("Hello, World!")
print("This is a simple print statement")
print()  # Empty line for spacing

# =============================================================================
# 🎨 ADVANCED PRINT FORMATTING
# =============================================================================

print("=== Advanced Print Formatting ===")

# 1. Multiple arguments
print("Name:", "Tony Lee", "Course:", "AI Track 7th")

# 2. Custom separator
print("Apple", "Banana", "Cherry", sep=" | ")
print("2025", "10", "30", sep="-")

# 3. Custom end character (instead of newline)
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" Done!")

# 4. Combining sep and end
print("Processing", "data", "please", "wait", sep="...", end="!\n")

# =============================================================================
# 🔤 STRING FORMATTING METHODS
# =============================================================================

print("\n=== String Formatting Methods ===")

# Method 1: % formatting (old style)
name = "Tony Lee"
age = 30
course = "AI Track 7th"

print("Hello, I'm %s, %d years old, studying %s" % (name, age, course))

# Method 2: .format() method
print("Hello, I'm {}, {} years old, studying {}".format(name, age, course))

# Named placeholders with .format()
print("Hello, I'm {name}, {age} years old, studying {course}".format(
    name=name, age=age, course=course))

# Method 3: f-strings (modern and recommended)
print(f"Hello, I'm {name}, {age} years old, studying {course}")

# =============================================================================
# 📊 ADVANCED F-STRING FORMATTING
# =============================================================================

print("\n=== Advanced F-String Formatting ===")

# Number formatting
pi = 3.14159265359
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Pi to 4 decimal places: {pi:.4f}")

# Width and alignment
team_name = "AI-ACE"
print(f"Team: {team_name:>10}")  # Right align in 10 chars
print(f"Team: {team_name:<10}")  # Left align in 10 chars  
print(f"Team: {team_name:^10}")  # Center align in 10 chars

# Padding with characters
print(f"Team: {team_name:*^15}")  # Center with * padding

# Number formatting with commas
big_number = 1234567
print(f"Big number: {big_number:,}")

# Percentage formatting
score = 0.856
print(f"Score: {score:.1%}")

# =============================================================================
# 🌈 PRINT WITH COLORS (ANSI Codes)
# =============================================================================

print("\n=== Colored Output ===")

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'  # Reset to default

print(f"{RED}This is red text{RESET}")
print(f"{GREEN}This is green text{RESET}")
print(f"{BLUE}This is blue text{RESET}")
print(f"{YELLOW}This is yellow text{RESET}")

# Combining colors with formatting
team_members = ["이병남", "장수민", "허지호", "이상준", "고준"]
print(f"\n{CYAN}🎯 AI-ACE Team Members:{RESET}")
for i, member in enumerate(team_members, 1):
    print(f"{GREEN}{i:2d}. {member}{RESET}")

# =============================================================================
# 📝 PRINT TO FILES
# =============================================================================

print("\n=== Print to Files ===")

# Print to file instead of console
with open("day2_output.txt", "w", encoding="utf-8") as f:
    print("This goes to a file!", file=f)
    print(f"Team: {team_name}", file=f)
    print(f"Date: October 30, 2025", file=f)

print("✅ Output saved to 'day2_output.txt'")

# =============================================================================
# 🔧 PRACTICAL EXAMPLES
# =============================================================================

print("\n=== Practical Examples ===")

# Progress bar simulation
def print_progress_bar(percentage):
    bar_length = 20
    filled_length = int(percentage * bar_length // 100)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    print(f"\rProgress: [{bar}] {percentage}%", end="")

print("Simulating progress:")
import time
for i in range(0, 101, 10):
    print_progress_bar(i)
    time.sleep(0.1)
print()  # New line after progress

# Table formatting
print("\n📊 Student Progress Table:")
print(f"{'Name':<12} {'Course':<15} {'Progress':<10}")
print("-" * 40)
students = [
    ("이병남", "AI Track 7th", "100%"),
    ("장수민", "AI Track 7th", "95%"),
    ("허지호", "AI Track 7th", "90%")
]

for name, course, progress in students:
    print(f"{name:<12} {course:<15} {progress:<10}")

# =============================================================================
# 🎯 DEBUG PRINTING
# =============================================================================

print("\n=== Debug Printing ===")

# Debug with variable names (Python 3.8+)
x = 42
y = "AI Track"
print(f"Debug: {x=}, {y=}")

# Multi-line debug output
data = {"name": "Tony", "team": "AI-ACE", "day": 2}
print("Debug info:")
for key, value in data.items():
    print(f"  {key}: {value}")

# =============================================================================
# 🏁 SUMMARY
# =============================================================================

print(f"\n{GREEN}=== Day 2 Print Methods Summary ==={RESET}")
print(f"{CYAN}✅ Learned:{RESET}")
print("  • Advanced print() parameters (sep, end)")
print("  • String formatting methods (%, .format(), f-strings)")
print("  • Number and text alignment")
print("  • Colored output with ANSI codes")
print("  • File output redirection")
print("  • Debug printing techniques")

print(f"\n{YELLOW}🎯 Next: Variables and Data Types!{RESET}")

if __name__ == "__main__":
    print(f"\n{PURPLE}🚀 Run this file to see all examples in action!{RESET}")