# ============================================================
#  코드 4-8  파이 차트 (px.pie, hole=0.3 도넛)
#  실행: python code_4_8.py
#  출력: code_4_8.html  → 브라우저로 열기
# ============================================================

import pandas as pd
import plotly.express as px

# ── 데이터 준비 ──────────────────────────────────────────────
# 실제 CSV가 있으면 아래 주석을 해제하세요
# pop_df    = pd.read_csv("data/population_clean.csv")
# age_total = pop_df.groupby("연령대")["인구수"].sum().reset_index()

# 샘플 데이터
age_total = pd.DataFrame({
    "연령대": ["0-19세", "20-39세", "40-59세", "60세 이상"],
    "인구수": [950_000, 1_800_000, 1_650_000, 1_100_000],
})

# ── 파이 차트 (도넛) 생성 ─────────────────────────────────────
fig = px.pie(
    age_total,
    names="연령대",
    values="인구수",
    title="서울시 연령대별 인구 비율",
    hole=0.3,                              # 0.3 = 도넛 모양
    color_discrete_sequence=["#4472C4", "#70AD47", "#FFC000", "#DC2626"],
)
fig.update_traces(
    textposition="inside",
    textinfo="percent+label",
)
fig.update_layout(template="plotly_white")

# ── HTML 저장 ─────────────────────────────────────────────────
fig.write_html("code_4_8.html")
print("✅ code_4_8.html 저장 완료 — 브라우저로 열어보세요")
