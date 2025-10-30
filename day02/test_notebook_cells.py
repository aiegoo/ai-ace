# 🔧 Essential imports for our Day 2 journey
import sys
import datetime
import time
import json
from collections import Counter

# Display our setup
print("🚀 Jupyter Environment Setup Complete!")
print(f"📍 Python Version: {sys.version}")
print(f"📅 Session Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Check if we're in Jupyter
try:
    from IPython.display import display, HTML, Markdown
    print("✅ Jupyter/IPython environment detected!")
    print("💡 You can use display(), HTML(), and Markdown() for rich output")
except ImportError:
    print("⚠️  Running in standard Python (not Jupyter)")

print("\n🎯 Ready for Day 2 Advanced Python Learning!")
print("👥 Team: AI-ACE + Goorm AI Track 7th Students")

print("\n" + "="*50)
print("🎯 Now running the F-String Demo:")
print("="*50)

# 🎯 F-String Magic - The Modern Way
print("=== F-String Formatting Demo ===")

# Our AI-ACE team data
team_leader = "이병남"
age = 25
course = "AI Track 7th"
team_size = 6

# Basic f-string
print(f"👋 안녕하세요! I'm {team_leader}, leader of AI-ACE team")

# F-string with expressions
print(f"📊 Team Info: {team_size} members in {course}")
print(f"🎂 Age next year: {age + 1}")

# F-string with formatting
gpa = 3.8456789
print(f"📈 GPA: {gpa:.2f}")  # 2 decimal places

# F-string with width and alignment
print(f"{'Name':<15} {'Age':>5} {'Role':<20}")
print(f"{team_leader:<15} {age:>5} {'Team Leader':<20}")

print("\n💡 Try it yourself: Change the values above and re-run this cell!")