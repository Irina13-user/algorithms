from time import time

def get_numbers():
    for number in range(10**7):
        tmp = str(number)
        if '0' in tmp and '1' in tmp and '5' in tmp:
            yield number

start = time()

count = 0
for number in get_numbers():
    tmp = str(number)
    if '9' in tmp:
        count += 1
print(count)

end = time()
print(end - start)
