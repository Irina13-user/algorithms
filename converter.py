# def convert_from_N_to_10(number, n):
#     result = 0
#     exponent = 0
#     while number:
#         exponent += 1
#         result += (number % 10) * n**exponent
#         number //= 10
def convert_from_10_to_N(number, n):
    quotient = 0
    result = 0
    intermediate = 1
    while number:
        quotient = number % n
        quotient *= intermediate
        result += quotient
        intermediate *= 10
        number //= n
        quotient = 0
    return result
number = int(input())
n = int(input())
print(convert_from_10_to_N(number, n))