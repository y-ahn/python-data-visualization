# ============================================================
#  코드 3-8  시간대별 이용 패턴 분석
#  실행: python code_3_8.py
# ============================================================

import pandas as pd
import numpy as np

np.random.seed(42)

# ── 샘플 데이터 (code_3_7.py 와 동일) ─────────────────────────
n = 2000
start_times = pd.date_range('2024-01-01', periods=n, freq='1h') + \
              pd.to_timedelta(np.random.randint(0, 60, n), unit='m')
durations   = np.random.exponential(scale=25, size=n)

bike_df = pd.DataFrame({
    '대여시각': pd.to_datetime(start_times),
    '이용시간': durations,
})
bike_df['시간대'] = bike_df['대여시각'].dt.hour
bike_df['요일']   = bike_df['대여시각'].dt.day_name()

# ── 시간대별 평균 이용 건수 ───────────────────────────────────
hourly_usage = bike_df.groupby('시간대').size().reset_index(name='이용건수')

print('=== 시간대별 이용 Top 5 ===')
print(hourly_usage.nlargest(5, '이용건수').to_string(index=False))
print()

# ── 요일별 이용 패턴 ─────────────────────────────────────────
day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
day_kr    = {'Monday':'월','Tuesday':'화','Wednesday':'수',
             'Thursday':'목','Friday':'금','Saturday':'토','Sunday':'일'}

daily_usage = bike_df.groupby('요일').size().reset_index(name='이용건수')
daily_usage['요일순'] = daily_usage['요일'].map({d:i for i,d in enumerate(day_order)})
daily_usage = daily_usage.sort_values('요일순')
daily_usage['요일한글'] = daily_usage['요일'].map(day_kr)

print('=== 요일별 이용 건수 ===')
for _, row in daily_usage.iterrows():
    bar = '█' * int(row['이용건수'] / 15)
    print(f"  {row['요일한글']}요일  {row['이용건수']:4d}건  {bar}")
