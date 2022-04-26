# 소수의 정의 : 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수
# 소수의 정의를 이용한 기본적인 소수 판별 알고리즘

def is_prime_number(x):
    # 2부터 x-1까지 모든 수를 확인하면서 나누어 떨어지는 경우가 하나라도 있으면 소수 아님
    for i in range(2, x):
        if x % i == 0:  # 하나라도 나누어 떨어지면
            return False
    return True


print(is_prime_number(17))
print(is_prime_number(20))
