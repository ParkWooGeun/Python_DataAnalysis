import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

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
    
    # # errors='coerce'의미 births(문제가 있으면 NaN으로 // 열을 숫자형으로 변환)
    # df['births'] = pd.to_numeric(df['births'], errors='coerce')

    # # births 열의 평균만 출력
    # print(df['births'].mean(), end="\n\n")

# # numpy 배열 생성 및 출력 (arang - 15까지 숫자 생성, reshape - 3행 5열로 변환)
#     arr1 = np.arange(15).reshape((3, 5))    
#     print(arr1, end="\n\n")

# # 배열의 형태 출력
#     print(arr1.shape)

# # 배열의 차원 출력
#     print(arr1.ndim)    

# #zeros 함수로 3행 4열의 배열 생성
#     arr2 = np.zeros((3, 4)) 
#     print(arr2, end="\n\n")

# # 같은 형태 -> 가능
# import numpy as np
# a = np.arange(12).reshape(3,4)   # shape (3,4)
# b = np.ones((3,4))
# print((a + b).shape)             # (3,4)

# # (3,4) + (4,) -> 오른쪽부터 비교: 4==4, 3 vs (없음->1) -> 가능 (b가 (1,4)로 브로드캐스트)
# c = np.array([1,2,3,4])         # shape (4,)
# print((a + c).shape)            # (3,4)

# # (3,4) + (3,1) -> 두번째 축이 1이라 가능
# d = np.array([[1],[2],[3]])     # shape (3,1)
# print((a + d).shape)            # (3,4)

# # 호환 불가 예: (3,4) + (2,)
# e = np.array([1,2])             # shape (2,)
# # a + e  # ValueError: operands could not be broadcast together

#막대그래프 그리기 plt.bar()
    # x = df['names']     
    # y = df['births']
    # plt.bar(x, y)
    # plt.xlabel('Names')
    # plt.ylabel('Births')
    # plt.title('Bar Graph of Births by Name')
    # plt.show()

    # # 산점도 그래프출력하기 plat.scatter()
    # plt.scatter(x, y)
    # plt.xlabel('Names')
    # plt.ylabel('Births')
    # plt.title('Scatter Plot of Births by Name')
    # plt.show()
    
if __name__ == "__main__":
    main()
