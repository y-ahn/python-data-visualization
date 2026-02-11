# ============================================================
#  코드 2-14  Excel 파일 읽기 및 저장
#  실행: python code_2_14.py
#  필요: pip install openpyxl
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

# Excel 저장
apt_df.to_excel('data/seoul_apt.xlsx', index=False, sheet_name='실거래가')
print('✅ data/seoul_apt.xlsx 저장 완료')

# Excel 읽기
df_excel = pd.read_excel('data/seoul_apt.xlsx', sheet_name='실거래가')
print(df_excel)

# 여러 시트 저장
with pd.ExcelWriter('data/seoul_report.xlsx') as writer:
    apt_df.to_excel(writer, sheet_name='실거래가', index=False)
    apt_df.describe().to_excel(writer, sheet_name='통계요약')
print('✅ data/seoul_report.xlsx (2개 시트) 저장 완료')
