from  math import inf
with open('24_6.txt') as file:
    lines = file.readlines()
min_count = inf
for line in lines:
    max_len = 0
    cur_len = 1
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            cur_len += 1
        else:
            max_len = max(max_len, cur_len)
            cur_len = 1
            symbol = line[i-1]
    min_count = min(line.count(symbol), min_count)
print(min_count)



