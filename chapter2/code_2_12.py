# ============================================================
#  코드 2-12  CSV 파일 읽기
#  실행: python code_2_12.py
# ============================================================

import pandas as pd
import os

# ── 실제 CSV가 있으면 아래를 사용하세요 ──────────────────────
# apt_df = pd.read_csv('data/seoul_apt_price.csv', encoding='utf-8')

# ── 샘플 CSV 생성 후 읽기 (파일 없어도 실행 가능) ─────────────
sample_csv = """자치구,거래금액,전용면적,거래건수
강남구,125000,84.5,245
서초구,118000,79.3,198
송파구,95000,76.2,312
강동구,65000,72.1,187
마포구,82000,68.4,156
"""
os.makedirs('data', exist_ok=True)
with open('data/sample_apt.csv', 'w', encoding='utf-8') as f:
    f.write(sample_csv)

# CSV 읽기
apt_df = pd.read_csv('data/sample_apt.csv', encoding='utf-8')
print('데이터 크기:', apt_df.shape)
print()
print(apt_df.head())
print()
print(apt_df.dtypes)
