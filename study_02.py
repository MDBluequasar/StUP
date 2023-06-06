# 96페이지 
# '숫자 카드 게임'

m = int(input('열의 갯수를 입력하세요.: '))
n = int(input('행의 갯수를 입력하세요.: '))
lista = [[3,1,2], [4,1,4], [2,2,2]]


for i in range(n):
    minv = min(lista)
    ans = max(minv)
print(ans)


# 99 페이지 
# '1이 될 때까지'
 
# n = int(input('값을 입력해주세요.: '))
# k = int(input('값을 입력해주세요.: '))
# ans = 0
# while True:
#     y = (n // k) * k
#     ans += (n - y)
#     n = y
#     if n < k:
#         break
#     ans += 1
#     n //= k
# ans += (n - 1)
# print(ans)