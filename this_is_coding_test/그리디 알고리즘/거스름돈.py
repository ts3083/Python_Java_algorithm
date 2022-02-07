n = 1260
count = 0

array = [500, 100, 50, 10]
for coin in array: # 화폐의 갯수만큼 반복문 실행
    count += n // coin 
    # 거스름돈을 coin으로 나눈 몫이 코인의 갯수, 그것을 count로 더한다
    n %= coin # 거스름돈을 coin으로 나눈 나머지를 다시 새로운 거스름돈으로 설정

print(count)