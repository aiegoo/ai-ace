# 🤖 Age Calculator Bot - Daily Mission Demo
# Running our Jupyter notebook code as a standalone script

def main():
    print("🎯 Daily Mission: Age Calculator Bot")
    print("=" * 40)

    try:
        # Step 1: 사용자 이름 입력받기
        name = input("당신의 이름은? ").strip()
        
        if not name:
            print("⚠️ 이름을 입력해주세요!")
            name = "익명"
        
        # Step 2: 태어난 연도 입력받기
        birth_year_str = input("태어난 연도(숫자 4자리): ").strip()
        
        # Step 3: 문자열을 숫자로 변환
        birth_year_num = int(birth_year_str)
        
        # 유효성 검사
        if birth_year_num < 1900 or birth_year_num > 2025:
            print("⚠️ 유효하지 않은 연도입니다. (1900-2025)")
            birth_year_num = 2000  # 기본값
        
        # Step 4: 현재 연도 설정
        current_year = 2025
        
        # Step 5: 현재 나이 계산 (빼기 연산)
        current_age = current_year - birth_year_num
        
        # Step 6: 100년 뒤 나이 계산 (더하기 연산)
        future_age = current_age + 100
        
        # Step 7 & 8: 숫자를 문자열로 변환하고 예쁜 출력
        print("\n" + "🎉 결과 발표 🎉")
        print("-" * 30)
        print("안녕하세요, " + name + "님.")
        print("당신의 현재 나이는 " + str(current_age) + "살입니다.")
        print("100년 뒤에는 " + str(future_age) + "살이 되시겠네요!")

        # 보너스: f-string으로도 해보기
        print("\n💡 f-string 버전:")
        print(f"안녕하세요, {name}님.")
        print(f"당신의 현재 나이는 {current_age}살입니다.")
        print(f"100년 뒤에는 {future_age}살이 되시겠네요!")
        
        # 나이에 따른 추가 메시지
        print("\n🎊 추가 정보:")
        if current_age < 0:
            print(f"🔮 {name}님은 미래에서 오셨군요! (아직 태어나지 않음)")
        elif current_age == 0:
            print(f"🍼 {name}님은 올해 태어난 신생아입니다!")
        elif current_age < 20:
            print(f"🎓 {name}님은 {current_age}살의 젊은 학생이군요!")
        elif current_age < 65:
            print(f"💼 {name}님은 {current_age}살의 현역 세대입니다!")
        else:
            print(f"🎖️ {name}님은 {current_age}살의 인생 선배님입니다!")
        
        if future_age >= 100:
            print("🏆 100세 이상까지 살게 되시는군요! 장수하세요!")

    except ValueError:
        print("❌ 오류: 태어난 연도는 숫자로 입력해주세요!")
    except Exception as e:
        print(f"❌ 예상치 못한 오류가 발생했습니다: {e}")

def demo_with_team_data():
    """AI-ACE 팀 데이터로 자동 데모"""
    print("\n" + "="*50)
    print("🧪 AI-ACE Team Demo (No Input Required)")
    print("="*50)
    
    # AI-ACE 팀 멤버들의 예시 데이터
    team_examples = [
        {"name": "이병남", "birth_year": 2000},
        {"name": "장수민", "birth_year": 1999}, 
        {"name": "허지호", "birth_year": 2001},
        {"name": "이상준", "birth_year": 2000},
        {"name": "정수민", "birth_year": 2002},
        {"name": "고준", "birth_year": 1998}
    ]

    current_year = 2025

    print("👥 AI-ACE Team Age Analysis:")
    print("-" * 30)

    for member in team_examples:
        # Mission requirements 적용
        name = member["name"]
        birth_year_str = str(member["birth_year"])  # Step 2: 문자열로 시뮬레이션
        birth_year_num = int(birth_year_str)        # Step 3: 숫자로 변환
        
        current_age = current_year - birth_year_num  # Step 5: 현재 나이 계산
        future_age = current_age + 100              # Step 6: 100년 뒤 나이 계산
        
        # Step 7 & 8: 문자열 변환 및 출력
        print("안녕하세요, " + name + "님.")
        print("당신의 현재 나이는 " + str(current_age) + "살입니다.")
        print("100년 뒤에는 " + str(future_age) + "살이 되시겠네요!")
        print()

    # 팀 평균 나이 계산
    total_age = sum(current_year - member["birth_year"] for member in team_examples)
    average_age = total_age / len(team_examples)

    print(f"📊 팀 통계:")
    print(f"   평균 나이: {average_age:.1f}살")
    print(f"   팀 크기: {len(team_examples)}명")
    print(f"   100년 뒤 평균: {average_age + 100:.1f}살")

    print("\n✅ Mission Complete! 모든 요구사항이 구현되었습니다:")
    print("   ✓ input() 시뮬레이션")
    print("   ✓ 문자열 → 숫자 변환 int()")
    print("   ✓ 나이 계산 (빼기 연산)")
    print("   ✓ 미래 나이 계산 (더하기 연산)")
    print("   ✓ 숫자 → 문자열 변환 str()")
    print("   ✓ 문자열 연결 출력")

if __name__ == "__main__":
    print("🚀 Age Calculator Bot Demo")
    print("Choose an option:")
    print("1. Interactive mode (with input)")
    print("2. Demo mode (AI-ACE team data)")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == "1":
        main()
    elif choice == "2":
        demo_with_team_data()
    else:
        print("Invalid choice. Running demo mode...")
        demo_with_team_data()
    
    print("\n🎉 Thanks for trying our Age Calculator Bot!")
    print("💡 This demonstrates all Day 2 concepts: variables, data types, input/output, and formatting!")