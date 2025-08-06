with open('24_5.txt') as file:
    s = file.readline()
max_len = 0
cur_len = 0
correct = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E",
           "F", "G", "H", "I", "J", "K", "L", "M", "N")
for symbol in s:
    if symbol in correct:
        cur_len += 1
    else:
        max_len = max(max_len, cur_len)
        cur_len = 0
max_len = max(max_len, cur_len)
print(max_len)
