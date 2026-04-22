sum_of_numbers = 0
min_dif1 = 10000
min_dif2 = 10000
with open("inf_22_10_20_27a.txt") as file:
    n = int(file.readline())
    for line in file:
        num1, num2 = map(int, line.split())
        num1, num2 = max(num1, num2),min(num1, num2)
        sum_of_numbers += num1
        if (num1 - num2) % 3 == 1:
            min_dif1 = min(min_dif1, num1 - num2)
        if (num1 - num2) % 3 == 2:
            min_dif2 = min(min_dif2, num1 - num2)
if sum_of_numbers % 3 == 0:
    print(sum_of_numbers)
elif sum_of_numbers % 3 == 1:
    print(sum_of_numbers - min_dif1)
else:
    print(sum_of_numbers - min_dif2)
