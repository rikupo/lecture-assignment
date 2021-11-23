import numpy as np
import matplotlib.pyplot as plt
import math

import joblib
import itertools


def main():
    dir_name = r"C:\Users\tooyama\PycharmProjects\class-assignments\InfoMathEngRepo5"
    # theta固定で他の変数を色々やる感じ？？？
    k = 0.3
    epsi = 0.2
    theta = 0.1

    loopnum = 1000 # 同じパラメータでのループ数
    last_value = -0.3
    resol = 10 # パラメータ変化のステップ数

    a_resol = 1000



    solution_logger = []
    a_logger = []

        #print(a)
    bef = last_value

    bef = last_value
    for a in range(0, a_resol + int(0.1 * a_resol)):
        a = a / a_resol
        for loops in range(loopnum):
            next = k*bef - a * math.tanh(bef/epsi) + theta
            if loops >= loopnum*0.99:
                a_logger.append(a)
                solution_logger.append(next)
                #print(f"{a} : {next}")
            bef = next

    fig = plt.figure(f"test")
    plt.plot(a_logger,solution_logger, marker='.', markersize=1, color="black", linestyle="None")
    # plt.plot(predict, marker='+', label="predicted", markersize=14, linestyle="None", color="blue", linewidth=10)
    plt.xlabel('a')
    plt.ylabel('sigma')

    plt.title(f"k= {k} , " r"$\alpha$=" + f"{a} , " r"$\epsilon$ = " f"{epsi} , " r"$\theta$" f" = {theta}")
    save_name = dir_name + "\\" + f"k{k}-alpha{a}-epsi{epsi}-theta{theta}"
    fig.savefig(f"{save_name}.png")
    solution_logger = []
    a_logger = []
    #return 0
    plt.show()

if __name__ == "__main__":
    main()