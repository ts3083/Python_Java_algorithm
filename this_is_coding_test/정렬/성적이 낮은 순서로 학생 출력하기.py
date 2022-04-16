"""
1줄 : 학생의 수 N(십만명 이하) 입력받기
2줄 : 부터 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가
공백으로 구분되어 입력된다
문자열 길이와 학생의 성적은 100이하 자연수

성적이 낮은 학생 순서대로 출력
성적이 동일하다면 자유롭게 출력
"""

arr = []
n = int(input())
for i in range(n):
    data = input().split()
    arr.append([data[0], int(data[1])])

arr = sorted(arr, key=lambda x: x[1])

for i in arr:
    print(i[0], end=' ')
