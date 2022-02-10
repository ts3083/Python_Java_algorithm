dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
arr = ['R', 'L', 'U', 'D']

num = int(input())
x, y = 1, 1
plans = input().split() # 리스트 입력받기
for plan in plans:
    for i in range(4):
        if (plan == arr[i]):
            nx = x + dx[i]
            ny = y + dy[i]
    if (nx >= 1 and ny >= 1 and nx <= num and ny <= num):
        x = nx
        y = ny    
print(x, y)