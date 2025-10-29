# 📚 AI-ACE 레퍼런스 솔루션 브랜치

**main** 브랜치에 오신 것을 환영합니다! 이 브랜치는 모든 일일 미션의 레퍼런스 솔루션과 예제를 제공합니다.

## 👥 우리 팀 - AI Track 서브 그룹

### 팀 멤버:
- **Tony Lee** (@aiegoo) - 팀 리더 (서브 그룹 기간 중)
- **ChangMin** (@changminis) - 팀 멤버
- **Heozico** (@heozico) - 팀 멤버 (team scriber) 
- **Joonii93** (@joonii93-ops) - 팀 멤버
- **Jsmin2080** (@jsmin2080-afk) - 팀 멤버
- **Weisheit129** (@weisheit129) - 팀 멤버

### 🔗 중요 링크:
- **📊 구글 마스터시트**: [AI Track 진도 추적](https://docs.google.com/spreadsheets/d/1wXp2DvRJQz4G9mpcYZjBxFEkFyRopkFjHVNw3cEKyMM/edit?usp=sharing)
- **🏠 메인 리포지토리**: [ai-track](https://github.com/aiegoo/ai-track)
- **👥 팀 리포지토리**: [ai-ace](https://github.com/aiegoo/ai-ace)
- **📋 구름 LMS**: [AI Track 7회차 과정](https://k-digital.goorm.io/lecture/61583/7회차-생성-ai-응용-서비스-개발자-양성-과정)

### 📝 플랫폼 링크:

| 사용 목적 | 플랫폼 | 링크 |
|-----------|--------|------|
| **소통** | 디스코드 [메인 소통 창구] | [생성ai-7회차](https://discordapp.com/channels/1240560508659175437/1422500198822842398) |
| **강의장** | Zoom [실시간 비대면 강의장] | 생성 AI 7회차 줌 |
| **멘토링룸** | Zep [메타버스: 퍼실리테이션, DEEP 톡, 팀 스터디] | [Zep 룸](https://zep.us/play/yondAn) |
| | Zep 예약 현황 모니터링 시트 | [예약 시트](https://docs.google.com/spreadsheets/d/1dW9aD62xqGkXgPAblGFtbVYLF8kTFQI5cLXeJ77nXFs/edit?usp=sharing) |
| **학습** | 구름LMS [강의 자료, 시험, 녹화본] | [LMS](https://k-digital.goorm.io/learn/lecture/61583/7%ED%9A%8C%EC%B0%A8-%EC%83%9D%EC%84%B1-ai-%EC%9D%91%EC%9A%A9-%EC%84%9C%EB%B9%84%EC%8A%A4-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%96%91%EC%84%B1-%EA%B3%BC%EC%A0%95) |
| | 구름EDU(EXP) [미션 수행] | [EXP](https://exp.goorm.io/) |
| **문서화** | 노션 [프로젝트, 팀 스터디, 학습 일지] | [7회차 노션](https://goormkdx.notion.site/7-294c0ff4ce3180cc8f41fc9d603a14bf?source=copy_link) |

### 📋 과정 정보:
- **전체 과정 기간**: 2025년 10월 28일 ~ 2026년 5월 20일 (약 205일, 29주, 131 수업일)
- **서브 그룹 활동 기간**: 2025년 10월 29일 ~ 2025년 11월 27일 (30일)
- **포커스**: 일일 POC 프로젝트와 실습 중심 학습
- **협업 방식**: GitHub 기반 팀 워크플로우

## 🎯 이 브랜치의 목적

이 브랜치는:
- ✅ **레퍼런스 솔루션** - 잘 문서화된 예제 구현
- ✅ **학습 리소스** - 다양한 접근 방식 비교
- ✅ **베스트 프랙티스** - 코드 스타일과 구조 예제
- ✅ **미션 템플릿** - 향후 과제를 위한 구조

## 🔍 레퍼런스 솔루션 사용법

### 자신의 작업과 비교하기:
```bash
# main 브랜치로 전환하여 레퍼런스 솔루션 확인
git checkout main

# 레퍼런스 구현 살펴보기
cd day01
cat chicken_art_reference.py

# 자신의 브랜치로 돌아가서 작업 계속
git checkout [your-branch-name]
```

### 예제로부터 학습하기:
1. **먼저 자신만의 솔루션을 완성하세요** - 너무 일찍 보지 마세요!
2. **접근 방식 비교** - 같은 문제에 대한 다른 해결법 확인
3. **새로운 기법 학습** - 모르는 Python 기능 발견
4. **코드 개선** - 향후 미션에 학습한 내용 적용

## 📁 Reference Structure

Each daily mission will have:
```
## 📁 레퍼런스 구조

각 일일 미션은 다음을 포함합니다:
```
dayXX/
├── README_REFERENCE.md           # 미션 목표와 학습 목표
├── solution_basic.py             # 간단하고 초보자 친화적인 솔루션
├── solution_advanced.py          # 고급 기법과 최적화
├── solution_creative.py          # 창의적이고 재미있는 변형
├── LEARNING_NOTES.md            # 핵심 개념과 설명
└── COMMON_MISTAKES.md           # 피해야 할 실수와 디버깅 방법
```

## 🎓 학습 철학

### Remember:
- 🌟 **Multiple solutions are valid** - There's no single "right" way
- 🚀 **Your approach matters** - Even simple solutions are valuable
- 🔄 **Iteration improves code** - First working, then better
- 🤝 **Learn from others** - But make it your own

### 하지 말아야 할 것:
- ❌ 이해하지 못한 채 솔루션 복사하기
- ❌ 자신의 코드가 다르다고 기분 나빠하기
- ❌ 학습 과정 건너뛰기
- ❌ 이해보다 속도를 비교하기

## 🚀 빠른 내비게이션

### 팀 멤버를 위한 안내:
```bash
# 리포지토리 클론
git clone git@github.com:aiegoo/ai-ace.git
cd ai-ace

# 개인 워크스페이스로 전환
git checkout [your-name]-workspace

# 레퍼런스 솔루션 보기 (이 브랜치)
git checkout main
```

### 개별 워크스페이스:
- `changminis-workspace` - ChangMin의 개인 워크스페이스
- `heozico-workspace` - Heozico의 개인 워크스페이스  
- `joonii93-ops-workspace` - Joonii93의 개인 워크스페이스
- `jsmin2080-afk-workspace` - Jsmin2080의 개인 워크스페이스
- `weisheit129-workspace` - Weisheit129의 개인 워크스페이스
- `tonylee-workspace` - Tony의 개인 워크스페이스

## 📊 진도 추적

[구글 마스터시트](https://docs.google.com/spreadsheets/d/1wXp2DvRJQz4G9mpcYZjBxFEkFyRopkFjHVNw3cEKyMM/edit?usp=sharing)에서 진도와 팀 통계를 확인하세요.

시트에는 다음이 포함됩니다:
- ✅ 일일 미션 완료 상태
- 📈 개인 진도 추적
- 🏆 팀 성취와 마일스톤
- 📝 노트와 회고
- 🎯 다가오는 미션 미리보기

## 🆘 도움이 필요하신가요?

1. **LEARNING_NOTES.md 확인** - 핵심 개념 설명
2. **COMMON_MISTAKES.md 검토** - 문제해결 가이드
3. **레퍼런스 솔루션과 비교** - 다양한 접근법 확인
4. **팀 토론에서 질문** - 함께 협력하고 학습
5. **마스터시트 업데이트** - 질문과 진도 추적

## 🎉 AI Track에 오신 것을 환영합니다!

코딩 여정을 시작할 준비가 되셨나요? 개인 워크스페이스로 이동하여 Day 1부터 시작하세요!

**즐거운 코딩 되세요! 🚀**

## 🔄 미션 비교 워크플로우

1. **개인 브랜치에서 솔루션 작업**
2. **기본 요구사항을 먼저 완성**
3. **접근법 테스트 및 문서화**
4. **학습을 위해 레퍼런스 솔루션 확인**
5. **새로운 인사이트를 바탕으로 반복 개선**
6. **팀과 발견한 내용 공유**

## 🎯 현재 미션

- ✅ **Day 1: ASCII 닭 아트** - 다양한 구현 방식
- ⏳ **Day 2: TBD** - 곧 공개!
- ⏳ **Day 3: TBD** - 곧 공개!

---

**즐거운 학습과 비교 되세요! 🚀**

기억하세요: 가장 좋은 솔루션은 여러분이 이해하고 다른 사람에게 설명할 수 있는 것입니다!