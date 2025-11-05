def сheck(a):
    first = 0
    second = len(str(a)) - 1
    palindrome = str(a)
    while first < second:
        if palindrome[first] != palindrome[second]:
            return "NO"
        first += 1
        second -= 1
    return "YES"

a = int(input())
print(сheck(a))
