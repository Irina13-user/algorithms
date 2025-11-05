numbers = [1, 2, 3, 4, 5]
length = len(numbers)
for i in range(30):
    print(f"iteration #{i + 1} calling {numbers[i % length]}")