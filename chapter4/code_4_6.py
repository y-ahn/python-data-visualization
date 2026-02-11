# ============================================================
#  코드 4-6  박스 플롯 (px.box)
#  실행: python code_4_6.py
#  출력: code_4_6.html  → 브라우저로 열기
# ============================================================

import pandas as pd
import numpy as np
import plotly.express as px

np.random.seed(42)

# ── 데이터 준비 ──────────────────────────────────────────────
# 실제 CSV가 있으면 아래 주석을 해제하세요
# apt_df = pd.read_csv("data/seoul_apt_clean.csv")
# top_districts = ["강남구", "서초구", "송파구", "용산구", "마포구"]
# box_df = apt_df[apt_df["시군구"].isin(top_districts)]

# 샘플 데이터 (정규분포로 거래금액 분포 생성)
top_districts = ["강남구", "서초구", "송파구", "용산구", "마포구"]
base_prices   = [125, 118, 95, 88, 82]

rows = []
for district, base in zip(top_districts, base_prices):
    prices = np.random.normal(base, base * 0.12, 200)
    for p in prices:
        rows.append({"시군구": district, "거래금액": round(p, 1)})
box_df = pd.DataFrame(rows)

# ── 박스 플롯 생성 ────────────────────────────────────────────
fig = px.box(
    box_df,
    x="시군구",
    y="거래금액",
    color="시군구",
    title="자치구별 아파트 거래금액 분포",
    labels={"시군구": "자치구", "거래금액": "거래금액 (천만원)"},
    points="outliers",                    # 이상치만 점으로 표시
    category_orders={"시군구": top_districts},
)
fig.update_layout(template="plotly_white", showlegend=False)

# ── HTML 저장 ─────────────────────────────────────────────────
fig.write_html("code_4_6.html")
print("✅ code_4_6.html 저장 완료 — 브라우저로 열어보세요")
