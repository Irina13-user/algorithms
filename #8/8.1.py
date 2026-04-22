count = 0
for number in range(100000, 1000000):
    current = str(number)
    for i in range(1, len(current)):
        if (current[i]<=current[i-1]) or ((int(current[i-1]) + int(current[i])) % 2 == 0):
            break
    else:
        count += 1
print(count)
