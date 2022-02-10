"""
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어짐
모든 알파벳을 오름차순으로 사전식 정렬, 그 뒤에 모든 숫자를 더한 값을 추가

알파벳 대문자와 숫자가 랜덤으로 한줄에 입력된다
처음부터 하나씩 확인하면서 문자열은 새로운 문자열에 담고
숫자는 sum을 이용해서 모두 더한다
그리고 마지막 원소까지 이동을 완료하면 문자열을 복사한 문자열을
하나씩 출력하고 마지막으로 sum을 출력
"""
li = []
sum = 0
s = input()
for key in s:
    if (key.isalpha()):
        li.append(key)
    else:
        k = int(key)
        sum += k
li.sort()  # 문자열을 알파벳 순서로 정렬
if (sum != 0):
    li.append(str(sum))  # li의 element를 문자열으 형태로 변환하여 공백없이 출력
print(''.join(li))
