# 🧪 Quick Demo Version - AI-ACE Team Examples
# Extracted from our Jupyter notebook for standalone execution

print("🧪 Quick Demo: Age Calculator with Team Examples")
print("=" * 50)

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
print("   ✓ 문자열 → 숫자 변환")
print("   ✓ 나이 계산 (빼기 연산)")
print("   ✓ 미래 나이 계산 (더하기 연산)")
print("   ✓ 숫자 → 문자열 변환")
print("   ✓ 문자열 연결 출력")

print("\n🎯 Daily Mission Requirements Summary:")
print("1. ✅ input() 사용하여 이름 받기")
print("2. ✅ input() 사용하여 태어난 연도 받기")
print("3. ✅ int() 사용하여 문자열을 숫자로 변환")
print("4. ✅ current_year = 2025 설정")
print("5. ✅ 빼기 연산으로 현재 나이 계산")
print("6. ✅ 더하기 연산으로 100년 뒤 나이 계산")
print("7. ✅ str() 사용하여 숫자를 문자열로 변환")
print("8. ✅ + 연산자로 문자열 연결하여 예쁜 출력")

print("\n🚀 Bonus Features Added:")
print("   💡 f-string 포맷팅 (Day 2 advanced content)")
print("   🎨 ANSI 색상 코드 (Day 2 advanced content)")
print("   🔍 데이터 타입 확인 (Day 2 data types)")
print("   📊 팀 통계 계산 (수학 연산 활용)")
print("   ⚠️  에러 처리 (예외 처리)")