n = int(input())
ability = list(map(int, input().split()))

a = [1] * n  # ability[i]를 마지막 원소로 가지는 부분 수열의 최대길이

ability.reverse()  # 증가하는 배열로 바꾸기
# 배열의 총 원소 수에서 증가하는 배열의 최대길이를 빼면 열외시켜야 하는 병사의 수이다
# 4 2 5 8 4 11 15
# 1 1 2 3

for i in range(1, n):
    for j in range(i):
        if (ability[i] > ability[j]):
            a[i] = max(a[i], a[j] + 1)

print(n - max(a))
