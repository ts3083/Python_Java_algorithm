"""
1줄 : 떡의 개수 N / 요청한 떡의 길이 M이 주어짐(N은 백만개 이하 + M은 20억 이하)
2초의 제한시간 + int형을 사용하면 20억의 수까지 표현가능하므로 int형 사용한다

2줄 : N개 떡의 개별 높이가 각각 주어짐

결국 M만큼의 떡을 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값
= 손님한테 최소한만을 줄 수 있는 경우

리스트를 오름차순 정렬
절단기 길이가 길수록 손님한테 주는 떡 길이는 줄어든다
반대로 절단기 길이가 짧아지면 손님한테 주는 떡 길이는 늘어난다

중간부터 중간데이터로 절단기의 길이를 설정했을 경우 =
1. 남는 떡 길이의 합 < M -> 절단기 길이 낮추기
2. 남는 떡 길이의 합 >= M -> 절단기 길이 늘리기
"""

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, result = 0, 0
end = max(arr)

while (start <= end):
    sum = 0  # sum은 반복문 실행될 때 0으로 초기화되어 있어야함
    height = (start + end) // 2
    for elem in arr:
        if elem > height:
            sum += (elem - height)
    if (sum >= m):  # sum이 더 큰 경우의 코드가 실행된 마지막 경우의 height를 출력
        start = height + 1
        result = height
    else:
        end = height - 1

print(result)
# 10 13 15 17   4 3     8 13 15
# 10 15 17 19   4 6     9 14 17
"""
height를 출력하면 생기는 오류 = 딱 맞는 값이 나오면 상관없지만
만약 딱 떨어지지않는 값이 나오면 최대값이 출력되어야 하기 때문에 수정이 필요
"""
