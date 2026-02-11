# ============================================================
#  코드 3-3  자치구별 평균 거래금액 및 평당가격 계산
#  실행: python code_3_3.py
# ============================================================

import pandas as pd
import numpy as np

np.random.seed(42)

# ── 샘플 데이터 (code_3_2.py 실행 후 저장된 파일이 있으면 아래 사용) ──
# apt_df = pd.read_csv('data/seoul_apt_clean.csv')

# 샘플 데이터 직접 생성
districts  = ['강남구','서초구','송파구','용산구','마포구',
               '강동구','관악구','노원구','종로구','중구']
base_price = [125, 118, 95, 88, 82, 65, 58, 52, 75, 70]
rows = []
for d, base in zip(districts, base_price):
    for _ in range(100):
        area  = np.random.uniform(40, 120)
        price = base * (area / 85) * np.random.uniform(0.85, 1.15)
        rows.append({
            '시군구':   d,
            '아파트':   f'{d[:2]}아파트',
            '거래금액': round(price, 0),
            '전용면적': round(area, 1),
            '평수':     round(area / 3.3058, 2),
            '평당가격': round((price / (area / 3.3058)), 0),
        })
apt_df = pd.DataFrame(rows)

# ── 자치구별 평균 거래금액 및 평당가격 계산 ───────────────────
district_summary = apt_df.groupby('시군구').agg(
    평균거래금액=('거래금액', 'mean'),
    평균평당가격=('평당가격', 'mean'),
    거래건수=('아파트', 'count'),
).round(0)

# 평균 거래금액 기준 내림차순 정렬
district_summary = district_summary.sort_values('평균거래금액', ascending=False)

print('=== 자치구별 평균 거래금액 Top 10 ===')
print(district_summary.head(10).to_string())
