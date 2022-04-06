a = input("x=")
X = int(a)
b = input("Y=")
Y = int(b)

def xpery(X,Y):
    for i in range(1,X):
        if i % Y == 0:
            print(i)


def xeven(X,Y):
    for i in range(1,X):
        if i % 2 == 0:
            print(i)

print("XまでのうちYで割り切れるのは")
xpery(X,Y)

print("Xまでの偶数は")
xeven(X,Y)