import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 뜻하는 int형에서 가장 큰 값을 INF로 설정

n, m = map(int, input().split())  # 노드의 개수, 간선의 개수를 입력받기
start = int(input())  # 시작 노드 입력받기
graph = [[] for i in range(n + 1)]  # 각 노드의 인접한 노드의 정보를 담는 리스트 선언
visited = [False] * (n + 1)  # 방문여부를 확인하는 리스트 만들기
distance = [INF] * (n + 1)  # 최단거리를 저장하는 테이블 만들기

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번노드에서 b번노드로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환하는 함수 - 완전 탐색


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:  # 방문하지 않은 노드 중 최단거리의 원소찾기
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘


def dijkstra(start):
    distance[start] = 0  # 시작노드 초기화
    visited[start] = True
    for j in graph[start]:  # 1번 노드와 인접한 [노드, 비용]을 j로 순서대로 확인
        distance[j[0]] = j[1]  # 처음에는 시작노드와 가까운 노드와의 거리로 무조건 갱신

    for i in range(n - 1):
        now = get_smallest_node()  # 현재 최단거리가 가장 짧은 노드를 now로 저장
        visited[now] = True
        for j in graph[now]:
            # 현재 노드까지 최단거리와 다음 노드의 최단거리 합을 cost로 저장
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
