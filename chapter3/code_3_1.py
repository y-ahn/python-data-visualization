# ============================================================
#  코드 3-1  실거래가 데이터 읽기 및 기본 탐색
#  실행: python code_3_1.py
# ============================================================

import pandas as pd
import numpy as np
import os

np.random.seed(42)

# ── 실제 CSV가 있으면 아래 주석을 해제하세요 ──────────────────
# apt_df = pd.read_csv('data/seoul_apt_price.csv', encoding='utf-8')

# ── 샘플 데이터 생성 ──────────────────────────────────────────
districts = ['강남구','서초구','송파구','용산구','마포구',
             '강동구','관악구','노원구','종로구','중구']
base_price = [125,118,95,88,82,65,58,52,75,70]

rows = []
for d, base in zip(districts, base_price):
    for month in range(1, 13):
        for _ in range(np.random.randint(20, 40)):
            area  = np.random.uniform(40, 120)
            price = base * (area / 85) * np.random.uniform(0.85, 1.15)
            rows.append({
                '시군구':    d,
                '계약년월':  f'2024{month:02d}',
                '계약일':    np.random.randint(1, 28),
                '아파트':    f'{d[:2]}아파트',
                '전용면적':  round(area, 1),
                '거래금액':  f'{round(price * 10000):,}',  # 쉼표 있는 문자열
                '층':        np.random.randint(1, 30),
            })
apt_df = pd.DataFrame(rows)

# ── 데이터 구조 확인 (코드 3-1 본문) ─────────────────────────
print(f'데이터 크기: {apt_df.shape}')
print('\n컬럼 정보:')
print(apt_df.info())
print('\n처음 5개 데이터:')
print(apt_df.head())
print('\n기술통계:')
print(apt_df.describe(include='all'))
