# ============================================================
#  코드 5-4  Dash 대시보드
#
#  실행 방법 2가지 중 선택하세요:
#
#  ① HTML 파일로 저장 (Dash 설치 불필요, 브라우저에서 바로 열림)
#       python code_5_4.py
#       → code_5_4.html 생성
#
#  ② 실제 Dash 앱 실행 (드롭다운으로 자치구 바꾸면 그래프 실시간 변경)
#       pip install dash
#       python code_5_4.py --dash
#       → http://127.0.0.1:8050 접속
# ============================================================

import sys
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

np.random.seed(42)

# ── 샘플 데이터 ──────────────────────────────────────────────
# 실제 CSV가 있으면 아래 주석을 해제하세요
# apt_df = pd.read_csv('data/seoul_apt_clean.csv')
# apt_df['연월'] = pd.to_datetime(apt_df['계약일']).dt.to_period('M').astype(str)

MONTHS = [f'2024-{m:02d}' for m in range(1, 13)]
DISTRICT_DATA = {
    '강남구': [123, 125, 127, 126, 128, 130, 129, 131, 132, 130, 128, 125],
    '서초구': [116, 118, 119, 118, 120, 121, 120, 119, 118, 117, 116, 115],
    '송파구': [93,  95,  96,  97,  98,  99,  97,  96,  95,  94,  93,  92],
    '용산구': [86,  88,  87,  89,  90,  91,  89,  88,  87,  86,  85,  84],
    '마포구': [80,  82,  83,  82,  84,  85,  84,  83,  82,  81,  80,  79],
}


# ── 그래프 생성 함수 (HTML 저장 · Dash 콜백 공용) ─────────────
def make_trend_fig(district):
    """콜백 update_trend() 에 해당"""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=MONTHS,
        y=DISTRICT_DATA[district],
        mode='lines+markers',
        line=dict(color='#1F4788', width=2.5),
        marker=dict(size=9, color='#4472C4', line=dict(color='white', width=2)),
        fill='tozeroy',
        fillcolor='rgba(68,114,196,0.08)',
        hovertemplate='%{x}<br>평균: %{y:,}천만원<extra></extra>',
    ))
    fig.update_layout(
        title=f'{district} 월별 평균 거래금액 추이',
        xaxis_title='계약 연월',
        yaxis_title='평균 거래금액 (천만원)',
        template='plotly_white',
        hovermode='x unified',
        xaxis_tickangle=-45,
        margin=dict(t=50, b=50, l=60, r=20),
    )
    return fig


def make_dist_fig(district):
    """콜백 update_distribution() 에 해당"""
    base   = sum(DISTRICT_DATA[district]) / 12
    prices = np.random.normal(base, base * 0.2, 500)
    mean_v = prices.mean()
    med_v  = float(pd.Series(prices).median())

    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=prices, nbinsx=50,
        marker_color='#4472C4', opacity=0.75,
        hovertemplate='구간: %{x}<br>건수: %{y}<extra></extra>',
    ))
    fig.add_vline(x=mean_v, line_dash='dash', line_color='#DC2626', line_width=2,
                  annotation_text=f'평균 {mean_v:.0f}',
                  annotation_font_color='#DC2626')
    fig.add_vline(x=med_v,  line_dash='dot',  line_color='#22863A', line_width=2,
                  annotation_text=f'중앙값 {med_v:.0f}',
                  annotation_position='top left',
                  annotation_font_color='#22863A')
    fig.update_layout(
        title=f'{district} 거래금액 분포',
        xaxis_title='거래금액 (천만원)',
        yaxis_title='빈도',
        template='plotly_white',
        showlegend=False,
        margin=dict(t=50, b=50, l=60, r=20),
    )
    return fig


