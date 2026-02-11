# ============================================================
#  코드 4-3  산점도 (px.scatter, color, size, hover_data)
#  실행: python code_4_3.py
#  출력: code_4_3.html  → 브라우저로 열기
# ============================================================

import pandas as pd
import numpy as np
import plotly.express as px

np.random.seed(42)

# ── 데이터 준비 ──────────────────────────────────────────────
# 실제 CSV가 있으면 아래 주석을 해제하세요
# apt_df = pd.read_csv("data/seoul_apt_clean.csv")
# top5 = ["강남구", "서초구", "송파구", "용산구", "마포구"]
# apt_df = apt_df[apt_df["시군구"].isin(top5)]

# 샘플 데이터
top5_info = {"강남구": 125, "서초구": 118, "송파구": 95, "용산구": 88, "마포구": 82}
rows = []
for district, base in top5_info.items():
    for _ in range(80):
        area  = np.random.uniform(40, 150)
        price = base * (area / 85) * np.random.uniform(0.85, 1.15)
        rows.append({
            "시군구":   district,
            "전용면적": round(area, 1),
            "거래금액": round(price, 0),
            "층":       np.random.randint(1, 30),
            "아파트명": f"{district[:2]}아파트{np.random.randint(1,5)}단지",
        })
apt_df = pd.DataFrame(rows)

# ── 산점도 생성 ───────────────────────────────────────────────
fig = px.scatter(
    apt_df,
    x="전용면적",
    y="거래금액",
    color="시군구",
    size="전용면적",
    hover_data=["아파트명", "층"],
    title="전용면적 vs 거래금액  (색상=자치구, 크기=면적)",
    labels={"전용면적": "전용면적 (㎡)", "거래금액": "거래금액 (천만원)", "시군구": "자치구"},
    opacity=0.65,
    size_max=25,
)
fig.update_layout(template="plotly_white")

# ── HTML 저장 ─────────────────────────────────────────────────
fig.write_html("code_4_3.html")
print("✅ code_4_3.html 저장 완료 — 브라우저로 열어보세요")
