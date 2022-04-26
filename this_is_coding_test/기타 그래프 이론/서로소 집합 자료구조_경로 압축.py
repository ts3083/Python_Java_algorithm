def find_parent(parent, x): # 특정 원소가 속한 집합을 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 (Union)
def union_parent(parent, a, b):
    a = find_parent(parent, a) # a노드의 루트노드 찾기
    b = find_parent(parent, b) # b노드의 루트노드 찾기
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 선언과 초기화

for i in range(1, v + 1):
    parent[i] = i # 부모를 자기자신으로 초기화

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end="")

print()

print('부모 테이블: ', end="")
for i in range(1, v + 1):
    print(parent[i], end="")