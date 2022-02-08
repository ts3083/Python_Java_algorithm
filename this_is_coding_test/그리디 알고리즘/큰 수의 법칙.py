# 배열의 크기 M K를 입력받고 다음 행에서 배열의 크기만큼 숫자를 입력받는다
# 특정한 인덱스에 해당하는 숫자를 K번 초과하지않고 M번 더해서 나올 수 있는 최대값을 구하는 프로그램
# ex) 5 8 3 / 2 4 5 4 6 -> 6 6 6 5 6 6 6 5 = 46
# ex) 5 7 2 / 3 4 3 4 3 -> 4 4 4 4 4 4 4 = 28

size, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = 0
count = 0 # count라는 매개변수로 횟수가 K번을 넘지 못하게 설정
max0 = arr[size - 1] # 제일 큰수
max1 = arr[size - 2] # 그다음 큰수(제일 큰 수와 같은 수일 수도 있음)

for i in range(0, M): # 0부터 M-1까지 ***마지막 원소 포함안됨
    if(count < K):
        result += max0
        count += 1
    else:
        result += max1
        count = 0
print(result)