#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
✅ Exercise Solutions - Day 2
Goorm AI Track 7th - October 30, 2025

Solutions to practice exercises - Check your answers here!
Try the exercises first before looking at these solutions.
"""

# =============================================================================
# ✅ SOLUTION 1: ADVANCED PRINT METHODS
# =============================================================================

print("✅ SOLUTION 1: Advanced Print Methods")
print("=" * 50)

print("Task 1: Formatted student report")
name = "이병남"
age = 25
course = "AI Track 7th"
gpa = 3.85

# Solution using f-string
print(f"Student: {name} | Age: {age} | Course: {course} | GPA: {gpa}")

print("\n" + "-"*30)
print("Task 2: Colored output")

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

print(f"{GREEN}SUCCESS{RESET} {RED}ERROR{RESET} {BLUE}INFO{RESET}")

print("\n" + "-"*30)
print("Task 3: Custom separators and endings")

fruits = ["apple", "banana", "cherry"]
print(*fruits, sep="->", end=" (fruits)\n")

# =============================================================================
# ✅ SOLUTION 2: VARIABLES AND SCOPE
# =============================================================================

print("\n\n✅ SOLUTION 2: Variables and Scope")
print("=" * 50)

global_counter = 0

def increment_counter():
    """Increment the global counter"""
    global global_counter
    global_counter += 1

def local_variable_demo():
    """Demonstrate local vs global variables"""
    local_var = "I'm local"
    print(f"Local variable: {local_var}")
    print(f"Global counter: {global_counter}")

print("Task 1: Counter function")
print(f"Initial counter: {global_counter}")
increment_counter()
print(f"After increment: {global_counter}")

print("\nTask 2: Variable scope")
local_variable_demo()

# =============================================================================
# ✅ SOLUTION 3: DATA TYPE MANIPULATION
# =============================================================================

print("\n\n✅ SOLUTION 3: Data Type Manipulation")
print("=" * 50)

print("Task 1: Student Database Operations")

students = [
    {"name": "이병남", "age": 25, "grades": [90, 85, 92]},
    {"name": "장수민", "age": 23, "grades": [88, 90, 87]},
    {"name": "허지호", "age": 24, "grades": [92, 89, 91]}
]

# 1. Add new student
students.append({"name": "정수민", "age": 22, "grades": [94, 88, 90]})

# 2. Calculate average grades
print("Student averages:")
for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    student["average"] = avg  # Store for later use
    print(f"  {student['name']}: {avg:.1f}")

# 3. Find highest average
best_student = max(students, key=lambda s: s["average"])
print(f"\nHighest average: {best_student['name']} ({best_student['average']:.1f})")

print("\n" + "-"*30)
print("Task 2: Data Type Conversion")

mixed_data = ["25", "3.14", "True", "100", "False", "2.71"]

integers = []
floats = []
booleans = []

for item in mixed_data:
    # Try integer conversion first
    try:
        if '.' not in item and item not in ['True', 'False']:
            integers.append(int(item))
        elif item in ['True', 'False']:
            booleans.append(item == 'True')
        else:
            floats.append(float(item))
    except ValueError:
        print(f"Could not convert: {item}")

print(f"Integers: {integers}")
print(f"Floats: {floats}")
print(f"Booleans: {booleans}")

# =============================================================================
# ✅ SOLUTION 4: COLLECTIONS MASTERY
# =============================================================================

print("\n\n✅ SOLUTION 4: Collections Mastery")
print("=" * 50)

print("Task 1: Set Operations - Skills Analysis")

team_a_skills = {"Python", "JavaScript", "AI", "Machine Learning"}
team_b_skills = {"Python", "Java", "AI", "Data Science", "React"}
team_c_skills = {"Python", "C++", "AI", "Computer Vision"}

# 1. Skills common to all teams
common_skills = team_a_skills & team_b_skills & team_c_skills
print(f"Common to all teams: {common_skills}")

# 2. Skills unique to each team
unique_a = team_a_skills - team_b_skills - team_c_skills
unique_b = team_b_skills - team_a_skills - team_c_skills
unique_c = team_c_skills - team_a_skills - team_b_skills

print(f"Unique to Team A: {unique_a}")
print(f"Unique to Team B: {unique_b}")
print(f"Unique to Team C: {unique_c}")

# 3. Total unique skills
all_skills = team_a_skills | team_b_skills | team_c_skills
print(f"Total unique skills: {all_skills}")
print(f"Skills count: {len(all_skills)}")

# 4. Recommendations for Team A
other_teams_skills = team_b_skills | team_c_skills
recommendations = other_teams_skills - team_a_skills
print(f"Team A should learn: {recommendations}")

print("\n" + "-"*30)
print("Task 2: Dictionary Manipulation - Grade Management")

gradebook = {
    "이병남": {"midterm": 90, "final": 92, "project": 88},
    "장수민": {"midterm": 88, "final": 87, "project": 90},
    "허지호": {"midterm": 92, "final": 91, "project": 89}
}

# 1. Calculate final grades
def calculate_final_grade(grades):
    """Calculate weighted final grade"""
    return (grades["midterm"] * 0.3 + 
            grades["final"] * 0.4 + 
            grades["project"] * 0.3)

def get_letter_grade(score):
    """Convert numeric score to letter grade"""
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

print("Final grades:")
final_scores = {}

for student, grades in gradebook.items():
    final_score = calculate_final_grade(grades)
    letter_grade = get_letter_grade(final_score)
    final_scores[student] = final_score
    
    print(f"  {student}: {final_score:.1f} ({letter_grade})")

# 3. Class average
class_average = sum(final_scores.values()) / len(final_scores)
print(f"\nClass average: {class_average:.1f}")

# 4. Highest and lowest
highest_student = max(final_scores, key=final_scores.get)
lowest_student = min(final_scores, key=final_scores.get)

print(f"Highest: {highest_student} ({final_scores[highest_student]:.1f})")
print(f"Lowest: {lowest_student} ({final_scores[lowest_student]:.1f})")

# =============================================================================
# ✅ SOLUTION 5: REAL-WORLD APPLICATION
# =============================================================================

print("\n\n✅ SOLUTION 5: Real-World Application")
print("=" * 50)

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

def display_team_info(members):
    """Display formatted team information"""
    print("🏆 AI-ACE Team Information:")
    print("-" * 40)
    
    for i, member in enumerate(members, 1):
        status = "✅ Active" if member["active"] else "❌ Inactive"
        skills_str = ", ".join(member["skills"])
        projects_str = ", ".join(member["projects"])
        
        print(f"{i}. {member['name']} ({member['role']})")
        print(f"   📧 {member['email']}")
        print(f"   🛠️  Skills: {skills_str}")
        print(f"   📋 Projects: {projects_str}")
        print(f"   📊 Status: {status}")
        print()

def add_new_member(members, name, role, email, skills):
    """Add a new team member"""
    new_member = {
        "name": name,
        "role": role,
        "email": email,
        "skills": skills if isinstance(skills, list) else [skills],
        "projects": [],
        "active": True
    }
    members.append(new_member)
    print(f"✅ Added {name} to the team!")

def find_members_by_skill(members, skill):
    """Find all members who have a specific skill"""
    return [member for member in members if skill in member["skills"]]

def get_team_statistics(members):
    """Calculate team statistics"""
    total_members = len(members)
    active_members = len([m for m in members if m["active"]])
    
    # Collect all skills
    all_skills = set()
    for member in members:
        all_skills.update(member["skills"])
    
    # Count projects
    total_projects = sum(len(member["projects"]) for member in members)
    
    print("📊 Team Statistics:")
    print(f"  👥 Total members: {total_members}")
    print(f"  ✅ Active members: {active_members}")
    print(f"  🛠️  Unique skills: {len(all_skills)}")
    print(f"  📋 Total projects: {total_projects}")
    print(f"  🔧 Skills list: {', '.join(sorted(all_skills))}")

def assign_project(members, member_name, project):
    """Assign a new project to a team member"""
    for member in members:
        if member["name"] == member_name:
            member["projects"].append(project)
            print(f"✅ Assigned '{project}' to {member_name}")
            return
    print(f"❌ Member '{member_name}' not found")

# Test the functions
print("=== AI-ACE Team Management System ===")

display_team_info(team_members)

print("\n📊 Statistics:")
get_team_statistics(team_members)

print("\n🔍 Finding Python developers:")
python_devs = find_members_by_skill(team_members, "Python")
for dev in python_devs:
    print(f"  • {dev['name']}")

print("\n➕ Adding new member:")
add_new_member(team_members, "정수민", "개발자", "user@example.com", ["Python", "Data Science"])

print("\n📋 Assigning project:")
assign_project(team_members, "정수민", "Machine Learning Model")

# =============================================================================
# ✅ BONUS CHALLENGE SOLUTIONS
# =============================================================================

print("\n\n✅ BONUS CHALLENGE SOLUTIONS")
print("=" * 50)

print("Challenge 1: Data Type Detective")

import json

def smart_convert(value_str):
    """Intelligently convert string to most appropriate type"""
    value_str = value_str.strip()
    
    # Handle None
    if value_str.lower() == 'none':
        return None
    
    # Handle booleans
    if value_str.lower() == 'true':
        return True
    elif value_str.lower() == 'false':
        return False
    
    # Try integer
    try:
        if '.' not in value_str:
            return int(value_str)
    except ValueError:
        pass
    
    # Try float
    try:
        return float(value_str)
    except ValueError:
        pass
    
    # Try list/dict with eval (dangerous in real apps!)
    if value_str.startswith('[') or value_str.startswith('{'):
        try:
            return eval(value_str)  # WARNING: Don't use eval in production!
        except:
            pass
    
    # Default to string
    return value_str

mysterious_data = [
    "42",           
    "3.14159",      
    "True",         
    "[1, 2, 3]",    
    "{'a': 1}",     
    "None",         
    "not_a_number", 
]

print("Smart conversion results:")
for data in mysterious_data:
    result = smart_convert(data)
    print(f"'{data}' → {result} ({type(result).__name__})")

print("\n" + "-"*30)
print("Challenge 2: Collection Performance")

import time

# Generate test data
test_data = list(range(10000))
search_target = 9999

# List vs Set search performance
print("🔍 Search Performance Comparison:")

# List search
start_time = time.time()
found_in_list = search_target in test_data
list_time = time.time() - start_time

# Set search
test_set = set(test_data)
start_time = time.time()
found_in_set = search_target in test_set
set_time = time.time() - start_time

print(f"List search: {list_time:.6f} seconds")
print(f"Set search: {set_time:.6f} seconds")
print(f"Set is {list_time/set_time:.0f}x faster for searching!")

# Append vs Add performance
print("\n📝 Addition Performance Comparison:")

# List append
test_list = []
start_time = time.time()
for i in range(1000):
    test_list.append(i)
list_append_time = time.time() - start_time

# Set add
test_set = set()
start_time = time.time()
for i in range(1000):
    test_set.add(i)
set_add_time = time.time() - start_time

print(f"List append (1000 items): {list_append_time:.6f} seconds")
print(f"Set add (1000 items): {set_add_time:.6f} seconds")

if list_append_time > set_add_time:
    print(f"Set is {list_append_time/set_add_time:.1f}x faster for adding!")
else:
    print(f"List is {set_add_time/list_append_time:.1f}x faster for adding!")

# =============================================================================
# 📚 EXPLANATION OF SOLUTIONS
# =============================================================================

print("\n\n📚 SOLUTION EXPLANATIONS")
print("=" * 50)

explanations = [
    "🎯 F-strings (f'text {variable}') are the fastest and most readable formatting method",
    "🌈 ANSI codes work in most terminals but may not work in all environments",
    "📊 Global variables need the 'global' keyword to modify them inside functions",
    "🔧 List comprehensions and generator expressions are more Pythonic than loops",
    "⚡ Sets use hash tables, making 'in' operations O(1) vs O(n) for lists",
    "📋 Dictionary.get() is safer than dict[key] as it won't raise KeyError",
    "🛡️ Always handle exceptions when converting types in real applications",
    "🎲 eval() is dangerous - never use it with untrusted input!",
    "📈 For large datasets, choose data structures based on your operations",
    "🤝 Working with teammates helps you learn different approaches to problems"
]

for i, explanation in enumerate(explanations, 1):
    print(f"{i:2}. {explanation}")

# =============================================================================
# 🎯 REFLECTION ANSWERS
# =============================================================================

print("\n\n🎯 REFLECTION ANSWERS")
print("=" * 50)

print("1. When to use tuple vs list:")
print("   • Use tuples for data that shouldn't change (coordinates, RGB values)")
print("   • Use tuples as dictionary keys (they're hashable)")
print("   • Use tuples for function returns with multiple values")
print("   • Use lists for data that needs modification")

print("\n2. '==' vs 'is':")
print("   • '==' compares values")
print("   • 'is' compares object identity (memory location)")
print("   • Use 'is' only for None, True, False")

print("\n3. Set vs list for unique items:")
print("   • Sets automatically handle uniqueness")
print("   • Sets have O(1) lookup time vs O(n) for lists")
print("   • Sets support mathematical operations (union, intersection)")

print("\n4. Python truthiness:")
print("   • False: 0, 0.0, '', [], {}, set(), None, False")
print("   • True: Everything else!")
print("   • Empty collections are falsy, non-empty are truthy")

print("\n5. F-string benefits:")
print("   • Fastest string formatting method")
print("   • Most readable and concise")
print("   • Supports expressions inside {}")
print("   • Available in Python 3.6+")

print("\n6. Global vs local variables:")
print("   • Prefer local variables for better code organization")
print("   • Use global sparingly (constants, configuration)")
print("   • Local variables are faster and safer")

print("\n7. Handling conversion errors:")
print("   • Use try/except blocks")
print("   • Provide default values")
print("   • Validate input before conversion")
print("   • Log errors for debugging")

print("\n8. Checking dictionary keys:")
print("   • Use 'key in dict' (fastest)")
print("   • Use dict.get(key, default)")
print("   • Avoid dict[key] without checking first")

if __name__ == "__main__":
    print("\n🎉 Great job completing the exercises!")
    print("🚀 You've mastered Day 2 concepts!")
    print("🤝 Share your solutions with teammates and compare approaches!")