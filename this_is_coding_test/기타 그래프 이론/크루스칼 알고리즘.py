# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):  # 두 원소가 속한 집합을 합치기(Union 연산)
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())  # 노드의 개수와 간선의 개수
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# parent 테이블에서 루트 노드를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 간선 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # 비용을 기준으로 오름차순 정렬하기 위해 첫 번째 원소는 비용

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 아니면 신장 트리 포함, 아니면 아무것도 하지 않음
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost  # 비용을 count

print(result)
