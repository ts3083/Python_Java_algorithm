import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())  # 노드의 개수 / 간선의 개수 입력받기
edges = []  # 모든 간선에 대한 정보를 담는 리스트 생성
dist = [INF] * (n + 1)  # 최단거리 테이블을 모두 INF으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())  # a에서 b도시로 가는 비용이 c
    edges.append((a, b, c))


def bellman_Ford(start):  # 벨만 포드 알고리즘
    dist[start] = 0  # 시작노드 초기화
    for i in range(n):  # 매 반복마다 "모든 간선"을 확인
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if (dist[cur] != INF and dist[next_node] > dist[cur] + cost):
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if (i == n - 1):
                    return True
    return False


negative_cycle = bellman_Ford(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])
