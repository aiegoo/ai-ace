#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔢 Data Types Tutorial - Day 2
Goorm AI Track 7th - October 30, 2025

Complete guide to Python data types
"""

# =============================================================================
# 📊 PYTHON DATA TYPES OVERVIEW
# =============================================================================

print("=== Python Data Types Overview ===")
print("📚 Python has several built-in data types:")
print("  • Numbers: int, float, complex")
print("  • Text: str")
print("  • Boolean: bool")
print("  • Sequences: list, tuple, range")
print("  • Mappings: dict")
print("  • Sets: set, frozenset")
print("  • None: NoneType")

# =============================================================================
# 🔢 NUMERIC TYPES
# =============================================================================

print("\n=== Numeric Types ===")

# Integer (int)
age = 25
student_count = 17
print(f"Integer examples: age={age}, student_count={student_count}")
print(f"Type: {type(age).__name__}")

# Float (floating-point)
height = 175.5
pi = 3.14159
gpa = 3.85
print(f"Float examples: height={height}, pi={pi}, gpa={gpa}")
print(f"Type: {type(height).__name__}")

# Complex numbers
complex_num = 3 + 4j
print(f"Complex example: {complex_num}")
print(f"Real part: {complex_num.real}, Imaginary part: {complex_num.imag}")

# Numeric operations
print(f"\nNumeric operations:")
print(f"Addition: 10 + 5 = {10 + 5}")
print(f"Subtraction: 10 - 5 = {10 - 5}")
print(f"Multiplication: 10 * 5 = {10 * 5}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Floor division: 10 // 3 = {10 // 3}")
print(f"Modulus: 10 % 3 = {10 % 3}")
print(f"Exponent: 2 ** 3 = {2 ** 3}")

# =============================================================================
# 📝 STRING TYPE
# =============================================================================

print("\n=== String Type ===")

# String creation
name = "이병남"
course = 'AI Track 7th'
multiline = """This is a
multiline string
for documentation"""

print(f"String examples:")
print(f"  Name: {name} (type: {type(name).__name__})")
print(f"  Course: {course}")
print(f"  Multiline: {repr(multiline)}")

# String methods
sample_text = "  Hello, AI Track 7th!  "
print(f"\nString methods:")
print(f"Original: '{sample_text}'")
print(f"Upper: '{sample_text.upper()}'")
print(f"Lower: '{sample_text.lower()}'")
print(f"Strip: '{sample_text.strip()}'")
print(f"Replace: '{sample_text.replace('AI', 'Artificial Intelligence')}'")
print(f"Length: {len(sample_text)}")

# String indexing and slicing
text = "Python"
print(f"\nString indexing/slicing with '{text}':")
print(f"First character: text[0] = '{text[0]}'")
print(f"Last character: text[-1] = '{text[-1]}'")
print(f"First 3 chars: text[:3] = '{text[:3]}'")
print(f"Last 3 chars: text[-3:] = '{text[-3:]}'")
print(f"Every 2nd char: text[::2] = '{text[::2]}'")

# =============================================================================
# ✅ BOOLEAN TYPE
# =============================================================================

print("\n=== Boolean Type ===")

is_student = True
is_graduated = False
print(f"Boolean examples: is_student={is_student}, is_graduated={is_graduated}")
print(f"Type: {type(is_student).__name__}")

# Boolean operations
print(f"\nBoolean operations:")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# Truthiness in Python
print(f"\nTruthiness examples:")
values_to_test = [0, 1, "", "hello", [], [1, 2], {}, {"key": "value"}, None]
for value in values_to_test:
    print(f"bool({repr(value)}) = {bool(value)}")

# =============================================================================
# 📋 LIST TYPE (MUTABLE SEQUENCE)
# =============================================================================

print("\n=== List Type (Mutable) ===")

# Creating lists
team_members = ["이병남", "장수민", "허지호", "이상준", "고준"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["Tony", 25, True, 3.14]

print(f"Lists examples:")
print(f"  Team: {team_members}")
print(f"  Numbers: {numbers}")
print(f"  Mixed: {mixed_list}")
print(f"Type: {type(team_members).__name__}")

# List operations
print(f"\nList operations:")
print(f"Length: {len(team_members)}")
print(f"First member: {team_members[0]}")
print(f"Last member: {team_members[-1]}")

# Modifying lists (mutable)
team_copy = team_members.copy()
team_copy.append("정수민")
team_copy.insert(1, "새로운 멤버")
removed = team_copy.pop()

print(f"Modified list: {team_copy}")
print(f"Removed member: {removed}")

# List methods
print(f"\nList methods:")
scores = [85, 92, 78, 96, 88]
print(f"Scores: {scores}")
print(f"Max: {max(scores)}")
print(f"Min: {min(scores)}")
print(f"Sum: {sum(scores)}")
print(f"Average: {sum(scores)/len(scores):.1f}")
print(f"Sorted: {sorted(scores)}")

# =============================================================================
# 📦 TUPLE TYPE (IMMUTABLE SEQUENCE)
# =============================================================================

print("\n=== Tuple Type (Immutable) ===")

# Creating tuples
coordinates = (10, 20)
student_info = ("이병남", 25, "AI-ACE", True)
single_tuple = (42,)  # Note the comma for single element

print(f"Tuple examples:")
print(f"  Coordinates: {coordinates}")
print(f"  Student info: {student_info}")
print(f"  Single element: {single_tuple}")
print(f"Type: {type(coordinates).__name__}")

# Tuple operations
print(f"\nTuple operations:")
print(f"Length: {len(student_info)}")
print(f"First element: {student_info[0]}")
print(f"Last element: {student_info[-1]}")

# Tuple unpacking
name, age, team, is_leader = student_info
print(f"Unpacked: name='{name}', age={age}, team='{team}', leader={is_leader}")

# Why use tuples?
print(f"\n📚 Tuples vs Lists:")
print(f"  • Tuples are immutable (can't change)")
print(f"  • Tuples are faster than lists")
print(f"  • Tuples can be dictionary keys")
print(f"  • Use tuples for data that shouldn't change")

# =============================================================================
# 🗂️ DICTIONARY TYPE (KEY-VALUE MAPPING)
# =============================================================================

print("\n=== Dictionary Type (Mapping) ===")

# Creating dictionaries
student = {
    "name": "이병남",
    "age": 25,
    "course": "AI Track 7th",
    "team": "AI-ACE",
    "skills": ["Python", "AI", "Leadership"]
}

print(f"Dictionary example:")
for key, value in student.items():
    print(f"  {key}: {value}")
print(f"Type: {type(student).__name__}")

# Dictionary operations
print(f"\nDictionary operations:")
print(f"Get name: {student['name']}")
print(f"Get age (safe): {student.get('age', 'Unknown')}")
print(f"Get grade (safe): {student.get('grade', 'Not set')}")

# Modifying dictionaries
student['grade'] = 'A+'
student.update({"email": "onofftony@gmail.com", "github": "@aiegoo"})
removed_skill = student['skills'].pop()

print(f"Updated student: {student}")
print(f"Removed skill: {removed_skill}")

# Dictionary methods
print(f"\nDictionary methods:")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items count: {len(student)}")

# =============================================================================
# 🎯 SET TYPE (UNIQUE COLLECTION)
# =============================================================================

print("\n=== Set Type (Unique Collection) ===")

# Creating sets
skills = {"Python", "JavaScript", "AI", "Machine Learning", "Python"}  # Duplicate removed
numbers_set = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates empty dict, not set

print(f"Set examples:")
print(f"  Skills: {skills}")  # Duplicates automatically removed
print(f"  Numbers: {numbers_set}")
print(f"Type: {type(skills).__name__}")

# Set operations
ai_skills = {"Python", "AI", "Machine Learning", "Data Science"}
web_skills = {"Python", "JavaScript", "HTML", "CSS"}

print(f"\nSet operations:")
print(f"AI skills: {ai_skills}")
print(f"Web skills: {web_skills}")
print(f"Intersection (common): {ai_skills & web_skills}")
print(f"Union (all): {ai_skills | web_skills}")
print(f"Difference (AI only): {ai_skills - web_skills}")

# =============================================================================
# 🚫 NONE TYPE
# =============================================================================

print("\n=== None Type ===")

# None represents absence of value
result = None
optional_value = None

print(f"None examples: result={result}, optional_value={optional_value}")
print(f"Type: {type(result).__name__}")

# Common None usage
def get_student_grade(student_id):
    # Simulating database lookup
    if student_id == "2025001":
        return "A+"
    return None  # Student not found

grade = get_student_grade("2025001")
unknown_grade = get_student_grade("9999999")

print(f"Known student grade: {grade}")
print(f"Unknown student grade: {unknown_grade}")
print(f"Checking for None: {unknown_grade is None}")

# =============================================================================
# 🔄 TYPE CONVERSION (CASTING)
# =============================================================================

print("\n=== Type Conversion ===")

# String to number
str_num = "42"
int_val = int(str_num)
float_val = float(str_num)

print(f"String '{str_num}' converted:")
print(f"  To int: {int_val} (type: {type(int_val).__name__})")
print(f"  To float: {float_val} (type: {type(float_val).__name__})")

# Number to string
num = 123
str_val = str(num)
print(f"Number {num} to string: '{str_val}' (type: {type(str_val).__name__})")

# List/tuple conversion
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)

print(f"List to tuple: {my_list} → {my_tuple}")
print(f"Tuple to list: {my_tuple} → {back_to_list}")

# String to list
text = "Hello"
char_list = list(text)
print(f"String to list: '{text}' → {char_list}")

# Error handling for conversion
print(f"\nSafe conversion examples:")
test_values = ["42", "3.14", "hello", "True"]

for value in test_values:
    try:
        as_int = int(value)
        print(f"  '{value}' → int: {as_int}")
    except ValueError:
        print(f"  '{value}' → int: Cannot convert!")

# =============================================================================
# 🎯 PRACTICAL EXAMPLES
# =============================================================================

print("\n=== Practical Examples ===")

# Example 1: Student management system
print("📚 Student Management System:")

students_db = [
    {"id": "2025001", "name": "이병남", "age": 25, "grades": [90, 85, 92]},
    {"id": "2025002", "name": "장수민", "age": 23, "grades": [88, 90, 87]},
    {"id": "2025003", "name": "허지호", "age": 24, "grades": [92, 89, 91]}
]

for student in students_db:
    avg_grade = sum(student["grades"]) / len(student["grades"])
    print(f"  {student['name']}: Average grade {avg_grade:.1f}")

# Example 2: Data type checking
print("\n🔍 Data Type Checking:")

sample_data = [
    42,                    # int
    3.14,                  # float
    "Hello",               # str
    True,                  # bool
    [1, 2, 3],            # list
    (4, 5, 6),            # tuple
    {"key": "value"},      # dict
    {7, 8, 9},            # set
    None                   # NoneType
]

for item in sample_data:
    type_name = type(item).__name__
    print(f"  {str(item):15} → {type_name}")

# =============================================================================
# 🏁 SUMMARY
# =============================================================================

print("\n=== Data Types Summary ===")
print("🎯 Python Data Types Learned:")
print("  📊 Numbers: int, float, complex")
print("  📝 Text: str (with methods and slicing)")
print("  ✅ Boolean: True/False and truthiness")
print("  📋 List: Mutable sequences with methods")
print("  📦 Tuple: Immutable sequences for fixed data")
print("  🗂️ Dictionary: Key-value mappings")
print("  🎯 Set: Unique collections with operations")
print("  🚫 None: Representing absence of value")
print("  🔄 Type conversion between data types")

print(f"\n📈 Total data types covered: {len(['int', 'float', 'complex', 'str', 'bool', 'list', 'tuple', 'dict', 'set', 'NoneType'])}")

if __name__ == "__main__":
    print("\n🚀 Run this file to explore Python data types!")