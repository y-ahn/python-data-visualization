# ============================================================
#  코드 3-5  자치구 및 연령대별 인구 집계
#  실행: python code_3_5.py
# ============================================================

import pandas as pd
import numpy as np

np.random.seed(42)

# ── 샘플 데이터 (code_3_4.py 와 동일) ─────────────────────────
def age_group(age):
    if age < 20:   return '0-19세'
    elif age < 40: return '20-39세'
    elif age < 60: return '40-59세'
    else:          return '60세 이상'

districts = ['강남구','서초구','송파구','마포구','노원구']
rows = []
for d in districts:
    for age in range(0, 90):
        count = int(np.random.normal(3000, 800))
        rows.append({'자치구': d, '나이': age, '인구수': max(0, count)})
pop_df = pd.DataFrame(rows)
pop_df['연령대'] = pop_df['나이'].apply(age_group)

# ── 자치구 및 연령대별 인구 집계 ──────────────────────────────
pop_summary = pop_df.groupby(['자치구', '연령대'])['인구수'].sum().reset_index()

# 피벗 테이블로 변환 (자치구 × 연령대)
pop_pivot = pop_summary.pivot(index='자치구', columns='연령대', values='인구수')

print('=== 자치구 × 연령대 인구 피벗 테이블 ===')
print(pop_pivot.to_string())
print()

# 인구 비율 계산
pop_pivot_pct = pop_pivot.div(pop_pivot.sum(axis=1), axis=0).round(3) * 100
print('=== 연령대 비율 (%) ===')
print(pop_pivot_pct.to_string())
