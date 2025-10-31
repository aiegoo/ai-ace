# 🎯 Day 3 Functions & Modules: 코드에서 함수 추출하기

## 📋 학습 목표
`ex04결혼증감율실습.ipynb`에서 실제 정부 통계 분석 코드를 함수로 분리하여 재사용 가능한 모듈을 만들어보세요.

## 🔍 함수 추출 패턴 분석

### 1. 데이터 로딩 함수
```python
# 현재 코드 (Cell 1-3)
df = pd.read_csv('혼인건수_시도_시_군_구__20251031074342.csv', encoding='euc-kr')
df.columns = df.columns.str.strip()

# 함수로 추출하기
def load_marriage_data(file_path, encoding='euc-kr'):
    """KOSIS 혼인 데이터를 로드하고 전처리합니다."""
    df = pd.read_csv(file_path, encoding=encoding)
    df.columns = df.columns.str.strip()
    return df
```

### 2. 월별 집계 함수
```python
# 현재 코드 (Cell 4-6)
national_values = {
    '2024.07': df['2024.07'].sum(),
    '2024.08': df['2024.08'].sum(),
    # ... 반복되는 코드
}

# 함수로 추출하기
def calculate_monthly_totals(df, year=2024, months=range(7, 13)):
    """월별 전국 혼인건수를 계산합니다."""
    monthly_totals = {}
    for month in months:
        col_name = f'{year}.{month:02d}'
        if col_name in df.columns:
            monthly_totals[col_name] = df[col_name].sum()
    return monthly_totals
```

### 3. 지역별 분석 함수
```python
# 현재 코드 (Cell 7-10)
regional_data = df.groupby('시군구별').agg({
    '2024.07': 'sum', '2024.08': 'sum', ...
}).reset_index()

# 함수로 추출하기
def analyze_regional_data(df, year=2024, months=range(7, 13)):
    """지역별 혼인 통계를 분석합니다."""
    month_cols = [f'{year}.{month:02d}' for month in months if f'{year}.{month:02d}' in df.columns]
    
    regional_data = df.groupby('시군구별').agg(
        {col: 'sum' for col in month_cols}
    ).reset_index()
    
    regional_data['하반기_합계'] = regional_data[month_cols].sum(axis=1)
    regional_data['월평균'] = regional_data['하반기_합계'] / len(month_cols)
    
    return regional_data
```

### 4. 증감률 계산 함수
```python
# 현재 코드 (Cell 11-13)
monthly_growth_rates = []
for i in range(1, len(values)):
    growth = (values[i] - values[i-1]) / values[i-1] * 100
    monthly_growth_rates.append(growth)

# 함수로 추출하기
def calculate_growth_rates(values):
    """월별 증감률을 계산합니다."""
    growth_rates = []
    for i in range(1, len(values)):
        growth = (values[i] - values[i-1]) / values[i-1] * 100
        growth_rates.append(round(growth, 2))
    return growth_rates
```

### 5. 시각화 함수
```python
# 현재 코드 (Cell 15-20)
fig, axes = plt.subplots(2, 4, figsize=(20, 12))
# ... 복잡한 시각화 코드

# 함수로 추출하기
def create_government_dashboard(monthly_data, regional_data, save_path=None):
    """정부 보고서 스타일의 종합 대시보드를 생성합니다."""
    fig, axes = plt.subplots(2, 4, figsize=(20, 12))
    
    # 각 서브플롯 생성 로직을 별도 함수로 분리
    plot_monthly_trend(axes[0,0], monthly_data)
    plot_top_regions(axes[0,1], regional_data)
    plot_growth_rates(axes[0,2], monthly_data)
    # ... 기타 플롯 함수들
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    return fig
```

### 6. 데이터 내보내기 함수
```python
# 현재 코드 (Cell 25)
regional_export.to_csv('KOSIS_지역별_혼인통계_분석.csv', encoding='utf-8-sig')

# 함수로 추출하기
def export_analysis_results(monthly_data, regional_data, output_dir='./'):
    """분석 결과를 CSV 파일로 내보냅니다."""
    import os
    
    # 월별 데이터 내보내기
    monthly_df = pd.DataFrame({
        '월': list(monthly_data.keys()),
        '혼인건수': list(monthly_data.values())
    })
    monthly_df.to_csv(os.path.join(output_dir, 'monthly_analysis.csv'), 
                     encoding='utf-8-sig', index=False)
    
    # 지역별 데이터 내보내기
    regional_data.to_csv(os.path.join(output_dir, 'regional_analysis.csv'), 
                        encoding='utf-8-sig', index=False)
    
    return ['monthly_analysis.csv', 'regional_analysis.csv']
```

## 🎯 실습 과제

### Step 1: 기본 함수 작성
1. `load_marriage_data()` 함수를 작성하여 데이터 로딩을 모듈화하세요
2. `calculate_monthly_totals()` 함수로 월별 집계를 자동화하세요
3. 각 함수에 적절한 docstring을 추가하세요

### Step 2: 분석 함수 모듈화
1. `analyze_regional_data()` 함수를 구현하세요
2. `calculate_growth_rates()` 함수를 작성하세요
3. 매개변수와 반환값을 명확히 정의하세요

### Step 3: 시각화 함수 분리
1. 큰 시각화 코드를 작은 함수들로 분해하세요
2. `plot_monthly_trend()`, `plot_regional_chart()` 등 개별 플롯 함수를 만드세요
3. 공통 스타일 설정을 별도 함수로 분리하세요

### Step 4: 모듈 파일 생성
1. `marriage_analysis.py` 파일을 생성하세요
2. 모든 함수를 모듈로 정리하세요
3. `if __name__ == "__main__":` 구문으로 테스트 코드를 추가하세요

### Step 5: 메인 스크립트 작성
1. 모듈을 import하여 사용하는 깔끔한 메인 스크립트를 작성하세요
2. 원래 노트북과 동일한 결과를 함수 호출로 구현하세요

## 📝 함수 설계 가이드라인

### 1. 단일 책임 원칙
- 각 함수는 하나의 명확한 기능만 수행
- 함수 이름으로 기능을 명확히 표현

### 2. 매개변수 설계
- 필수 매개변수와 선택적 매개변수 구분
- 기본값 설정으로 사용성 향상
- 타입 힌트 추가 권장

### 3. 에러 처리
- 파일 경로, 컬럼명 등 유효성 검사
- 의미 있는 에러 메시지 제공
- try-except 구문 적절히 활용

### 4. 문서화
- 함수의 목적, 매개변수, 반환값 설명
- 사용 예시 포함
- 주의사항 명시

## 🏆 완성 목표

### 모듈 구조 예시
```
marriage_analysis/
├── __init__.py
├── data_loader.py       # 데이터 로딩 함수들
├── statistics.py        # 통계 계산 함수들
├── visualization.py     # 시각화 함수들
├── export.py           # 내보내기 함수들
└── main.py             # 메인 실행 스크립트
```

### 사용 예시
```python
# 모듈화된 코드 사용
from marriage_analysis import data_loader, statistics, visualization

# 데이터 로드
df = data_loader.load_marriage_data('marriage_data.csv')

# 분석 수행
monthly_totals = statistics.calculate_monthly_totals(df)
regional_data = statistics.analyze_regional_data(df)

# 시각화 생성
visualization.create_government_dashboard(monthly_totals, regional_data, 'dashboard.png')
```

이제 복잡한 분석 코드를 재사용 가능한 함수와 모듈로 변환하는 실제 경험을 해보세요! 🚀