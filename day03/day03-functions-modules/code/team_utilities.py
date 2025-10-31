"""
Day 3: AI-ACE Team Utility Functions - Template Ready for Content

This module will contain utility functions that demonstrate
how our team members use functions and modules in practice.

Template created and ready for your Day 3 content!
"""

# Team member data structure
AI_ACE_TEAM = {
    "이병남": {"role": "팀장 & Course Leader", "nickname": "Tony Lee", "specialty": "Leadership"},
    "장수민": {"role": "Developer", "nickname": "ChangMin", "specialty": "Development"},
    "허지호": {"role": "Team Scriber", "nickname": "Heozico", "specialty": "Documentation"},
    "이상준": {"role": "Operations Expert", "nickname": "Joonii93", "specialty": "Operations"},
    "정수민": {"role": "AI Track Member", "nickname": "Jsmin2080", "specialty": "AI Processing"},
    "고준": {"role": "Deep Learning Focus", "nickname": "Weisheit129", "specialty": "Deep Learning"}
}

def get_team_info(member_name=None):
    """Get information about AI-ACE team members"""
    if member_name:
        return AI_ACE_TEAM.get(member_name, "Member not found")
    return AI_ACE_TEAM

def display_team():
    """Display all team members with their roles"""
    print("👥 AI-ACE Team Members:")
    print("=" * 50)
    
    for name, info in AI_ACE_TEAM.items():
        print(f"🎯 {name} ({info['nickname']})")
        print(f"   Role: {info['role']}")
        print(f"   Specialty: {info['specialty']}")
        print()

def team_function_examples():
    """Template for team-specific function examples"""
    print("🔧 Team Function Examples - Template Ready!")
    print("📝 This will contain function examples from each team member")
    print("🎯 Following our established AI-ACE learning pattern")
    
    return "Team utilities template ready!"

# Main execution
if __name__ == "__main__":
    print("🚀 AI-ACE Team Utilities - Day 3 Functions & Modules")
    print()
    
    display_team()
    
    result = team_function_examples()
    print(f"✅ {result}")
    print("\n📝 Ready for your Day 3 team utilities content!")