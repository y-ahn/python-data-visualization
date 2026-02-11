# ============================================================
#  코드 2-13  CSV 파일 저장
#  실행: python code_2_13.py
# ============================================================

import pandas as pd
import os

apt_df = pd.DataFrame({
    '자치구':    ['강남구', '서초구', '송파구', '강동구', '마포구'],
    '평균거래금액': [125000, 118000, 95000, 65000, 82000],
    '전용면적':   [84.5, 79.3, 76.2, 72.1, 68.4],
    '거래건수':   [245, 198, 312, 187, 156],
})

os.makedirs('data', exist_ok=True)

# CSV 저장 — index=False : 인덱스 번호 제외
apt_df.to_csv('data/seoul_apt_clean.csv', index=False, encoding='utf-8')
print('✅ data/seoul_apt_clean.csv 저장 완료')

# 저장 확인
check = pd.read_csv('data/seoul_apt_clean.csv')
print(check)
