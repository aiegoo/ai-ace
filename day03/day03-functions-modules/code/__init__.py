# Package initialization for Day 3 Functions & Modules
"""
Day 3: Functions & Modules Learning Package

This package contains all the supporting code examples and utilities
for learning functions and modules in Python.

AI-ACE Team Learning Materials
Course: Goorm AI Track 7th
Date: November 1, 2025
"""

__version__ = "1.0.0"
__author__ = "AI-ACE Team"
__course__ = "Goorm AI Track 7th"

# Import main learning modules when package is imported
try:
    from .function_examples import *
    from .module_samples import *
    from .team_utilities import *
except ImportError:
    # Handle import errors gracefully during development
    pass

print("📦 Day 3 Functions & Modules package loaded!")
print("🎯 Ready for AI-ACE learning experience!")