nums = [3,3,3,2,2,2]
answer = 0
    
num_len = len(set(nums)) # 중복 값을 제거 하여 중복된 경우의 수 제거(다양한 종류의 포켓몬 고를 수 있음)
result = int(len(nums)/2) # 고를 수 있는 포켓몬의 수 정의
    
if result < num_len :
    answer = result
else :
    answer = num_len
    
print(answer)