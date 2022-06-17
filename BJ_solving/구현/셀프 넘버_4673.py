dp = [False] * 10001
for i in range(1, 10001):
    if (i < 10):
        temp = i + i
    elif (i < 100):
        temp = i + i // 10 + i % 10
    elif (i < 1000):
        temp = i + i // 100 + i % 100 // 10 + i % 10
    elif (i < 10000):
        temp = i + i // 1000 + i % 1000 // 100 + i % 100 // 10 + i % 10
    if (temp <= 10000):
        dp[temp] = True

for i in range(1, 10001):
    if (dp[i] == False):
        print(i)
