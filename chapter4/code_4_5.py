# ============================================================
#  코드 4-5  자치구별 비교 시계열 (hovermode='x unified')
#  실행: python code_4_5.py
#  출력: code_4_5.html  → 브라우저로 열기
# ============================================================

import pandas as pd
import numpy as np
import plotly.express as px

np.random.seed(42)

# ── 데이터 준비 ──────────────────────────────────────────────
# 실제 CSV가 있으면 아래 주석을 해제하세요
# apt_df = pd.read_csv("data/seoul_apt_clean.csv")
# apt_df["계약일"] = pd.to_datetime(apt_df["계약일"])
# apt_df["연월"]   = apt_df["계약일"].dt.to_period("M").astype(str)
# top_districts = ["강남구", "서초구", "송파구", "용산구", "마포구"]
# df5 = (
#     apt_df[apt_df["시군구"].isin(top_districts)]
#     .groupby(["연월", "시군구"])["거래금액"]
#     .mean().reset_index()
# )

# 샘플 데이터
months = [f"2024-{m:02d}" for m in range(1, 13)]
district_prices = {
    "강남구": [123, 125, 127, 126, 128, 130, 129, 131, 132, 130, 128, 125],
    "서초구": [116, 118, 119, 118, 120, 121, 120, 119, 118, 117, 116, 115],
    "송파구": [93,  95,  96,  97,  98,  99,  97,  96,  95,  94,  93,  92],
    "용산구": [86,  88,  87,  89,  90,  91,  89,  88,  87,  86,  85,  84],
    "마포구": [80,  82,  83,  82,  84,  85,  84,  83,  82,  81,  80,  79],
}
rows = [
    {"연월": m, "시군구": d, "거래금액": p}
    for d, prices in district_prices.items()
    for m, p in zip(months, prices)
]
df5 = pd.DataFrame(rows)

# ── 다중 선 그래프 생성 ───────────────────────────────────────
fig = px.line(
    df5,
    x="연월",
    y="거래금액",
    color="시군구",
    title="주요 자치구 월별 평균 거래금액 비교",
    markers=True,
    labels={"연월": "계약 연월", "거래금액": "평균 거래금액 (천만원)", "시군구": "자치구"},
)
fig.update_traces(line_width=2.5, marker_size=7)
fig.update_layout(
    template="plotly_white",
    hovermode="x unified",    # ← 핵심: 모든 자치구 값 동시 표시
    xaxis_tickangle=-45,
)

# ── HTML 저장 ─────────────────────────────────────────────────
fig.write_html("code_4_5.html")
print("✅ code_4_5.html 저장 완료 — 브라우저로 열어보세요")
