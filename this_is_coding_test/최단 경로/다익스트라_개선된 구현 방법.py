import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())  # 노드의 개수, 간선의 개수를 입력받기
start = int(input())  # 시작 노드 입력받기
graph = [[] for i in range(n + 1)]  # 각 노드의 인접한 노드의 정보를 담는 리스트 선언
distance = [INF] * (n + 1)  # 최단거리를 저장하는 테이블 만들기
# 방문처리를 하는 visited함수를 만들지 않아도 됨

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번노드에서 b번노드로 가는 비용이 c
    graph[a].append((b, c))


def dijkstra(start):
    q = []  # 최소힙 정렬을 위한 리스트 선언
    heapq.heappush(q, (0, start))  # (거리, 노드)의 형식으로 우선순위 큐 삽입
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면 반복실행
        dist, now = heapq.heappop(q)  # 지금까지의 최단거리의 노드를 pop
        # dist는 방문한 노드와 인접한 노드 중 최단거리 / now는 그 최단거리 노드의 노드
        if distance[now] < dist:
            # pop된 노드의 최단거리보다 distance에 갱신된 최단거리가 더 작다면 갱신 필요없음
            continue  # visited의 역할을 함

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))  # 갱신된 최단거리 정보를 저장


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
