# 스페이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수 = 실패율

n = 5 # 스테이지 갯수

stages = [2,1,2,6,2,4,3,3] # 각 스테이지 별 아직 클리어하지 못한 플에이어의 수
people = len(stages) # 총 인원수


result = {}

answer = []
    
for i in range(1, n+1):
    if people != 0:
        result[i]= stages.count(i) / people
        people = people - stages.count(i)
    else:
        result[i] = 0

    
answer = sorted(result, key = result.get, reverse=True)
                  
print(answer)