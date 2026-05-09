from itertools import product
alphabet = "012345678"
count = 0
for combination in product(alphabet, repeat = 5):
    if combination[0] > combination[1] > combination[2] > combination[3] > combination[4]:
        count += 1
print(count)