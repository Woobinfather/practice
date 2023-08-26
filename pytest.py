import matplotlib.pyplot as plt  # matplotlib 라이브러리를 불러온다.
import random  # 랜덤 모듈을 불러온다.
import pandas as pd
import numpy as np


result = []
for i in range(100):
    dice1 = random.randint(1, 6)  # 1부터 6까지의 랜덤한 정수를 dice1 변수에 저장한다.
    dice2 = random.randint(1, 6)  # 1부터 6까지의 랜덤한 정수를 dice2 변수에 저장한다.
    dice3 = random.randint(1, 6)  # 1부터 6까지의 랜덤한 정수를 dice3 변수에 저장한다.

    total = dice1 + dice2 + dice3  # 세 주사위의 합을 구한다.

    print("첫 번째 주사위: ", dice1)  # 첫 번째 주사위의 눈을 출력한다.
    print("두 번째 주사위: ", dice2)  # 두 번째 주사위의 눈을 출력한다.
    print("세 번째 주사위: ", dice3)  # 세 번째 주사위의 눈을 출력한다.
    print("주사위 합계: ", total)  # 세 주사위의 합을 출력한다.
    result.append(total)

print("최종 결과")
print(result)

df = pd.DataFrame(result)
plt.show(df)


def show_bar_chart(df):  # df를 인자로 받는 show_bar_chart 함수를 정의한다.
    df.plot(kind='bar')  # df를 막대그래프로 그린다.
    plt.show()  # 그래프를 출력한다.
