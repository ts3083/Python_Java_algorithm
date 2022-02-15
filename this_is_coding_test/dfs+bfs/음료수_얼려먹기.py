n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))  # 리스트 안에 리스트를 입력받아서 삽입

# 바로 상하좌우를 방문하면서 0을 1로 바꾸는 재귀함수 작성


def visit(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return  # 범위를 벗어나면 그냥 종료
    if graph[x][y] == 0:
        graph[x][y] = 1  # 방문표시
        visit(x - 1, y)  # 상
        visit(x + 1, y)  # 하
        visit(x, y - 1)  # 좌
        visit(x, y + 1)  # 우
    return


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            visit(i, j)
            cnt += 1
print(cnt)
