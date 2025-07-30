with open('1_24.txt') as file:
    s = file.readline()
max_len = 0
cur_len = 1
cur_sym = s[0].isdigit()
for i in range(1, len(s)):
    if cur_sym and not s[i].isdigit():
        cur_len += 1
    elif not cur_sym and s[i].isdigit():
        cur_len += 1
    else:
        max_len = max(max_len, cur_len)
        cur_len = 0
    cur_sym = s[i].isdigit()
max_len = max(max_len, cur_len)
print(max_len)