# ============================================================
#  코드 3-7  따릉이 데이터 로드 및 전처리
#  실행: python code_3_7.py
# ============================================================

import pandas as pd
import numpy as np

np.random.seed(42)

# ── 샘플 데이터 (실제 CSV가 있으면 아래 주석 해제) ────────────
# bike_df = pd.read_csv('data/seoul_bike.csv', encoding='utf-8')

# 샘플 데이터 생성
n = 500
start_times = pd.date_range('2024-01-01', periods=n, freq='3h') + \
              pd.to_timedelta(np.random.randint(0, 180, n), unit='m')
durations   = np.random.exponential(scale=25, size=n)   # 평균 25분

bike_df = pd.DataFrame({
    '대여일시': start_times,
    '반납일시': start_times + pd.to_timedelta(durations, unit='m'),
    '대여소명': np.random.choice(['여의도공원', '강남역', '홍대입구', '건대입구'], n),
})

# ── 날짜/시간 데이터 변환 ─────────────────────────────────────
bike_df['대여시각'] = pd.to_datetime(bike_df['대여일시'])
bike_df['반납시각'] = pd.to_datetime(bike_df['반납일시'])

# 이용시간 계산 (분 단위)
bike_df['이용시간'] = (
    bike_df['반납시각'] - bike_df['대여시각']
).dt.total_seconds() / 60

# 시간대, 요일, 월 추출
bike_df['시간대'] = bike_df['대여시각'].dt.hour
bike_df['요일']   = bike_df['대여시각'].dt.day_name()
bike_df['월']     = bike_df['대여시각'].dt.month

# ── 이상치 제거 (0분 미만, 1440분=24시간 초과) ────────────────
before = len(bike_df)
bike_df = bike_df[(bike_df['이용시간'] >= 0) & (bike_df['이용시간'] <= 1440)]
print(f'이상치 제거: {before - len(bike_df)}건 → {len(bike_df)}건 남음')

print()
print(bike_df[['대여시각','이용시간','시간대','요일','월']].head(8))
print()
print(f'이용시간 평균: {bike_df["이용시간"].mean():.1f}분')
print(f'이용시간 중앙값: {bike_df["이용시간"].median():.1f}분')

# 4장에서 사용할 따릉이 데이터 저장
import os
os.makedirs('data', exist_ok=True)
bike_df.to_csv('data/bike_clean.csv', index=False, encoding='utf-8')
print('\n✅ data/bike_clean.csv 저장 완료 (4장에서 사용)')
