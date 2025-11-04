import pandas as pd

def main():
    names = ['Bob', 'JES', 'Mary', 'John']
    births = [968, 155, 77, 578]
    custom = [1, 5, 25, 13]

    Baby = list(zip(names, births))
    df = pd.DataFrame(data=Baby, columns=['names', 'births'])

    print(df.head())   # ✅ 이 줄이 핵심입니다

if __name__ == "__main__":
    main()
