# 2
def calculate_time(n):
    f = {}
    g = {}
    def F(n):
        if n in f:
            return f[n]
        if n == 1:
            f[n] = 1
            return 1
        f[n] = G(n) + F(n - 1) + n
        return f[n]
    def G(n):
        if n in g:
            return g[n]
        if n == 1:
            g[n] = 2
            return 2
        g[n] = G(n - 1) + 2*n
        return g[n]


n = int(input())
time = calculate_time(n)
print(time)





"""
t1, p1 = (input()).split()
t2, p2 = (input()).split()
t1 = int(t1)
p1 = int(p1)
t2 = int(t2)
p2 = int(p2)
s = int(input())
if s - t1 >=0:
    d1 = (s - t1) // p1 + 1
else:
    d1 = 0
if s - t2 >= 0:
    d2 = (s - t2) // p2 + 1
else:
    d2 = 0
print(d1 + d2)
"""
