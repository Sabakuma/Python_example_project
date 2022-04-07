a = input("x=")
x = int(a)
b = input("Y=")
y = int(b)

def xpery(X,Y):
    for i in range(1,X):
        if i % Y == 0:
            print(i)


def xeven(X):
    lst = []
    for i in range(1,X):
        if i % 2 == 0:
            lst.append(i)
    return lst

#print("XまでのうちYで割り切れるのは")
#xpery(X,Y)

print("Xまでの偶数は")
result = xeven(x)
print(result)
