
a = [[0.0], [2.002002002002002e-06], [6.006006006006006e-05], [0.004912912912912913], [0.08195995995995996]]
print(a[1])
print(len(a[0]))
a1 = a[1][0]
if a1 > 1:
    pass
x = [1,3,2,11]
y = [0,2,3,4]

point = [x,y]

print(point)

poin = [[0,0]]
poin.append([111,1])
poin.append([22,5])
poin.append([3,34])

print(sorted(poin, key=lambda x:x[0]))
print(poin[-1][0])

print(len(poin))

print(lambda poin:poin[0])

n = 10

print(list(range(10,13)))

if True: print(n)