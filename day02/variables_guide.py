#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📦 Variables Guide - Day 2
Goorm AI Track 7th - October 30, 2025

Comprehensive guide to Python variables
"""

# =============================================================================
# 📚 VARIABLE BASICS REVIEW
# =============================================================================

print("=== Variable Basics ===")

# Creating variables
name = "Tony Lee"
age = 30
height = 175.5
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}cm")
print(f"Is Student: {is_student}")

# =============================================================================
# 🏷️ VARIABLE NAMING CONVENTIONS
# =============================================================================

print("\n=== Variable Naming Conventions ===")

# ✅ Good variable names (PEP 8 style)
student_name = "이병남"           # Snake case for variables
course_name = "AI Track 7th"     # Descriptive names
total_students = 17              # Clear purpose
is_team_leader = True            # Boolean with is_ prefix

# ❌ Bad variable names (avoid these)
# n = "Tony"                     # Too short, unclear
# StudentName = "Tony"           # CamelCase (use for classes)
# student-name = "Tony"          # Hyphens not allowed
# 2students = 17                 # Can't start with number
# class = "AI Track"             # Reserved keyword

print("✅ Good naming examples:")
print(f"student_name: {student_name}")
print(f"course_name: {course_name}")
print(f"total_students: {total_students}")
print(f"is_team_leader: {is_team_leader}")

# =============================================================================
# 🔄 VARIABLE REASSIGNMENT
# =============================================================================

print("\n=== Variable Reassignment ===")

# Variables can change type and value
progress = 0
print(f"Initial progress: {progress} (type: {type(progress).__name__})")

progress = 50.5
print(f"Updated progress: {progress} (type: {type(progress).__name__})")

progress = "Almost done!"
print(f"Final progress: {progress} (type: {type(progress).__name__})")

# =============================================================================
# 📖 MULTIPLE ASSIGNMENT
# =============================================================================

print("\n=== Multiple Assignment ===")

# Multiple variables in one line
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Same value to multiple variables
a = b = c = 100
print(f"a={a}, b={b}, c={c}")

# Swapping variables
first = "Hello"
second = "World"
print(f"Before swap: first='{first}', second='{second}'")

first, second = second, first
print(f"After swap: first='{first}', second='{second}'")

# Unpacking lists/tuples
team_members = ["이병남", "장수민", "허지호"]
leader, member1, member2 = team_members
print(f"Leader: {leader}, Members: {member1}, {member2}")

# =============================================================================
# 🌍 VARIABLE SCOPE
# =============================================================================

print("\n=== Variable Scope ===")

# Global variable
global_var = "I'm global!"

def function_example():
    # Local variable
    local_var = "I'm local!"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")
    
    # Modifying global variable
    global global_var
    global_var = "Modified global!"

print(f"Before function - Global: {global_var}")
function_example()
print(f"After function - Global: {global_var}")

# =============================================================================
# 🏷️ CONSTANTS (CONVENTION)
# =============================================================================

print("\n=== Constants (Convention) ===")

# Python doesn't have true constants, but we use ALL_CAPS by convention
PI = 3.14159
MAX_STUDENTS = 17
TEAM_NAME = "AI-ACE"
API_URL = "https://api.example.com"

print(f"Pi: {PI}")
print(f"Max students: {MAX_STUDENTS}")
print(f"Team: {TEAM_NAME}")
print(f"API URL: {API_URL}")

# =============================================================================
# 🔍 VARIABLE INTROSPECTION
# =============================================================================

print("\n=== Variable Introspection ===")

sample_var = "Hello, AI Track!"

# Check type
print(f"Type: {type(sample_var)}")
print(f"Type name: {type(sample_var).__name__}")

# Check if variable exists
print(f"'sample_var' exists: {'sample_var' in locals()}")
print(f"'nonexistent_var' exists: {'nonexistent_var' in locals()}")

# Get variable info
print(f"Variable ID: {id(sample_var)}")
print(f"Variable length: {len(sample_var)}")

# =============================================================================
# 📚 VARIABLE MEMORY MANAGEMENT
# =============================================================================

print("\n=== Memory Management ===")

# Small integers are cached
a = 100
b = 100
print(f"a is b: {a is b}")  # True for small integers

# Larger integers are not cached
x = 1000000
y = 1000000
print(f"x is y: {x is y}")  # May be False

# String interning
str1 = "hello"
str2 = "hello"
print(f"str1 is str2: {str1 is str2}")  # True for simple strings

# =============================================================================
# 🎯 PRACTICAL EXAMPLES
# =============================================================================

print("\n=== Practical Examples ===")

# Example 1: Student information system
print("📚 Student Information System:")

students = {
    "student_id": "2025001",
    "student_name": "이병남",
    "student_email": "onofftony@gmail.com",
    "course_name": "생성AI 7회차",
    "team_name": "AI-ACE",
    "enrollment_date": "2025-10-29"
}

for key, value in students.items():
    print(f"  {key.replace('_', ' ').title()}: {value}")

# Example 2: Configuration variables
print("\n⚙️ Configuration Settings:")

# Development settings
DEBUG_MODE = True
MAX_RETRY_COUNT = 3
DEFAULT_TIMEOUT = 30.0
LOG_LEVEL = "INFO"

config_vars = {
    "Debug Mode": DEBUG_MODE,
    "Max Retries": MAX_RETRY_COUNT,
    "Timeout": f"{DEFAULT_TIMEOUT}s",
    "Log Level": LOG_LEVEL
}

for setting, value in config_vars.items():
    status = "✅" if isinstance(value, bool) and value else "⚙️"
    print(f"  {status} {setting}: {value}")

# Example 3: Counter with increment
print("\n📊 Progress Counter:")

progress_counter = 0
total_tasks = 5

for task_num in range(1, total_tasks + 1):
    progress_counter += 1
    percentage = (progress_counter / total_tasks) * 100
    print(f"  Task {task_num} completed - Progress: {percentage:.1f}%")

# =============================================================================
# 🔧 VARIABLE BEST PRACTICES
# =============================================================================

print("\n=== Variable Best Practices ===")

print("✅ DO:")
print("  • Use descriptive names: user_email instead of e")
print("  • Use snake_case for variables")
print("  • Use ALL_CAPS for constants")
print("  • Initialize variables before use")
print("  • Use meaningful prefixes: is_active, has_permission")

print("\n❌ DON'T:")
print("  • Use single letters (except for loops)")
print("  • Use reserved keywords")
print("  • Mix naming conventions")
print("  • Use ambiguous abbreviations")

# =============================================================================
# 🏁 SUMMARY
# =============================================================================

print("\n=== Variables Summary ===")
print("🎯 Key Concepts Learned:")
print("  • Variable naming conventions (snake_case)")
print("  • Variable reassignment and type flexibility")
print("  • Multiple assignment and unpacking")
print("  • Variable scope (global vs local)")
print("  • Constants by convention (ALL_CAPS)")
print("  • Variable introspection and memory")
print("  • Best practices and common pitfalls")

print(f"\n📊 Variables in current scope: {len(locals())} local variables")

if __name__ == "__main__":
    print("\n🚀 Run this file to explore Python variables!")