# 315 page
# 만들 수 없는 금액

n = int(input()) # 동전의 수
co = list(map(int, input().split())) # 동전의 금액
co.sort()

result = 1 # 동전을 뽑았을 때의 목표 값

for i in co:
    if result < i: # for문으로 돌려서 나온 i값이 결과값 보다 작다면 만들 수 없는 수를 의미한다.
        break
    result += i # 결과 값이 i 보다 작지 않다면 계속 i값을 더하여 만들 수 있는 수를 계산하게 ㅏㄴ다;.

print(result) # break 걸린 결과 값이 즉 만들 수 없는 최소값을 의미한다.

