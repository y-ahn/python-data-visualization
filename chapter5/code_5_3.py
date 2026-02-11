# ============================================================
#  코드 5-3  다중 입력 콜백 (Dropdown + RangeSlider)
#  실행: python code_5_3.py
#  접속: http://127.0.0.1:8050
#  필요: pip install dash plotly pandas numpy
# ============================================================

import pandas as pd
import numpy as np
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# ── 샘플 데이터 (실제 CSV가 있으면 아래 주석 해제) ────────────
# apt_df = pd.read_csv('data/seoul_apt_clean.csv')

np.random.seed(42)
districts   = ['강남구', '서초구', '송파구']
base_price  = {'강남구': 125000, '서초구': 118000, '송파구': 95000}

rows = []
for d in districts:
    prices = np.random.normal(base_price[d], base_price[d] * 0.2, 200)
    for p in prices:
        rows.append({'시군구': d, '거래금액': round(p, 0)})

apt_df = pd.DataFrame(rows)

# ── 앱 생성 ───────────────────────────────────────────────────
app = Dash(__name__)

# ── 레이아웃 ──────────────────────────────────────────────────
app.layout = html.Div([

    html.H1('자치구별 아파트 거래 분석'),

    # Dropdown  ← ... 대신 실제 options 작성
    dcc.Dropdown(
        id='district-dropdown',
        options=[
            {'label': '강남구', 'value': '강남구'},
            {'label': '서초구', 'value': '서초구'},
            {'label': '송파구', 'value': '송파구'},
        ],
        value='강남구'
    ),

    html.Br(),

    # RangeSlider
    html.Label('가격 범위 (만원)'),
    dcc.RangeSlider(
        id='price-slider',
        min=0,
        max=200000,
        step=5000,
        value=[0, 200000],
        marks={i: f'{i//1000}천' for i in range(0, 200001, 50000)}
    ),

    dcc.Graph(id='price-histogram')
])

# ── 다중 입력 콜백 ────────────────────────────────────────────
@app.callback(
    Output('price-histogram', 'figure'),
    Input('district-dropdown', 'value'),
    Input('price-slider', 'value')
)
def update_graph(selected_district, price_range):
    filtered_df = apt_df[
        (apt_df['시군구'] == selected_district) &
        (apt_df['거래금액'] >= price_range[0]) &
        (apt_df['거래금액'] <= price_range[1])
    ]
    fig = px.histogram(
        filtered_df,
        x='거래금액',
        nbins=50,
        title=f'{selected_district} 거래금액 분포  '
              f'({price_range[0]//1000}천 ~ {price_range[1]//1000}천만원)',
        color_discrete_sequence=['#3d7aba']
    )
    fig.update_layout(
        xaxis_title='거래금액 (만원)',
        yaxis_title='거래 건수',
        template='plotly_white'
    )
    return fig

# ── 앱 실행 ───────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)   # run_server() → run() 으로 변경
