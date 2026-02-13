# 📊 Python 데이터 시각화 입문
### 한국 공공데이터로 배우는 실전 분석

> **안영준 저 | Published by Rentify**

이 저장소는 『Python 데이터 시각화 입문』의 **챕터별 실습 소스코드**를 제공합니다.

---

## 📖 책 소개

서울 부동산 · 인구통계 · 공공자전거 데이터를 활용하여  
**Pandas → Plotly → Dash** 흐름으로 데이터 수집부터 인터랙티브 대시보드 구축까지 배웁니다.

---

## 🛠️ 실행 환경

| 항목 | 버전 |
|------|------|
| Python | 3.9 이상 |
| pandas | 2.0 이상 |
| plotly | 5.0 이상 |
| dash | 2.0 이상 |
| openpyxl | 3.0 이상 |

### 라이브러리 설치

```bash
pip install pandas plotly dash openpyxl numpy
```

---

## 📁 폴더 구조

```
python-data-visualization/
│
├── chapter2/          # Python 환경 구축 · Pandas 기초
│   ├── code_2_5.py       - Series 생성 및 활용
│   ├── code_2_6.py       - DataFrame 생성
│   ├── code_2_7.py       - 열(Column) 선택
│   ├── code_2_8.py       - 조건으로 행 필터링
│   ├── code_2_9.py       - loc와 iloc 사용
│   ├── code_2_10.py      - 기본 통계 함수
│   ├── code_2_11.py      - groupby를 사용한 그룹별 집계
│   ├── code_2_12.py      - CSV 파일 읽기
│   ├── code_2_13.py      - CSV 파일 저장
│   ├── code_2_14.py      - Excel 파일 읽기 및 저장
│   └── code_2_15.py      - 날짜 데이터 변환 및 추출
│
├── chapter3/          # 데이터 전처리
│   ├── code_3_1.py       - 실거래가 데이터 읽기 및 기본 탐색
│   ├── code_3_2.py       - 거래금액 및 면적 데이터 정제
│   ├── code_3_3.py       - 자치구별 평균 거래금액 및 평당가격 계산
│   ├── code_3_4.py       - 인구 데이터 로드 및 연령대 그룹 생성
│   ├── code_3_5.py       - 자치구 및 연령대별 인구 집계
│   ├── code_3_6.py       - 자치구별 고령화율 계산
│   ├── code_3_7.py       - 따릉이 데이터 로드 및 전처리
│   └── code_3_8.py       - 시간대별 이용 패턴 분석
│
├── chapter4/          # Plotly 인터랙티브 시각화
│   ├── code_4_1.py       - 기본 선 그래프
│   ├── code_4_2.py       - 막대 그래프
│   ├── code_4_3.py       - 산점도
│   ├── code_4_4.py       - 시계열 그래프
│   ├── code_4_5.py       - 다중선 비교
│   ├── code_4_6.py       - 박스플롯
│   ├── code_4_7.py       - 히트맵
│   ├── code_4_8.py       - 파이 / 도넛 차트
│   └── code_4_9.py       - 레이아웃 커스터마이징
│
└── chapter5/          # Dash 대시보드
    └── code_5_1.py       - 기본 Dash 앱
    └── code_5_2.py       - 드롭다운 자치구 선택
    └── code_5_3.py       - 다중 입력 콜백
    └── code_5_4.py       - 인터랙티브 대시보드
                            (① HTML 저장  ② 실제 Dash 앱, 두 가지 실행 방법 포함)
```

---

## ▶️ 실행 방법

### 기본 실행 (Chapter 2 · 3)
```bash
python chapter2/code_2_5.py
python chapter3/code_3_1.py
```

### Plotly 그래프 (Chapter 4)
```bash
python chapter4/code_4_1.py
# → code_4_1.html 생성 → 브라우저로 열기
```

### Dash 대시보드 (Chapter 5)

**방법 ① HTML 파일로 저장** (Dash 설치 불필요)
```bash
python chapter5/code_5_4.py
# → code_5_4.html 생성 → 브라우저로 열기
```

**방법 ② 실제 Dash 앱 실행** (드롭다운 인터랙션 포함)
```bash
pip install dash
python chapter5/code_5_4.py --dash
# → 브라우저에서 http://127.0.0.1:8050 접속
```

---

## 📂 샘플 데이터 안내

각 코드 파일에는 **샘플 데이터가 내장**되어 있어 별도 파일 없이 즉시 실행 가능합니다.

실제 공공데이터를 사용하려면 코드 상단 주석을 참고하세요:

```python
# 실제 CSV가 있으면 아래 주석을 해제하세요
# apt_df = pd.read_csv('data/seoul_apt_price.csv', encoding='utf-8')
```

| 데이터 | 출처 | 비고 |
|--------|------|------|
| 서울 아파트 실거래가 | [국토교통부 실거래가 공개시스템](https://rt.molit.go.kr) | chapter3, 4 |
| 서울시 인구통계 | [서울 열린데이터광장](https://data.seoul.go.kr) | chapter3, 4 |
| 서울 따릉이 이용정보 | [서울 열린데이터광장](https://data.seoul.go.kr) | chapter3, 4 |

---

## 🔖 챕터별 학습 내용

| 챕터 | 제목 | 핵심 내용 |
|------|------|-----------|
| 1장 | 데이터 분석을 위한 시각화 역할 | 시각화 장점, 한국 공공데이터, 인터랙티브 시각화 |
| 2장 | Python 환경 구축 · Pandas 기초 | Series, DataFrame, groupby, CSV/Excel |
| 3장 | 데이터 전처리 | 결측치 처리, 날짜 변환, 집계, 고령화율 |
| 4장 | Plotly 시각화 | 선/막대/산점도/히트맵/파이차트, 레이아웃 |
| 5장 | Dash 대시보드 | 콜백, 드롭다운, 실시간 그래프 업데이트 |

---

<p align="center">
  ⭐ 이 저장소가 도움이 되셨다면 Star를 눌러주세요!
</p>
