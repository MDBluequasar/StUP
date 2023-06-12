# 313 페이지
# 문자열 뒤집기

num = input("0와1로 이루어진 배열을 넣으시오.: ")

fir = num[0]
sec = num[0]
count = 0
\
for i in range(len(num)):
    if num[i] != sec and num[i] != fir:
        count += 1
    sec = num[i]
print(count)    