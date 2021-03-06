# 어떠한 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 실행
# 1. N에서 1을 빼기
# 2. N을 K로 나누기(단, N이 K로 나누어 떨어질 때만 선택가능)
# N, K가 주어질 때 N이 1이 될 때까지 1혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하기
# 첫째 줄에 N(1 <= N <= 100,000)과 K(2 <= K <= 100,000)가 공백을 기준으로 자연수로 각각 주어짐

# 아이디어 : 나누는 작업을 최대한 많이 한다
# 나누어 떨어진다면 우선적으로 나누기를 실행

N, K = map(int, input().split()) # 중요! input().split()으로 하면 N, K가 str형으로 인식함
# 따라서 map을 활용해서 입력값을 int형으로 바꿔준다
count = 0
while N != 1:
    if N < K:
        count += (N - 1)
        N = 1
    else:
        if (N % K != 0):
            count += 1
            N -= 1
        else:
            count += 1
            N //= K

print(count)