from collections import deque  # queue 사용을 위해 deque불러오기


def bfs(graph, start, visited):
    queue = deque([start])  # deque의 원소는 리스트이고 초기리스트 설정 = [1]
    visited[start] = True  # 방문처리
    while queue:
        # 큐가 빌때까지 반복
        v = queue.popleft()  # 제일 처음
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                # 방문하지 않은 인접노드를 큐에 넣고 방문처리


graph = [  # 그래프를 인접 리스트방식으로 작성
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

visited = [False] * 9
# 방문하지 않으면 False, 방문하면 True

bfs(graph, 1, visited)
