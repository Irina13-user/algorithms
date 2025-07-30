numbers = [0] * 25
numbers[2] = 1
for i in range (3, 11):
    numbers[i] = numbers[i - 1]
    if i % 2 == 0:
        numbers[i] += numbers[i // 2]
numbers[11] = numbers[10]
numbers[12] = numbers[6]
for i in range (13, 25):
    numbers[i] = numbers[i - 1]
    if i % 2 == 0 and i < 20:
        numbers[i] += numbers[i // 2]
numbers = {n: numbers[n] for n in range(25)}
print(numbers)
