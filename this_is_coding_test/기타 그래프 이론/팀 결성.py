def find_parent(parent, x):
    if(parent[x] != x):
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())  # 학생 수는 N + 1, 연산의 횟수는 M
parent = [0] * (N + 1)

for i in range(N + 1):  # 루트 노드 초기화
    parent[i] = i

for _ in range(M):
    command, a, b = map(int, input().split())  # 명령어, a학생이 속한 팀, b학생이 속한 팀
    if command == 0:  # union 연산
        union(parent, a, b)
    else:  # 같은 팀 여부 확인
        if find_parent(parent, a) == find_parent(parent, b):  # 같은 팀이면
            print("YES")
        else:  # 다른 팀이면
            print("NO")
