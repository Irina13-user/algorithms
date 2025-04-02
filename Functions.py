def quantity_of_numbers(number):
    while number:
        count = 0
        number // 10
        count += 1
    return count
def sum_of_numbers(number):
    while number:
        sum = 0
        sum += number % 10
    return sum
def quantity_of_divisors(number):
    quantity = 1
    if number % 2 == 0:
        quantity += 1
    elif number % 3 == 0:
        quantity += 1
    elif number % 5 == 0:
        quantity += 1
    elif number % 7 == 0:
        quantity += 1
    elif number % 11 == 0:
        quantity += 1
    elif number % 13 == 0:
        quantity += 1
    return quantity

number = int(input())
print(quantity_of_numbers(number))
print(sum_of_numbers(number))
print(quantity_of_divisors(number))


