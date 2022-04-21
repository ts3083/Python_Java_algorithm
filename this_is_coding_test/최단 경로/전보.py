import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))  # 도착 도시 / 시간

distance = [INF] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):
            continue
        for node in graph[now]:  # 시작노드와 인접한 노드의 정보를 모두 확인
            # 지금 node[0]의 노드에 저장된 최단거리하고 now를 거쳐올 때의 최단거리의 비교
            cost = dist + node[1]
            if (cost < distance[node[0]]):
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))


dijkstra(c)

cnt = 0
max = 0
for i in range(1, n + 1):
    if (distance[i] == INF):
        cnt += 1
    elif (max < distance[i]):
        max = distance[i]

print((n - 1) - cnt, max)  # 자기자신인 출발노드를 빼주어야 함
