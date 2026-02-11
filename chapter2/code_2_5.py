# ============================================================
#  코드 2-5  Series 생성 및 활용
#  실행: python code_2_5.py
# ============================================================

import pandas as pd

# 라벨과 데이터로 Series 생성
label = ['강남구', '서초구', '송파구', '강동구', '마포구']
data  = [540000, 420000, 660000, 450000, 380000]
population = pd.Series(data, index=label)
print(population)

# 특정 값 조회
print(population['강남구'])   # 540000

# 기본 연산
print(population.mean())      # 평균
print(population.max())       # 최대값
print(population[population > 450000])  # 조건 필터
