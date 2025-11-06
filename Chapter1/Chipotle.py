import numpy as np
import pandas as pd
from pathlib import Path


# 스크립트 기준으로 안전한 경로 생성
# file_path: pathlib.Path 또는 문자열(파일 경로) — 파일 위치 지정.
# sep='\t': 열 구분자가 탭 문자임을 의미(TSV 파일 읽기).
# 반환값: pandas.DataFrame (여기서는 변수 chip에 저장).
# 자주 쓰는 옵션: header, names, index_col, usecols, dtype, encoding, parse_dates, na_values, skiprows 등.
def Chipotle():
    # 스크립트 기준으로 안전한 경로 생성
    file_path = Path(__file__).parent / 'chipotle.tsv'

    if not file_path.exists():
        print("파일 없음:", file_path)
        return

    chip = pd.read_csv(file_path, sep='\t', encoding='utf-8')
    #print(chip.shape)   # (rows, columns) 형태 출력
    #chip.info()         # info()는 자체 출력하므로 print()로 감싸지 않음

#   chip.head(10)         # head()는 자체 출력하므로 print()로 감싸지 않음
#    print(chip.columns)

# order_id 열의 데이터 타입을 'category'로 변환
#    chip['order_id'] = chip['order_id'].astype('category')
# describe() - 기초 통계량 출력 (숫자 형 열에 대해서만 계산)
#    print(chip.describe())
# unique() - 고유값 값 출력  
 #   print(chip['item_name'].unique())

# unique() - 고유값 개수 출력  
 #   print(len(chip['item_name'].unique()))

#   #가장 많이 주문한 상위 10개 아이템 출력
#     item_counts = chip['item_name'].value_counts()[:10]
#     print(item_counts)
    
    # 아이템별 주문 갯수 출력 갯수는 count , 합계는 sum
    # ordered_item_counts = chip.groupby('item_name')['order_id'].count()[:10]
    # print(ordered_item_counts)

# unique(): 고유값 목록(원래 등장 순서) 반환. 타입: ndarray.
# value_counts(): 각 고유값의 빈도(개수)를 내림차순 정렬한 Series 반환.
    #print(chip['item_price'].head())           # 고유값 배열
    
    chip['item_price'] = chip['item_price'].apply(lambda x: float(x[1:]))  # '$' 제거 후 float 변환
    chip.describe()

if __name__ == "__main__":
    Chipotle()