INF = int(1e9)  # 무한을 의미

n, m = map(int, input().split())  # 노드의 개수 / 간선의 개수 입력받기
graph = [[INF]*(n + 1) for _ in range(n + 1)]  # INF로 초기화된 2차원 배열 만들기

# 자기자신으로 가는 비용은 0으로 초기화 해주기
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if (a == b):
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받기
for _ in range(m):
    # a에서 b로 가는 비용은 c = graph원소는 a에서 b출발인 최소비용
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):  # 1번 노드부터 경유할 노드를 하나씩 설정
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()  # 줄바꿈 기능
