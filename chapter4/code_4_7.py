# ============================================================
#  코드 4-7  히트맵 (go.Heatmap, pivot, colorscale='YlOrRd')
#  실행: python code_4_7.py
#  출력: code_4_7.html  → 브라우저로 열기
# ============================================================

import pandas as pd
import numpy as np
import plotly.graph_objects as go

np.random.seed(42)

# ── 데이터 준비 ──────────────────────────────────────────────
# 실제 CSV가 있으면 아래 주석을 해제하세요
# bike_df = pd.read_csv("data/bike_clean.csv")
# bike_df["대여일시"] = pd.to_datetime(bike_df["대여일시"])
# bike_df["시간대"]   = bike_df["대여일시"].dt.hour
# bike_df["요일"]     = bike_df["대여일시"].dt.day_name()
# pivot = bike_df.pivot_table(
#     values="이용건수", index="요일", columns="시간대", aggfunc="sum"
# )

# 샘플 데이터 (요일 × 시간대 이용 건수)
weekdays   = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
base_hour  = [150,100,80,70,80,180,400,750,1100,820,650,
              680,720,660,590,550,680,870,1050,820,580,420,280,190]

rows = []
for day in weekdays:
    for hour, base in enumerate(base_hour):
        cnt = base * np.random.normal(1.0, 0.08)
        if day in ["Saturday", "Sunday"]:
            if 10 <= hour <= 16: cnt *= 1.5
            elif  6 <= hour <=  9: cnt *= 0.5
            elif 17 <= hour <= 20: cnt *= 0.6
        rows.append({"요일": day, "시간대": hour, "이용건수": max(0, round(cnt))})
bike_df = pd.DataFrame(rows)

# ── 피벗 테이블 생성 ──────────────────────────────────────────
pivot = bike_df.pivot_table(
    values="이용건수",
    index="요일",
    columns="시간대",
    aggfunc="sum",
)

# 요일 순서 · 한글 변환
day_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
day_kr    = ["월요일", "화요일", "수요일",   "목요일",  "금요일", "토요일",  "일요일"]
pivot = pivot.reindex(day_order)

# ── 히트맵 생성 ───────────────────────────────────────────────
fig = go.Figure(go.Heatmap(
    z=pivot.values,
    x=[f"{h}시" for h in pivot.columns],
    y=day_kr,
    colorscale="YlOrRd",
    hovertemplate="%{y} %{x}<br>이용: %{z:.0f}건<extra></extra>",
    colorbar=dict(title="이용 건수"),
))
fig.update_layout(
    title="따릉이 요일 × 시간대별 이용 패턴",
    xaxis_title="시간대",
    yaxis_title="요일",
    template="plotly_white",
)

# ── HTML 저장 ─────────────────────────────────────────────────
fig.write_html("code_4_7.html")
print("✅ code_4_7.html 저장 완료 — 브라우저로 열어보세요")
