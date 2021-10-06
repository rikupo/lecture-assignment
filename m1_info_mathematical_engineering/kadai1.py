import numpy as np
import matplotlib.pyplot as plt
import math

import joblib
import itertools


def main():

    #d_list = [1.2,2,5,10]
    d_list = [1.7]
    for d in d_list:
        main2(d)

def main2(d):
    print(f"Alpha : {d}")
    ver = "ver4"
    print(np.sin(deg2rad(90)))
    epsilon = 1e-1000  # prevent zero divide
    loop_num = 1000
    #d = 1.2
    x_init = 1
    y_init = 1
    x_log = [x_init]
    y_log = [y_init]
    point = [[x_init,y_init]]
    for i in range(1,loop_num):
        z = (np.random.rand() + epsilon)
        r = z ** (-1/d)
        # print(f"{z} and {r}")
        theta = 2 * np.pi * np.random.rand()
        x = point[-1][0] + r*np.cos(theta)
        y = point[-1][1] + r*np.sin(theta)
        point.append([x,y])
        x_log.append(x)
        y_log.append(y)
    #print("fin")

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x_log,y_log, "o", linestyle='solid', color="black")
    ax.tick_params(bottom=False,
                   left=False,
                   right=False,
                   top=False)
    ax.tick_params(labelbottom=False,
                   labelleft=False,
                   labelright=False,
                   labeltop=False)
    ax.set_title("D= " + str(d))
    serial = np.random.randint(1,100)
    plt.savefig("C:/Users/tooyama/Desktop/情報数理01/" + str(ver)+ "-" + str(d) + str(f"-{serial}-") +str(".png"))

    r_log,cr_log = c_calc(point)

    #print(cr_log)

    for i in range(len(r_log)):
        if cr_log[i] > 0:
            cr_log = cr_log[i:]
            r_log = r_log[i:]
            print(cr_log)
            print(r_log)
            break
    try:
        off_set = 0
        #dc = (np.log(cr_log[i + 1])-np.log(cr_log[i]))/(np.log(r_log[i + 1])-np.log(r_log[i]))
        y = np.log(cr_log[i + off_set:i + off_set + 2])
        x = np.log(r_log[i + off_set:off_set + i + 2])
        print("to")
        print(f"x: {x}")
        print(f"y: {y}")
        dc = np.polyfit(x,y,1)
        hc = (cr_log[off_set + 10+ i] - cr_log[off_set+ i])/(r_log[off_set + 10+ i] - r_log[off_set+ i])
        print(f"hand calc is {hc}")

    except(RuntimeWarning):
        print("sorry")
        dc = None
    dc = dc[0]
    dc = 1.6367477253486983
    print(f"Dc : {dc}")
    fig1, ax1 = plt.subplots()
    ax1.plot(np.log(r_log), np.log(cr_log), "o", linestyle='solid', color="black")

    ax1.set_xlabel("log(r)")
    ax1.set_ylabel("logC(r)")
    ax1.set_title("D= " +str(d) +" Dc = " + str(dc))
    plt.savefig("C:/Users/tooyama/Desktop/情報数理01/"+ str(ver) + "-" + str(d) + "and" +str(f"{dc :.3f}") +".png")
    #plt.show()

def c_calc(point):

    n = len(point)
    # print(f'data length is {n}')
    point_s = sorted(point, key=lambda x: x[0])
    print(point_s)

    tiny_resol = 20
    tiny_resol_max = 0.5 # 10 ** 1
    # (i / tiny_resol) = tiny_resol_max
    r_list = [2 ** i for i in range(15)]
    #r_list_after = [10**(i) for i in range(1,7)]
    #r_list.extend(r_list_after)
    cr_list = []
    print(r_list)
    bef = 0
    for r in r_list:
        print(f'now r {r:.3f}', end="")
        counter = 0

        for i in range(n):
            # print(f'searching {i}/{n}',end="")
            for j in range(i + 1, n):
                #if r - point_s[i][0] - point_s[j][0] < 0: break  # x座標がrより遠い時点でブレイク
                if r - math.sqrt((point_s[i][0] - point_s[j][0]) ** 2 + (point_s[i][1] - point_s[j][1]) ** 2) > 0:
                    counter += 1
        cr_v = (2 * counter) / (n * (n - 1))
        plus = counter - bef
        bef = counter
        print(f' with {counter} points and c(r) : {cr_v} + {plus}')
        cr_list.append(cr_v)

    return r_list,cr_list

def search_upper():
    pass

def search_lower():
    pass

def deg2rad(deg):
    return deg * np.pi /180

if __name__ == "__main__":
    main()