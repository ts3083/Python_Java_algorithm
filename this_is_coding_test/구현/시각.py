hour = int(input())
count = 0 # 3이 하나라도 포함되는 모든 경우의 수

for h in range(hour + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s): # int를 문자열로 만들고 합치기 가능
                count += 1
print(count)