answer = input("do you know quantity of numbers? (y/n) ")
if answer.upper() == "Y" or  answer.upper() == "YES":
    count = int(input("enter quantity of numbers: "))
max_num1 = max_num2 = min_num1 = min_num2 = int(input())
for _ in range(count - 1):
    number = int(input())
    if number < min_num1:
        min_num2 = min_num1
        min_num1 = number
    elif number < min_num2:
        min_num2 = number
    elif number > max_num1:
        max_num2 = max_num1
        max_num1 = number
    elif number > max_num2:
        max_num2 = number
print(max_num1, max_num2, min_num1, min_num2)
