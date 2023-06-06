# 96페이지 숫자 카드 게임

m , n = map(int, input().split())

ans = 0
for i in range(n):
    data = list(map(int, input().split()))
    mi = min(data)
    ans = max(ans, mi)
print(ans)