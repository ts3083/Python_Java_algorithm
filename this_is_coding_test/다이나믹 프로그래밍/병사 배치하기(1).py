"""
나열된 병사들의 전투력이 내림차순이 되도록 하면서
최소한의 병사만을 제외하는
그 방법의 열외시켜야 하는 병사의 수를 출력하는 알고리즘 작성

15 11 4 8 5 2 4
15 3 4 8 5 2 4
15 

첫번째부터 차례대로 확인하면서 다음 인덱스의 원소가 자신보다 크다면
자기자신을 배열에서 삭제
삭제 연산의 횟수를 출력
"""

n = int(input())
ability = list(map(int, input().split()))
count, i = 0, 0

while i != (len(ability) - 1):
    if (ability[i] < ability[i + 1]):
        del ability[i]
        count += 1
    else:
        i += 1

print(count)
