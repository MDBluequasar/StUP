# programmers
# 콜라문제

a = 2
b = 1
n = 20

result = 0
add = 0

while True:
    if n // a != 0:
        add = (n // a) * b # 빈병 갯수와 교환해주는 콜라의 병이 변할 때를 고려한 코딩

        result += add # 최종적으로 가질 수 있는 콜라의 갯수
        # 교환 할 수 있는 콜라의 갯수(교환된 콜라의 갯수 = 빈병의 갯수)와 
        # 교환 할 수 없는 나머지 빈병을 더하여 최종적으로 가질 수 있는 빈병의 갯수를 합산한다.
        # 즉 나머지 빈병 + 교환된 콜라의 갯수
        n = n % a + add  
    else:
        break
print(result)
