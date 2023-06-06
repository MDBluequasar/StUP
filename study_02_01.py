# 96페이지 
# '숫자 카드 게임'

m = int(input('열의 갯수를 입력하세요.: '))
n = int(input('행의 갯수를 입력하세요.: '))
lista = [[3,1,2], [4,1,4], [2,2,2]]


for i in range(n):
    minv = min(lista)
    ans = max(minv)
print(ans)
