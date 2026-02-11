# ============================================================
#  코드 3-4  인구 데이터 로드 및 연령대 그룹 생성
#  실행: python code_3_4.py
# ============================================================

import pandas as pd
import numpy as np

np.random.seed(42)

# ── 샘플 데이터 (실제 CSV가 있으면 아래 주석 해제) ────────────
# pop_df = pd.read_csv('data/seoul_population.csv', encoding='utf-8')

districts = ['강남구','서초구','송파구','마포구','노원구']
rows = []
for d in districts:
    for age in range(0, 90):
        count = int(np.random.normal(3000, 800))
        rows.append({'자치구': d, '나이': age, '인구수': max(0, count)})
pop_df = pd.DataFrame(rows)

# ── 연령대 그룹 생성 함수 ─────────────────────────────────────
def age_group(age):
    if age < 20:
        return '0-19세'
    elif age < 40:
        return '20-39세'
    elif age < 60:
        return '40-59세'
    else:
        return '60세 이상'

# 연령대 컬럼 추가
pop_df['연령대'] = pop_df['나이'].apply(age_group)

print(pop_df.head(10))
print()
print('연령대 분포:')
print(pop_df['연령대'].value_counts())
