dp = [[0 for i in range(16)] for j in range(13)]
for i in range(16):
    dp[1][i] = 1
    # [1][i] -- 1-длина числа; i-любая цифра(последняя)
for i in range(1, 12):
    #i-длина
    for j in range(15, -1, -1):
        # j-последняя цифра для длины i
        for k in range(j-1, -1, -2):
            # k - следующая цифра после j
            dp[i + 1][j] += dp[i][k]
count = 0
for i in range(16):
    count += dp[12][i]
print(count)
print(dp[12])
