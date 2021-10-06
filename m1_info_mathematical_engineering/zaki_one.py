import random
import numpy as np
import matplotlib.pyplot as plt
import joblib
import itertools


def calc_r(x,y,N,i):
    R_list = []
    print(f"now  i - {i}")
    for j in range(i + 1, N):
        R_list.append(np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2))
    R_list.sort()
    return R_list

N = 10000       # Levy's Dustの反復回数
alpha = 10      # Levy's Dustの冪指数
z_min = 0.001   # 一様乱数zの最小値

x = [0]
y = [0]
for i in range(N-1):
    z = random.uniform(z_min, 1.0)
    r = z ** (-1/alpha)
    theta = 2 * np.pi * random.random()
    x.append(x[i] + r * np.cos(theta))
    y.append(y[i] + r * np.sin(theta))

plt.xlabel('x')
plt.ylabel('y')
plt.tick_params(direction='in')
plt.plot(x, y, marker='o', ms=2)
plt.savefig(f'./result/walk_{alpha}.png')

plt.clf()
plt.close()

print(f'Saved "./result/walk_{alpha}.png"')

R_list_result = joblib.Parallel(n_jobs=-1)(joblib.delayed(calc_r)(x,y,N,i) for i in range(N))
R_list = list(itertools.chain.from_iterable(R_list_result))

s = 0
c = 0
log_r = []
log_C = []
for r in [np.e**(x/100) for x in range(-100, 600)]:
    for i in range(s, len(R_list)):
        print(f"now2  r - {r} {i}")
        if r-R_list[i] <= 0:
            break
        c += 1
    C = c * 2/(N*(N-1))
    log_r.append(np.log(r))
    log_C.append(np.log(C))
    s = i

D, _ = np.polyfit(log_r, log_C, 1)

plt.xlabel('log(r)')
plt.ylabel('log{C(r)}')
plt.tick_params(direction='in')
plt.plot(log_r, log_C, label=f'D={D:.3f}')
plt.legend()
plt.savefig(f'./result/ICF_{alpha}.png')
plt.clf()
plt.close()
print(f'Saved "./result/ICF_{alpha}.png"')
print(f'alpha={alpha}, D={D:.3f}')
