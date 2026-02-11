# ============================================================
#  코드 3-2  거래금액 및 면적 데이터 정제
#  실행: python code_3_2.py
# ============================================================

import pandas as pd
import numpy as np
import os

np.random.seed(42)

# ── 샘플 데이터 (code_3_1.py 와 동일 생성) ────────────────────
districts  = ['강남구','서초구','송파구','용산구','마포구']
base_price = [125, 118, 95, 88, 82]
rows = []
for d, base in zip(districts, base_price):
    for month in range(1, 13):
        for _ in range(20):
            area  = np.random.uniform(40, 120)
            price = base * (area / 85) * np.random.uniform(0.85, 1.15)
            rows.append({
                '시군구':   d,
                '계약년월': f'2024{month:02d}',
                '계약일':   np.random.randint(1, 28),
                '전용면적': round(area, 1),
                '거래금액': f'{round(price * 10000):,}',  # 쉼표 포함 문자열
            })
apt_df = pd.DataFrame(rows)

# ── 1. 거래금액 정제 (쉼표 제거 후 숫자 변환) ────────────────
apt_df['거래금액'] = apt_df['거래금액'].str.replace(',', '').astype(int)

# ── 2. 날짜 데이터 생성 (년월 + 일 병합) ─────────────────────
apt_df['계약일'] = pd.to_datetime(
    apt_df['계약년월'].astype(str) +
    apt_df['계약일'].astype(str).str.zfill(2),
    format='%Y%m%d'
)
apt_df['연월'] = apt_df['계약일'].dt.to_period('M').astype(str)

# ── 3. 평수·평당가격 계산 ─────────────────────────────────────
apt_df['평수']     = apt_df['전용면적'] / 3.3058
apt_df['평당가격'] = (apt_df['거래금액'] / apt_df['평수']).round(0)

# ── 4. 결측치 및 이상치 제거 ─────────────────────────────────
apt_df = apt_df.dropna()
apt_df = apt_df[apt_df['거래금액'] > 0]

print('정제 완료')
print(f'  데이터 크기: {apt_df.shape}')
print(f'  결측치: {apt_df.isnull().sum().sum()}')
print()
print(apt_df[['시군구','계약일','연월','거래금액','평수','평당가격']].head(8))

# ── 5. 정제된 데이터 저장 (4장에서 사용) ─────────────────────
os.makedirs('data', exist_ok=True)
apt_df.to_csv('data/seoul_apt_clean.csv', index=False, encoding='utf-8')
print('\n✅ data/seoul_apt_clean.csv 저장 완료 (4장에서 사용)')
