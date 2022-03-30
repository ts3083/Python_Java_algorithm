import heapq  # 기본적으로 힙 라이브러리를 그대로 사용한다면 최소 힙(Min Heap)


def heapsort(arr):
    h = []
    result = []
    for value in arr:
        heapq.heappush(h, value)  # h리스트에 value값을 넣기

    for i in range(len(h)):
        result.append(heapq.heappop(h))  # heapq가 pop할 땐 크기가 작은 순서대로 pop
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
