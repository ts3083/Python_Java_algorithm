n = 5  # 데이터의 개수
m = 5  # 찾고자하는 부분합
data = [1, 2, 3, 2, 5]

count = 0
sum = 0
end = 0

for start in range(n):  # start를 차례대로 증가시키며 반복
    while sum < m and end < n:  # end를 가능한 만큼 이동시키기
        sum += data[end]
        end += 1
    if sum == m:
        count += 1
    sum -= data[start]

print(count)
