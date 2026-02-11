# ============================================================
#  코드 2-15  날짜 데이터 변환 및 추출
#  실행: python code_2_15.py
# ============================================================

import pandas as pd

# 날짜 문자열이 포함된 샘플 데이터
apt_df = pd.DataFrame({
    '계약일':   ['2024-01-15', '2024-02-20', '2024-03-05',
                 '2024-06-18', '2024-11-30'],
    '자치구':   ['강남구', '서초구', '송파구', '마포구', '강동구'],
    '거래금액': [125000, 118000, 95000, 82000, 65000],
})

# 문자열 → datetime 변환
apt_df['계약일'] = pd.to_datetime(apt_df['계약일'])
print('dtype:', apt_df['계약일'].dtype)   # datetime64[ns]
print()

# 날짜 구성요소 추출
apt_df['연도'] = apt_df['계약일'].dt.year
apt_df['월']   = apt_df['계약일'].dt.month
apt_df['요일'] = apt_df['계약일'].dt.day_name()

# to_period : 월 단위 기간으로 변환 (groupby에 유용)
apt_df['연월'] = apt_df['계약일'].dt.to_period('M').astype(str)

print(apt_df[['계약일', '연도', '월', '요일', '연월']])
print()

# 월별 평균 거래금액
print('=== 월별 평균 거래금액 ===')
print(apt_df.groupby('연월')['거래금액'].mean())
