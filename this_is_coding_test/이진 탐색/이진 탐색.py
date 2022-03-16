# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(arr, target, start, end):
    if (start > end):
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif (arr[mid] > target):  # 찾고자하는 수가 mid위치의 수보다 작다면
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


n, target = map(int, input().split())  # 원소의 개수 + 찾고자하는 수 입력받기
arr = list(map(int, input().split()))  # 전체 원소를 리스트로 입력받기

# 이진 탐색 수행 결과 출력하기
result = binary_search(arr, target, 0, n - 1)
if (result == None):
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
