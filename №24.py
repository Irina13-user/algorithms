with open('24-a') as F:
    s  = F.readline()
car = 1
max_l = 0
for i in range(1, len(s)):
    if s[i] == a and s[i + 1] == b or s[i + 1] == a and s[i] == b:
        car = 1
    else:
        car += 1
        max_l = max(max_l, car)
print(max_l)