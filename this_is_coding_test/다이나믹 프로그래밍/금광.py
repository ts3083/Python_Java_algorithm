t = int(input())

for test in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    h = 0
    graph = [[0] * m for _ in range(n)]
    for col in range(n):
        for row in range(m):
            graph[col][row] = array[h]
            h += 1

    a = [[0] * m for _ in range(n)]
    for x in range(n):
        a[x][0] = graph[x][0]  # 초기값 설정

    dx = [-1, 0, 1]

    for j in range(1, m):
        for i in range(n):
            for k in range(3):
                nx = i + dx[k]
                ny = j - 1
                if (nx < 0 or ny < 0 or nx >= n or ny >= m):
                    continue
                a[i][j] = max(a[nx][ny] + graph[i][j], a[i][j])

    print(max(map(max, a)))
