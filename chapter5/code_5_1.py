import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# ── 샘플 데이터 (실제 CSV가 있으면 아래 주석 해제)
# apt_df = pd.read_csv('data/seoul_apt_clean.csv')

apt_df = pd.DataFrame({
    '자치구':    ['강남구','서초구','송파구','용산구','마포구',
                  '강동구','관악구','노원구','종로구','중구'],
    '평균거래금액': [125000,118000,95000,88000,82000,
                    65000,58000,52000,75000,70000],
})

# ── fig 생성 (반드시 layout 보다 먼저!)
fig = px.bar(
    apt_df,
    x='자치구',
    y='평균거래금액',
    title='서울시 자치구별 평균 아파트 거래금액',
    color='평균거래금액',
    color_continuous_scale='Blues',
)

# ── Dash 앱 생성
app = Dash(__name__)

# ── 레이아웃 정의
app.layout = html.Div([
    html.H1('서울시 부동산 대시보드'),
    html.P('아파트 실거래가 분석'),
    dcc.Graph(id='price-graph', figure=fig)
])

# ── 앱 실행 (run_server → run 으로 변경)
if __name__ == '__main__':
    app.run(debug=True)