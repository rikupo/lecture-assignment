import numpy as np
import matplotlib.pyplot as plt
import math

def main():

    d_list = [1.2,2,5,10]
    for d in d_list:
        main2(d)

def main2(d):

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
    print("fin")

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
    plt.savefig("C:/Users/tooyama/Desktop/情報数理01/" + str(d) + ".png")
    #plt.figure()


    r_log,cr_log = c_calc(point,10,2)

    dc = (np.log(cr_log[1])-np.log(cr_log[0]))/(np.log(r_log[1])-np.log(r_log[0]))
    print(dc)
    fig1, ax1 = plt.subplots()
    ax1.plot(np.log(r_log), np.log(cr_log), "o", linestyle='solid', color="black")

    ax1.set_xlabel("log(r)")
    ax1.set_ylabel("logC(r)")
    ax1.set_title("D= " +str(d) +" Dc = " + str(dc))
    plt.savefig("C:/Users/tooyama/Desktop/情報数理01/" + str(d) + "and" +str(dc)+".png")
    #plt.show()

def c_calc(point,max_pow,resolution):

    n = len(point)
    print(f'data length is {n}')
    point_s = sorted(point, key=lambda x: x[0])
    print(point_s)

    cr_log= []
    r_log = []

    cr_v_flag = -1
    tiny_resol = 20
    tiny_resol_max = 0.5 # 10 ** 1
    # (i / tiny_resol) = tiny_resol_max
    r_list = [10 ** (i / tiny_resol) for i in range(1, int(tiny_resol_max * tiny_resol))]
    r_list_after = [10**(i/resolution) for i in range(int(tiny_resol_max + 1),int(max_pow*resolution))]
    r_list.extend(r_list_after)

    print(r_list)
    for k in r_list:
        r = k
        print(f'now r {int(r)}',end="")
        counter = 0
        for i in range(n):
            # print(f'searching {i}/{n}',end="")
            for j in range(i+1, n):
                if point_s[i][0] - point_s[j][0] > r: break # x座標がrより遠い時点でブレイク
                if math.sqrt((point_s[i][0] - point_s[j][0])**2 + (point_s[i][0] - point_s[j][0])**2) < r:
                    counter += 1
        cr_v = 2 * counter/(n*(n-1))
        print(f' with {counter} points and c(r) : {cr_v}')
        r_log.append(r)
        cr_log.append(cr_v)
        if cr_v_flag > 0:
            print("reached max r exiting")
            break
        if cr_v == 1.0:
            cr_v_flag = 1
    return r_log,cr_log



def search_upper():
    pass

def search_lower():
    pass

def deg2rad(deg):
    return deg * np.pi /180

if __name__ == "__main__":
    main()