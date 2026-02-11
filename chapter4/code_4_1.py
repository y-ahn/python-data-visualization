# ============================================================
#  코드 4-1  기본 선 그래프 (px.line)
#  실행: python code_4_1.py
#  출력: code_4_1.html  → 브라우저로 열기
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
# df = apt_df.groupby("연월")["거래금액"].mean().reset_index()

# 샘플 데이터
df = pd.DataFrame({
    "연월":    [f"2024-{m:02d}" for m in range(1, 13)],
    "거래금액": [85, 87, 91, 89, 93, 95, 92, 94, 96, 98, 97, 99],
})

# ── 선 그래프 생성 ────────────────────────────────────────────
fig = px.line(
    df,
    x="연월",
    y="거래금액",
    title="서울시 아파트 월별 평균 거래금액 추이",
    markers=True,
    labels={"연월": "계약 연월", "거래금액": "평균 거래금액 (천만원)"},
)
fig.update_layout(template="plotly_white", hovermode="x unified")

# ── HTML 저장 ─────────────────────────────────────────────────
fig.write_html("code_4_1.html")
print("✅ code_4_1.html 저장 완료 — 브라우저로 열어보세요")
