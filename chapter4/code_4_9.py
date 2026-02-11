# ============================================================
#  코드 4-9  레이아웃 커스터마이징
#            (update_layout / update_xaxes / update_traces)
#  실행: python code_4_9.py
#  출력: code_4_9.html  → 브라우저로 열기
# ============================================================

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ── 데이터 준비 (코드 4-4와 동일한 월별 거래건수) ───────────────
monthly = pd.DataFrame({
    "연월":    [f"2024-{m:02d}" for m in range(1, 13)],
    "거래건수": [850, 920, 1100, 980, 1050, 890, 750, 820, 950, 1080, 1150, 980],
})

# ── 좌·우 두 그래프 배치 ──────────────────────────────────────
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("스타일 적용 전 (Default)", "스타일 적용 후 (Customized)"),
    horizontal_spacing=0.1,
)

# 왼쪽 : 기본 스타일 그대로
fig.add_trace(
    go.Scatter(
        x=monthly["연월"], y=monthly["거래건수"],
        mode="lines+markers",
        name="기본",
        showlegend=False,
    ),
    row=1, col=1,
)

# 오른쪽 : 커스터마이징 적용할 동일 데이터
fig.add_trace(
    go.Scatter(
        x=monthly["연월"], y=monthly["거래건수"],
        mode="lines+markers",
        name="커스텀",
        showlegend=False,
    ),
    row=1, col=2,
)

# ── update_layout : 전체 레이아웃 ────────────────────────────
fig.update_layout(
    title=dict(
        text="코드 4-9 | 레이아웃 커스터마이징 — 적용 전 vs 적용 후",
        font=dict(size=18, color="#1F4788"),
    ),
    template="plotly_white",    # ← 흰 배경 테마
    hovermode="x unified",      # ← x축 기준 통합 호버
    height=450,
)

# ── update_xaxes : x축 각도 (오른쪽만) ───────────────────────
fig.update_xaxes(tickangle=45, col=2)

# ── update_traces : 마커·선 스타일 (오른쪽만) ────────────────
fig.update_traces(
    selector=dict(name="커스텀"),
    line=dict(color="#1F4788", width=2.5),
    marker=dict(
        color="#4472C4",
        size=9,
        line=dict(color="white", width=2),
    ),
)

# ── HTML 저장 ─────────────────────────────────────────────────
fig.write_html("code_4_9.html")
print("✅ code_4_9.html 저장 완료 — 브라우저로 열어보세요")
