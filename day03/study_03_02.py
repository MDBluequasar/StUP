# 312 페이지
# 곱하기 혹은 더하기

data = input("숫자를 입력해주세요")

result = 0
for i in range(0, len(data)):
    mu = int(data[i])
    if mu <= 1 or result <= 1:
        result += mu
    else:
        result *= mu
print(result)        