#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎯 Practice Exercises - Day 2
Goorm AI Track 7th - October 30, 2025

Hands-on exercises for advanced print methods, variables, and data types
Complete these exercises to reinforce your learning!
"""

# =============================================================================
# 🏋️ EXERCISE 1: ADVANCED PRINT METHODS
# =============================================================================

print("🏋️ EXERCISE 1: Advanced Print Methods")
print("=" * 50)

# TODO: Fix these print statements to match the expected output
print("Task 1: Create a formatted student report")
print("Expected output:")
print("Student: 이병남 | Age: 25 | Course: AI Track 7th | GPA: 3.85")
print("\nYour code:")
# Write your f-string here
name = "이병남"
age = 25
course = "AI Track 7th"
gpa = 3.85
# YOUR CODE HERE:


print("\n" + "-"*50)
print("Task 2: Create colored output (if terminal supports ANSI)")
print("Expected: Green 'SUCCESS', Red 'ERROR', Blue 'INFO'")
print("\nYour code:")
# Use ANSI codes to create colored text
# YOUR CODE HERE:


print("\n" + "-"*50)
print("Task 3: Print with custom separators and endings")
print("Expected: 'apple->banana->cherry' followed by ' (fruits)'")
print("\nYour code:")
fruits = ["apple", "banana", "cherry"]
# Use print() with sep and end parameters
# YOUR CODE HERE:


# =============================================================================
# 🏋️ EXERCISE 2: VARIABLES AND SCOPE
# =============================================================================

print("\n\n🏋️ EXERCISE 2: Variables and Scope")
print("=" * 50)

# Global variable
global_counter = 0

def increment_counter():
    """Fix this function to properly increment the global counter"""
    # YOUR CODE HERE: Make this function increment global_counter
    pass

def local_variable_demo():
    """Demonstrate local vs global variables"""
    local_var = "I'm local"
    # YOUR CODE HERE: Print both local_var and global_counter
    pass

print("Task 1: Fix the counter function")
print(f"Initial counter: {global_counter}")
increment_counter()
print(f"After increment: {global_counter}")  # Should be 1

print("\nTask 2: Variable scope demonstration")
local_variable_demo()

# =============================================================================
# 🏋️ EXERCISE 3: DATA TYPE MANIPULATION
# =============================================================================

print("\n\n🏋️ EXERCISE 3: Data Type Manipulation")
print("=" * 50)

print("Task 1: Student Database Operations")
# Create a list of student dictionaries
students = [
    {"name": "이병남", "age": 25, "grades": [90, 85, 92]},
    {"name": "장수민", "age": 23, "grades": [88, 90, 87]},
    {"name": "허지호", "age": 24, "grades": [92, 89, 91]}
]

# YOUR CODE HERE:
# 1. Add a new student: {"name": "정수민", "age": 22, "grades": [94, 88, 90]}
# 2. Calculate and print average grade for each student
# 3. Find the student with the highest average grade


print("\n" + "-"*30)
print("Task 2: Data Type Conversion Challenge")

# Given mixed data, convert and organize it
mixed_data = ["25", "3.14", "True", "100", "False", "2.71"]

# YOUR CODE HERE:
# 1. Create separate lists for integers, floats, and booleans
# 2. Convert string representations to appropriate types
# 3. Print each list with proper formatting

integers = []
floats = []
booleans = []

print(f"Integers: {integers}")
print(f"Floats: {floats}")
print(f"Booleans: {booleans}")

# =============================================================================
# 🏋️ EXERCISE 4: COLLECTIONS MASTERY
# =============================================================================

print("\n\n🏋️ EXERCISE 4: Collections Mastery")
print("=" * 50)

print("Task 1: Set Operations - Skills Analysis")

# Team skills
team_a_skills = {"Python", "JavaScript", "AI", "Machine Learning"}
team_b_skills = {"Python", "Java", "AI", "Data Science", "React"}
team_c_skills = {"Python", "C++", "AI", "Computer Vision"}

# YOUR CODE HERE:
# 1. Find skills common to all teams
# 2. Find skills unique to each team
# 3. Find total unique skills across all teams
# 4. Recommend skills that team_a should learn (skills others have but team_a doesn't)


print("\n" + "-"*30)
print("Task 2: Dictionary Manipulation - Grade Management")

# Grade book
gradebook = {
    "이병남": {"midterm": 90, "final": 92, "project": 88},
    "장수민": {"midterm": 88, "final": 87, "project": 90},
    "허지호": {"midterm": 92, "final": 91, "project": 89}
}

# YOUR CODE HERE:
# 1. Calculate final grade for each student (midterm 30%, final 40%, project 30%)
# 2. Add letter grades (A: 90+, B: 80+, C: 70+, D: 60+, F: <60)
# 3. Find class average
# 4. Find highest and lowest scoring students


# =============================================================================
# 🏋️ EXERCISE 5: REAL-WORLD APPLICATION
# =============================================================================

print("\n\n🏋️ EXERCISE 5: Real-World Application")
print("=" * 50)

print("Task: AI-ACE Team Management System")

# Team member data
team_members = [
    {
        "name": "이병남",
        "role": "팀장",
        "email": "onofftony@gmail.com",
        "skills": ["Python", "AI", "Leadership"],
        "projects": ["OCR System", "RAG Implementation"],
        "active": True
    },
    {
        "name": "장수민",
        "role": "개발자",
        "email": "wkdalsl629@gmail.com",
        "skills": ["Python", "Web Development"],
        "projects": ["Frontend Development"],
        "active": True
    },
    {
        "name": "허지호",
        "role": "개발자",
        "email": "gjwlgh0928@gmail.com",
        "skills": ["Python", "Backend"],
        "projects": ["API Development"],
        "active": True
    }
]

# YOUR CODE HERE: Implement these functions

def display_team_info(members):
    """Display formatted team information"""
    pass

def add_new_member(members, name, role, email, skills):
    """Add a new team member"""
    pass

def find_members_by_skill(members, skill):
    """Find all members who have a specific skill"""
    pass

def get_team_statistics(members):
    """Calculate team statistics (total members, skills distribution, etc.)"""
    pass

def assign_project(members, member_name, project):
    """Assign a new project to a team member"""
    pass

# Test your functions:
print("=== AI-ACE Team Management System ===")

# Example usage (uncomment when you implement the functions):
# display_team_info(team_members)
# python_developers = find_members_by_skill(team_members, "Python")
# print(f"Python developers: {[m['name'] for m in python_developers]}")

# =============================================================================
# 🎯 BONUS CHALLENGES
# =============================================================================

print("\n\n🎯 BONUS CHALLENGES")
print("=" * 50)

print("Challenge 1: Data Type Detective")
print("Given mysterious data, determine and convert types appropriately")

mysterious_data = [
    "42",           # Could be int
    "3.14159",      # Could be float  
    "True",         # Could be bool
    "[1, 2, 3]",    # Could be list
    "{'a': 1}",     # Could be dict
    "None",         # Could be None
    "not_a_number", # Invalid for numeric conversion
]

# YOUR CODE HERE:
# Create a function that takes a string and tries to convert it to the most appropriate type
# Handle conversion errors gracefully

def smart_convert(value_str):
    """Intelligently convert string to most appropriate type"""
    # Implement your logic here
    pass

# Test your converter
for data in mysterious_data:
    result = smart_convert(data)
    print(f"'{data}' → {result} ({type(result).__name__})")

print("\n" + "-"*30)
print("Challenge 2: Collection Performance")
print("Compare performance of different data structures")

import time

# Generate test data
test_data = list(range(10000))

# YOUR CODE HERE:
# 1. Time how long it takes to find an element in a list vs set
# 2. Time how long it takes to append to a list vs add to a set
# 3. Compare memory usage if possible

# Example timing structure:
# start_time = time.time()
# # Your operation here
# end_time = time.time()
# print(f"Operation took {end_time - start_time:.4f} seconds")

# =============================================================================
# 🏁 EXERCISE SOLUTIONS (HIDDEN - TRY FIRST!)
# =============================================================================

print("\n\n🏁 SOLUTIONS")
print("=" * 50)
print("💡 Try to solve the exercises above before looking at solutions!")
print("📁 Solutions will be provided in a separate file: exercise_solutions.py")

# =============================================================================
# 📝 REFLECTION QUESTIONS
# =============================================================================

print("\n\n📝 REFLECTION QUESTIONS")
print("=" * 50)
print("Answer these questions to reinforce your understanding:")
print()
print("1. When would you use a tuple instead of a list?")
print("2. What's the difference between '==' and 'is' when comparing variables?")
print("3. Why might you choose a set over a list for storing unique items?")
print("4. How does Python determine the truthiness of different data types?")
print("5. What are the benefits of using f-strings over other formatting methods?")
print("6. When should you use global variables vs local variables?")
print("7. How would you handle type conversion errors in a real application?")
print("8. What's the most efficient way to check if a key exists in a dictionary?")
print()
print("💭 Discuss these with your teammates and compare your answers!")

if __name__ == "__main__":
    print("\n🚀 Complete these exercises to master Day 2 concepts!")
    print("🤝 Work with your AI-ACE teammates and help each other learn!")