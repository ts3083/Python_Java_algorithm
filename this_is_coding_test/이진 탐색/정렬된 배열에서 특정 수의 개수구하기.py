"""
n개의 원소를 포함하는 수열이 오름차순
이 수열에서 x가 등장하는 횟수를 계산

1 1 2 2 2 2 3에서 x = 2라면 4출력
시간복잡도 logn만족해야 함
"""
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

left = bisect_left(arr, x)
right = bisect_right(arr, x)
result = right - left

if (result == 0):
    print(-1)
else:
    print(result)
