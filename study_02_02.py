# 99 페이지 
# '1이 될 때까지'
 
n = int(input('값을 입력해주세요.: '))
k = int(input('값을 입력해주세요.: '))
ans = 0
while True:
    y = (n // k) * k
    ans += (n - y)
    n = y
    if n < k:
        break
    ans += 1
    n //= k
ans += (n - 1)
print(ans)