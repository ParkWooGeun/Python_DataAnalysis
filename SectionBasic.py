import pandas as pd
import numpy as np  

def main():
    names = ['Bob', 'JES', 'Mary', 'John']
    births = [968, 155, 77, 578]
    custom = [1, 5, 25, 13]

    Baby = list(zip(names, births))
    df = pd.DataFrame(data=Baby, columns=['names', 'births'])

# #List형 출력
#     print(df.head(), end="\n\n")   

# #기본정보출력
#     print(df.dtypes, end="\n\n")

# #인덱스 정보
#     print(df.index, end="\n\n")

# #프레임 열의 형태정보
#     print(df.columns, end="\n\n")
# #하나의 열만 출력
#     print(df['names'], end="\n\n")  

# 특정 컬럼의 인덱스 몇개만 출력하기
#    print(df['names'].iloc[0:2])
    
# 조건 추가하여 선택 (예: births > 100)
#    print(df.loc[df['births'] >= 100, 'names','Births'])
    
    # errors='coerce'의미 births(문제가 있으면 NaN으로 // 열을 숫자형으로 변환)
    df['births'] = pd.to_numeric(df['births'], errors='coerce')

    # births 열의 평균만 출력
    print(df['births'].mean(), end="\n\n")



if __name__ == "__main__":
    main()
