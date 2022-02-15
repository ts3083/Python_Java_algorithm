def dfs(graph, v, visited):
    # 방문하면 방문표시하고 노드를 출력
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:  # 그래프의 v번째 원소의 리스트를 순서대로 실행
        if not visited[i]:  # 방문하지 않아야 재귀적으로 실행
            dfs(graph, i, visited)


graph = [  # 그래프를 2차원 리스트로 표현
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9  # 각 노드가 방문된 정보를 표현
# 방문하지 않으면 False, 방문하면 True

dfs(graph, 1, visited)  # 정의된 dfs 함수 호출
