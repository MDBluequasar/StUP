# 316 page
# 무지의 먹방 라이브

ftime = list(map(int, input().split()))
n = len(ftime)

foodg = []
for i in range(n):
    foodg.append((ftime[i], i+1)) # 음식을 먹는게 걸리는 시간, 음식 번호를 이중 리스트 화 해준다.
foodg.sort() # 음식을 먹는 시간이 빠른 순서로 정렬

time = 0

for i, food in enumerate(foodg):  
    d = food[0] - time 
