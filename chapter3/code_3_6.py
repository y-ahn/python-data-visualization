# ============================================================
#  코드 3-6  자치구별 고령화율 계산
#  실행: python code_3_6.py
# ============================================================

import pandas as pd
import numpy as np

np.random.seed(42)

# ── 샘플 데이터 ───────────────────────────────────────────────
districts = ['강남구','서초구','송파구','마포구','노원구',
             '도봉구','강북구','종로구','중구','서대문구']
rows = []
for i, d in enumerate(districts):
    for age in range(0, 90):
        # 강북/도봉/노원 쪽은 고령화율 높게
        base = 2500 + i * 100 if age >= 60 else 3000
        count = int(np.random.normal(base, 500))
        rows.append({'자치구': d, '나이': age, '인구수': max(0, count)})
pop_df = pd.DataFrame(rows)

# ── 고령화율 계산 ─────────────────────────────────────────────
# 전체 인구
total_pop   = pop_df.groupby('자치구')['인구수'].sum()

# 60세 이상 인구
elderly_pop = (
    pop_df[pop_df['나이'] >= 60]
    .groupby('자치구')['인구수']
    .sum()
)

# 고령화율 (%) = 60세이상 / 전체 * 100
aging_rate = (elderly_pop / total_pop * 100).round(2)
aging_rate = aging_rate.sort_values(ascending=False)

print('=== 자치구별 고령화율 (%) ===')
for district, rate in aging_rate.items():
    bar = '█' * int(rate / 2)
    print(f'  {district:6s}  {rate:5.1f}%  {bar}')
print()
print(f'평균 고령화율: {aging_rate.mean():.1f}%')
print(f'최고: {aging_rate.idxmax()} {aging_rate.max():.1f}%')
print(f'최저: {aging_rate.idxmin()} {aging_rate.min():.1f}%')
