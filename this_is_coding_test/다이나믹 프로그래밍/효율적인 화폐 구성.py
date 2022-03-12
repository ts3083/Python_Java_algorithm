"""
1줄 : 화폐의 갯수 N(100이하) / 총 금액 M(만개이하)
2줄부터 N개의 화폐의 가치가 주어짐

예를 들어 
2 15
2
3
이라면 13+2 / 12+3으로 생각하면 13원을 나누는데 필요한 최소화폐와 12원을 나누는데
필요한 최소화폐의 개수를 비교해서 더 작은 값으로 15의 화폐개수를 책정
보텀업 방식

M개 만큼의 배열이 필요하고 i를 화폐의 가치로 뺏을 때 0이 되야함
디폴트로는 -1로 하면 됨
1   2   3   4   5   6 7 8 9 10 11 12 13 14 15
-1  1   1   2   2   2
"""

n, m = map(int, input().split())
a = [10001] * (m + 1)
value = []

for i in range(n):
    x = int(input())
    value.append(x)

for i in range(1, m + 1):
    for elem_array in value:
        if (i - elem_array == 0):
            a[i] = 1
        elif (i - elem_array > 0):
            if (a[i - elem_array] != -1):
                a[i] = min(a[i], a[i - elem_array] + 1)

if (a[m] == 10001):
    print(-1)
else:
    print(a[m])
