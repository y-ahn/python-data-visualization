# ============================================================
#  코드 4-2  막대 그래프 (px.bar, color_continuous_scale='Blues')
#  실행: python code_4_2.py
#  출력: code_4_2.html  → 브라우저로 열기
# ============================================================

import pandas as pd
import numpy as np
import plotly.express as px

np.random.seed(42)

# ── 데이터 준비 ──────────────────────────────────────────────
# 실제 CSV가 있으면 아래 주석을 해제하세요
# apt_df = pd.read_csv("data/seoul_apt_clean.csv")
# district_summary = (
#     apt_df.groupby("시군구")["거래금액"]
#     .mean().reset_index()
#     .sort_values("거래금액", ascending=False)
# )

# 샘플 데이터
district_summary = pd.DataFrame({
    "시군구": ["강남구","서초구","송파구","용산구","마포구",
               "강동구","관악구","노원구","종로구","중구",
               "도봉구","성북구","중랑구","동대문구","서대문구"],
    "거래금액": [125, 118, 95, 88, 82, 65, 58, 52, 75, 70, 55, 60, 57, 63, 67],
}).sort_values("거래금액", ascending=False)

# ── 막대 그래프 생성 ──────────────────────────────────────────
fig = px.bar(
    district_summary,
    x="시군구",
    y="거래금액",
    color="거래금액",
    color_continuous_scale="Blues",
    title="자치구별 평균 아파트 거래금액",
    labels={"시군구": "자치구", "거래금액": "평균 거래금액 (천만원)"},
    text_auto=".0f",
)
fig.update_layout(template="plotly_white", xaxis_tickangle=-40)
fig.update_traces(textposition="outside")

# ── HTML 저장 ─────────────────────────────────────────────────
fig.write_html("code_4_2.html")
print("✅ code_4_2.html 저장 완료 — 브라우저로 열어보세요")
