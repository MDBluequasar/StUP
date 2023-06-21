# 315 page
# 볼링공 고르기

n, m = map(int, input().split()) # 볼링공의 갯수와 최대 무게
we = list(map(int, input().split())) # 공 무게 리스트화

an = 0

for i in range(n-1): # 임의로 1개의 공을 골랐을 때의 리스트를 만든다.
    for j in range(i+1, n): # 임의로 선택된 1개의 공을 제외한 리스트에서 다른 리스트를 비교 한다.
        if we[i] != we[j]: # 첫번째 공과 두번째 공의 무게가 다르다면 조건에 맞는다
            an += 1 # 그러므로 경우의 수가 1개씩 증가 한다.
print(an)
