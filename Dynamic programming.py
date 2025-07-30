numbers = [0] * 25
numbers[2] = 1
for i in range (3, 25):
    if i == 12:
        continue
    numbers[i] = numbers[i - 1]
    if i % 2 == 0:
        numbers[i] += numbers[i // 2]
    elif i == 11:
        continue
    numbers[i] = numbers[i - 1]
    if i % 2 == 0 and (i < 11 or i > 20):
        numbers[i] += numbers[i // 2]
print(numbers)
