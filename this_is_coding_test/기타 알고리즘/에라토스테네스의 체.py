import math

n = int(input())  # 2부터 n까지의 수 중에서 소수를 모두 출력
arr = [True for i in range(n + 1)]  # 처음에는 모든 수가 소수로 설정

for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n까지 모든 소수 판별(약수의 성질 활용)
    if (arr[i] == True):  # i가 소수로 남아있을 경우
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if arr[i] == True:
        print(i, end=' ')
