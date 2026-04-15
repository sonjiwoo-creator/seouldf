# 서울 관광 상권 분석 프로젝트

## 👥 팀 분업
- **추정매출-상권**: [손지우]
- **점포-상권**: [김소희]
- **길단위인구-상권**: [조정연]
- **상권변화지표-상권**: [이나경]

## 📦 초기 세팅

### 1. 저장소 clone
```bash
git clone https://github.com/sonjiwoo-creator/seouldf.git
cd seouldf
```

### 2. 가상환경 설정
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install pandas numpy matplotlib seaborn jupyter
```

### 3. 데이터 준비
`data/raw/` 안에 있는 zip 파일들을 각자 로컬에서 압축 해제하세요.
노트북 첫 셀에 자동 압축 해제 코드가 있으면 그냥 실행하면 됩니다.

## 📁 폴더 구조
\```
seouldf/
├─ data/
│  ├─ raw/          ← zip 파일 (Git에 포함)
│  └─ extracted/    ← 압축 해제본 (Git 제외, 각자 로컬)
├─ notebooks/       ← EDA 노트북들
└─ README.md
\```