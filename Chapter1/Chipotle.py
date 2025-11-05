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
    print(chip.shape)   # (rows, columns) 형태 출력
    chip.info()         # info()는 자체 출력하므로 print()로 감싸지 않음

if __name__ == "__main__":
    Chipotle()