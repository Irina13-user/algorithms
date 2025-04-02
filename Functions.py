def quantity_of_digits(number):
    count = 0
    while number:
        number //= 10
        count += 1
    return count
def sum_of_digits(number):
    sum = 0
    while number:
        sum += number % 10
        number //= 10
    return sum
def quantity_of_divisors(number):
    quantity = 2
    for divisor in range(2, int(number ** .5)):
        if number % divisor == 0:
            quantity += 2
    if number % (int(number ** .5)) == 0:
        quantity += 1
    return quantity

number = int(input())
print(quantity_of_digits(number))
print(sum_of_digits(number))
print(quantity_of_divisors(number))