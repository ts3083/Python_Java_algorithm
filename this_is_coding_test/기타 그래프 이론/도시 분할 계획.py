N, M = map(int, input().split())  # 집의 개수, 길의 개수

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i  # parent의 루트 노드 초기화


def find_parent(parent, x):
    if (parent[x] != x):
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b


edges = []
last_cost = 0
result = 0

for _ in range(M):
    a, b, c = map(int, input().split())  # a번 집, b번 집, 유지비 c
    edges.append((c, a, b))

edges.sort()

for e in edges:
    c, a, b = e
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += c
        last_cost = c

print(result - last_cost)
