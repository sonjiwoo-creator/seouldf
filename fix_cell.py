import json

with open('c:/sparta/project/03_final/seouldf/notebooks/RFM_EDA_진행.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_source = [
    "# %% 임대료 기준 상권 필터링\n",
    "# 자치구별 월세 중앙값으로 진입 비용 부담이 낮은 상권 추출\n",
    "\n",
    "임대료_기준 = 60  # 만원 (이 값을 바꿔서 기준 조정 가능)\n",
    "\n",
    "df_임대료필터 = rfm_clean[rfm_clean['월세_임대료_중앙값'] <= 임대료_기준].copy()\n",
    "\n",
    "n_전체 = len(rfm_clean)\n",
    "n_필터 = len(df_임대료필터)\n",
    "pct = n_필터 / n_전체 * 100\n",
    "print('=== 월세', 임대료_기준, '만원 이하 상권 필터링 결과 ===')\n",
    "print(f'전체 {n_전체}개 중 {n_필터}개 ({pct:.1f}%)')\n",
    "print()\n",
    "\n",
    "# 상권분류 분포\n",
    "print('[ 상권분류 분포 ]')\n",
    "print(df_임대료필터['상권분류'].value_counts())\n",
    "print()\n",
    "\n",
    "# 저평가 가치주 중 임대료 저렴한 곳 Top 10\n",
    "print('[ 저평가 가치주 + 저임대료 Top 10 (결제건수 기준) ]')\n",
    "mask = df_임대료필터['상권분류'] == '저평가_가치주'\n",
    "df_추천 = df_임대료필터[mask].sort_values('F_결제건수', ascending=False).head(10)\n",
    "cols = ['상권_코드_명', '자치구_코드_명', '월세_임대료_중앙값', 'F_결제건수', 'M_객단가', 'R_매출증감률', 'RFM_합계']\n",
    "print(df_추천[cols].to_string(index=False))\n",
    "print()\n",
    "\n",
    "# 자치구별 통과 상권 수\n",
    "print('[ 자치구별 필터 통과 상권 수 ]')\n",
    "print(df_임대료필터.groupby('자치구_코드_명')['상권_코드'].count().sort_values(ascending=False).to_string())\n"
]

nb['cells'][10]['source'] = new_source
nb['cells'][10]['outputs'] = []
nb['cells'][10]['execution_count'] = None

with open('c:/sparta/project/03_final/seouldf/notebooks/RFM_EDA_진행.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print('완료')
