with open('24_8.txt') as file:
    s = file.readline()
a_in_line = 0
start = True
for sign in s:
    cur_sign = s[sign]
    if cur_sign == "F":
        start == True

