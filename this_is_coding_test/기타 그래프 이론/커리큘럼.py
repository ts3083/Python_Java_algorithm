from collections import deque
import copy

v = int(input())  # 노드의 개수
indegree = [0] * (v + 1)  # 진입차수 테이블
graph = [[] for i in range(v + 1)]  # 각 노드에 연결된 간선 정보를 담는 그래프
time = [0] * (v + 1)  # 각 강의 시간을 0으로 초기화

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]  # 수강 시간 정보저장
    for x in data[1:-1]:  # 1번째 인덱스부터 맨 마지막 원소를 포함하지 않게 자르기
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():  # 위상 정렬
    result = copy.deepcopy(time)  # 알고리즘 수행 결과를 담을 리스트
    q = deque()  # 큐 기능을 위한 deque 라이브러리 사용
    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:  # 큐가 빌 때까지 반복
        now = q.popleft()
        for i in graph[now]:  # now와 인접한 노드들의 진입차수 1 빼기
            # max함수를 사용해야 같은 우선순위의 강의 중 가장 큰 값으로 계산할 수 있음
            # 동시 수강하기 때문에 가장 큰 값으로 계산하면 된다
            result[i] = max(result[i], result[now] + time[i])  # i노드의 걸리는 시간
            indegree[i] -= 1
            if indegree[i] == 0:  # 진입차수가 0이 되면 큐에 삽입
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])


topology_sort()
