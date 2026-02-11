# ============================================================
#  코드 4-4  월별 거래량 시계열 (dt.to_period + px.line)
#  실행: python code_4_4.py
#  출력: code_4_4.html  → 브라우저로 열기
# ============================================================

import pandas as pd
import numpy as np
import plotly.express as px

np.random.seed(42)

# ── 데이터 준비 ──────────────────────────────────────────────
# 실제 CSV가 있으면 아래 주석을 해제하세요
# apt_df = pd.read_csv("data/seoul_apt_clean.csv")
# apt_df["계약일"] = pd.to_datetime(apt_df["계약일"])
# apt_df["연월"]   = apt_df["계약일"].dt.to_period("M").astype(str)  # ← to_period 핵심
# monthly = apt_df.groupby("연월").size().reset_index(name="거래건수")

# 샘플 데이터
monthly = pd.DataFrame({
    "연월":    [f"2024-{m:02d}" for m in range(1, 13)],
    "거래건수": [850, 920, 1100, 980, 1050, 890, 750, 820, 950, 1080, 1150, 980],
})

# ── 시계열 선 그래프 생성 ─────────────────────────────────────
fig = px.line(
    monthly,
    x="연월",
    y="거래건수",
    title="서울시 아파트 월별 거래 건수",
    markers=True,
    labels={"연월": "계약 연월", "거래건수": "거래 건수 (건)"},
)
fig.update_traces(
    line_color="#2E5C8A",
    line_width=2.5,
    marker=dict(size=9, symbol="circle-open",
                line=dict(color="#2E5C8A", width=2.5)),
)
fig.update_layout(template="plotly_white", hovermode="x unified")

# 최고점 강조 어노테이션
peak_idx   = monthly["거래건수"].idxmax()
peak_month = monthly.loc[peak_idx, "연월"]
peak_cnt   = monthly.loc[peak_idx, "거래건수"]
fig.add_annotation(
    x=peak_month, y=peak_cnt,
    text=f"최고<br><b>{peak_cnt:,}건</b>",
    showarrow=True, arrowcolor="#DC2626",
    font=dict(color="#DC2626", size=12),
    ax=-60, ay=-40,
)

# ── HTML 저장 ─────────────────────────────────────────────────
fig.write_html("code_4_4.html")
print("✅ code_4_4.html 저장 완료 — 브라우저로 열어보세요")
