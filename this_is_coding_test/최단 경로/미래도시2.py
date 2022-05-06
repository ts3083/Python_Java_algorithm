# 플로이드 워셜 알고리즘을 이용
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1)for _ in range(n+1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    # a에서 b로 가는 비용은 c = graph원소는 a에서 b출발인 최소비용
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][k] + graph[k][x]

if(result >= INF):
    print(-1)
else:
    print(result)

