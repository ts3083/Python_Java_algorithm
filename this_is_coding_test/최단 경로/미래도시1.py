# 다익스트라 알고리즘을 이용한 방식
import sys
import heapq
input = sys.stdin.readline
INF = int(1000)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1)) # 도착 도시, 시간
    graph[b].append((a, 1))

x, k = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (n + 1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        time, now = heapq.heappop(q) # pop한 노드 인접노드의 시간과 노드
        if (distance[now] < time):
            continue
        for i in graph[now]:
            cost = time + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]

result = dijkstra(1, k) + dijkstra(k, x)

if(result >= INF):
    print(-1)
else:
    print(result)

