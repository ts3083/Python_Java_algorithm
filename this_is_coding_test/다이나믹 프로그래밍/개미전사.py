"""
1줄 : 식량창고의 개수 N(3 <= N <= 100)
2줄 : 공백을 기준으로 각 식량창고에 저장된 식량의 개수 k가 주어짐(1000이하)

개미 전사가 얻을 수 있는 식량의 최댓값을 출력
인접한 창고를 공격하면 안됨 = 한 칸이상 띄어서 공격

ai = i번째 식량창고까지의 최적의 해 리스트
1 3 1 5
1 3 3 8 이므로 8을 출력
i번째의 최댓값을 구하는 법 : i - 1번째 최적의 해와 i - 2의 최적의 해에 i를 더한 값중에
더 큰 값을 i번째 최적의 해로 설정한다 (점화식)
"""
n = int(input())
cage = list(map(int, input().split()))
arr = [0] * n

arr[0] = cage[0]
arr[1] = max(cage[0], cage[1])

for i in range(2, n):
    sum = arr[i - 2] + cage[i]
    arr[i] = max(arr[i - 1], sum)
print(arr[n - 1])
