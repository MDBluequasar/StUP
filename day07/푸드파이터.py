# programmers
# 푸드파이터

food = [1, 7, 1, 2]

anwer = ''
left = ''

for id, x in enumerate(food):
    # print(id, x)
    if id == 0: # 리스트는 0 번째는 물이며 항상 1개 이므로 물은 제외 하고 카운팅한다. 
        continue
    left += str(id) * (x // 2) #  1번째 음식부터 두사람에 대한 음식 갯수를 나눈 몫만을 더하여준다.
    # print(left)

answer = left + '0' + left[::-1] # 물을 중앙에 놓고 왼쪽과 오른쪽이 대칭을 이룰 수 있게 코딩한다.

print(answer)