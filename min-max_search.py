def min_search(number, min_num1, min_num2):
    if number < min_num1:
        return number, min_num1
    elif number < min_num2:
        return min_num1, number
    return min_num1, min_num2
def max_search(number, max_num1, max_num2):
    if number > max_num1:
        return number, max_num1
    elif number > max_num2:
        return max_num1, number
    return max_num1, max_num2
def initialise():
    global min_num2
    global min_num1
    global max_num1
    global max_num2
    number1 = int(input())
    number2 = int(input())
    if number1 > number2:
        number1, number2 = number2, number1
    min_num1, min_num2 = number1, number2
    max_num1, max_num2 = number2, number1
answer = input("do you know quantity of numbers? (y/n) ")
if answer.upper() == "Y" or answer.upper() == "YES":
    count = int(input("enter quantity of numbers: "))
    initialise()
    for _ in range(count - 2):
        number = int(input())
        min_num1, min_num2 = min_search(number, min_num1, min_num2)
        max_num1, max_num2 = max_search(number, max_num1, max_num2)
else:
    initialise()
    number = int(input())
    while number:
        min_num1, min_num2 = min_search(number, min_num1, min_num2)
        max_num1, max_num2 = max_search(number, max_num1, max_num2)
        number = int(input())
print(max_num1, max_num2, min_num1, min_num2)
