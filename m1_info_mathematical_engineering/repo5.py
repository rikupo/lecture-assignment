import numpy as np
import matplotlib.pyplot as plt
import math

import joblib
import itertools


def main():
    dir_name = r"C:\Users\tooyama\PycharmProjects\class-assignments\InfoMathEngRepo5-1"
    # theta固定で他の変数を色々やる感じ？？？
    k = 0.3
    epsi = 0.2
    theta = 0.5

    loopnum = 1000 # 同じパラメータでのループ数
    last_value = -0.3
    resol = 100 # パラメータ変化のステップ数

    solution_logger = []
    a_logger = []

        #print(a)

    k_list = [0.1,0.3,0.6,0.9]
    epsi_list = [0.1,0.3,0.6,0.9]
    alpha_list = [0.1,0.3,0.6,0.9,1.2,1.4,1.6,1.8]

    bef = last_value
    for k in k_list:
        for epsi in epsi_list:
            for alpha in alpha_list:
                print(f"k:{k} , epsilon {epsi}, alpha {alpha}")
                bef = last_value
                for theta in np.linspace(-0.1,1.1,100):
                    for loops in range(loopnum+int(0.1*loopnum)):
                        next = k*bef - alpha * math.tanh(bef/epsi) + theta
                        if loops >= loopnum*0.99:
                            a_logger.append(theta)
                            solution_logger.append(next)
                            #print(f"{a} : {next}")
                        bef = next

                fig = plt.figure(f"test")
                plt.plot(a_logger,solution_logger, marker='.', markersize=1, color="black", linestyle="None")
                # plt.plot(predict, marker='+', label="predicted", markersize=14, linestyle="None", color="blue", linewidth=10)
                plt.xlabel(r"$\theta$")
                plt.ylabel(r"$\sigma$(t)")

                plt.title(f"k= {k} ," r"$\alpha$" f"={alpha} ," r"$\epsilon$ = " f"{epsi}")
                save_name = dir_name + "\\" + f"k{k}-alpha{alpha}-epsi{epsi}"
                fig.savefig(f"{save_name}.png")
                plt.clf()
                plt.close()
                solution_logger = []
                a_logger = []
            #return 0
    #plt.show()

if __name__ == "__main__":
    main()