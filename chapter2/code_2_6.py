# ============================================================
#  코드 2-6  DataFrame 생성
#  실행: python code_2_6.py
# ============================================================

import pandas as pd

# 딕셔너리로 DataFrame 생성
data = {
    '자치구':    ['강남구', '서초구', '송파구', '강동구', '마포구'],
    '평균거래금액': [125000,  118000,  95000,  65000,  82000],
    '전용면적':   [84.5,    79.3,    76.2,   72.1,   68.4],
    '거래건수':   [245,     198,     312,    187,    156],
}
apt_df = pd.DataFrame(data)

print(apt_df)
print()
print('shape :', apt_df.shape)       # (5, 4)
print('dtypes:\n', apt_df.dtypes)
print()
print(apt_df.describe())             # 기술통계
