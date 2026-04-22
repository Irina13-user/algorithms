"""
def F_1(x, y, w, z):
    if ((x <= y) == (w or not(z))) == 1:
        return 1
    else:
        return 0
def F_2(x, y, w, z):
    if ((x <= y) and (not(w) == z)) == 1:
        return 1
    else:
        return 0
print("x y w z f1 f2")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                print(x, y, w, z, " ", F_1(x, y, w, z),F_2(x, y, w, z))
"""
n = int(input())
for n in range(100, 1, -1):
    s = bin(n)[2:]
    s = str(s)
    s += str(s.count ("1")%2)
    s += str(s.count ("1")%2)
    r = int(s, 2)
    if r < 100:
        print(r)
        break