# ════════════════════════════════════════════════════════════
#  실행 방법 ① : HTML 저장  (python code_5_4.py)
# ════════════════════════════════════════════════════════════
if '--dash' not in sys.argv:

    DEFAULT = '강남구'
    dashboard = make_subplots(
        rows=1, cols=2,
        subplot_titles=(
            f'[update_trend]  {DEFAULT} 월별 평균 거래금액 추이',
            f'[update_distribution]  {DEFAULT} 거래금액 분포',
        ),
        horizontal_spacing=0.12,
    )
    for trace in make_trend_fig(DEFAULT).data:
        dashboard.add_trace(trace, row=1, col=1)
    for trace in make_dist_fig(DEFAULT).data:
        dashboard.add_trace(trace, row=1, col=2)

    dashboard.update_layout(
        title=dict(
            text=(
                f'코드 5-4 | Dash 대시보드  ·  자치구: {DEFAULT}<br>'
                '<sup>드롭다운 인터랙션이 필요하면:  python code_5_4.py --dash</sup>'
            ),
            font=dict(size=16, color='#1F4788'),
        ),
        template='plotly_white',
        height=500,
        showlegend=False,
    )
    dashboard.update_xaxes(title_text='계약 연월',          tickangle=-45, col=1)
    dashboard.update_xaxes(title_text='거래금액 (천만원)',               col=2)
    dashboard.update_yaxes(title_text='평균 거래금액 (천만원)',           col=1)
    dashboard.update_yaxes(title_text='빈도',                            col=2)

    dashboard.write_html('code_5_4.html')
    print('✅ code_5_4.html 저장 완료 — 브라우저로 열어보세요')
    print()
    print('드롭다운 인터랙션이 필요하면:')
    print('  pip install dash')
    print('  python code_5_4.py --dash')


# ════════════════════════════════════════════════════════════
#  실행 방법 ② : Dash 앱  (python code_5_4.py --dash)
# ════════════════════════════════════════════════════════════
else:

    from dash import Dash, dcc, html, Input, Output

    app = Dash(__name__)

    app.layout = html.Div(
        style={'fontFamily': 'sans-serif', 'backgroundColor': '#F5F7FA'},
        children=[

            # 헤더
            html.Div(
                style={'backgroundColor': '#1F4788', 'color': 'white',
                       'padding': '20px 32px'},
                children=[
                    html.H2('서울시 부동산 분석 대시보드', style={'margin': 0}),
                    html.P('코드 5-4 | Dash + Plotly',
                           style={'margin': '4px 0 0', 'opacity': 0.7}),
                ],
            ),

            # 드롭다운
            html.Div(
                style={'padding': '16px 32px', 'backgroundColor': 'white',
                       'borderBottom': '1px solid #DDE3ED'},
                children=[
                    html.Label('자치구 선택  ',
                               style={'fontWeight': 'bold', 'color': '#1F4788'}),
                    dcc.Dropdown(
                        id='district-dropdown',
                        options=[{'label': d, 'value': d} for d in DISTRICT_DATA],
                        value='강남구',
                        clearable=False,
                        style={'width': '200px', 'display': 'inline-block'},
                    ),
                ],
            ),

            # 그래프 두 개
            html.Div(
                style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr'},
                children=[
                    html.Div(style={'backgroundColor': 'white', 'padding': '16px',
                                    'borderRight': '1px solid #DDE3ED'},
                             children=[dcc.Graph(id='trend-graph')]),
                    html.Div(style={'backgroundColor': 'white', 'padding': '16px'},
                             children=[dcc.Graph(id='dist-graph')]),
                ],
            ),
        ],
    )

    @app.callback(Output('trend-graph', 'figure'),
                  Input('district-dropdown', 'value'))
    def update_trend(district):
        return make_trend_fig(district)

    @app.callback(Output('dist-graph', 'figure'),
                  Input('district-dropdown', 'value'))
    def update_distribution(district):
        return make_dist_fig(district)

    print('━' * 45)
    print('  Dash 앱 실행 중...')
    print('  브라우저 접속: http://127.0.0.1:8050')
    print('  종료: Ctrl + C')
    print('━' * 45)
    app.run(debug=True)
