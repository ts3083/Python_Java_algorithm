"""
N크기 만큼의 배열 A, B 가 주어지고
K번 바꿔서 배열 A의 모든 원소의 합이 최대가 되도록 하는 프로그램
그 최대값을 출력

N, K는 10만 이하
모든 원소는 천만 이하 자연수

배열을 입력받고 정렬한 후에 A리스트의 작은 순서대로 B리스트의 큰 원소값과 swap하면 된다
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()  # 오름차순
b.sort(reverse=True)  # 내림차순

for i in range(k):  # k번 바꾸기
    if a[i] < b[i]:  # a의 원소가 b의 원소보다 작을 때에만 실행
        a[i], b[i] = b[i], a[i]  # 바꿔치기
    else:
        break

print(sum(a))
