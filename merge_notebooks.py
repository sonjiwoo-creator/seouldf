import json

# 파일 불러오기
with open('notebooks/nagyung_eda.ipynb', encoding='utf-8') as f:
    eda1 = json.load(f)
with open('notebooks/nagyung_eda_인구.ipynb', encoding='utf-8') as f:
    eda2 = json.load(f)
with open('main.ipynb', encoding='utf-8') as f:
    main = json.load(f)

# 구분 마크다운 셀 추가
divider1 = {'cell_type': 'markdown', 'metadata': {}, 'source': ['## 나경 EDA - 상권변화지표']}
divider2 = {'cell_type': 'markdown', 'metadata': {}, 'source': ['## 나경 EDA - 직장인구/상주인구']}

# main에 붙이기
main['cells'] += [divider1] + eda1['cells'] + [divider2] + eda2['cells']

# 저장
with open('main.ipynb', 'w', encoding='utf-8') as f:
    json.dump(main, f, ensure_ascii=False, indent=1)

print('완료!')