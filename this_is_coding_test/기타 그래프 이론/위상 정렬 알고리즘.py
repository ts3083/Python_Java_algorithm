from collections import deque

v, e = map(int, input().split())  # 노드의 개수와 간선의 개수
indegree = [0] * (v + 1)  # 진입 차수 테이블
graph = [[] for i in range(v + 1)]  # 각 노드에 연결된 간선의 정보를 담는 그래프

# 간선의 정보 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # a 출발 b 도착
    indegree[b] += 1  # 진입 차수 +1


def topology_sort():  # 위상 정렬
    result = []  # 알고리즘 수행 결과를 담을 리스트
    q = deque()  # 큐 기능을 위한 deque 라이브러리 사용
    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:  # 큐가 빌 때까지 반복
        now = q.popleft()
        result.append(now)
        for i in graph[now]:  # now와 인접한 노드들의 진입차수 1 빼기
            indegree[i] -= 1
            if indegree[i] == 0:  # 진입차수가 0이 되면 큐에 삽입
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
