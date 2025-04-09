#1
# from itertools import count
#
# winner = 0
# n = int(input())
# loser = False
# for _ in range(n):
#     points = int(input())
#     winner = max(points, winner)
#     if not loser and (points == 0):
#         loser = True
# print (winner)
# if loser:
#     print("YES")
# else:
#     print("NO")

#2
# summ = 0
# count = 0
# number = int(input())
# while number:
#     if number % 8 == 0:
#         count += 1
#         summ += number
#     number = int(input())
# if summ:
#     print(round(summ / count, 3))
# else:
#     print("NO")
#3
min_value = 30000
n = int(input())
for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        min_value = min(number, min_value)
print(min_value)





