s = input() #현재 나이트의 위치 입력받기
sero = "abcdefgh"
garo = [1, 2, 3, 4, 5, 6, 7, 8]
dx = [-2, -2, -1, 1, 2, 2, -1, 1]
dy = [1, -1, -2, -2, 1, -1, 2, 2]
count = 0

y = sero.find(s[0])
x = int(s[1])
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if (nx < 1 or ny < 1 or nx > 8 or ny > 8): #유효하지 않다면
        continue
    count += 1
print(count)