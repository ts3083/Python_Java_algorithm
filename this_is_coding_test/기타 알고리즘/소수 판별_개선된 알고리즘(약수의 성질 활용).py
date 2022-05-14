# 16이 약수는 1 2 4 8 16 이고 4를 기준으로(16의 제곱근) 대칭인 것을 알 수 있다.
# 16이 2로 나누어 떨어지는 것은 8로도 나누어 떨어진다는 것을 의미
# 즉, 제곱근까지만 나누어떨어지는지 확인하면 소수인지 판별이 가능하다.
import math


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):  # +1을 하여 제곱근까지 나누어떨어지는지 확인
        if x % i == 0:
            return False
    return True


print(is_prime_number(23))
print(is_prime_number(8))
