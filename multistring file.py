with open('multistring.txt', encoding='UTF-8') as file:
    lines = file.readlines()
for i in range(len(lines)):
    if "\n" in lines[i]:
        lines[i] = lines[i][:-1]
max_len = max(lines, key=len)
print(max_len)