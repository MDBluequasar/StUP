# 코딩테스트
# 321p
# 럭키 스트레이스

num = input('숫자를 입력해주면 안 잡아먹지:')
sum1 = 0
sum2 = 0

for i in range(len(num) // 2):
    sum1 += int(num[i])
# print(sum1)

for j in range(len(num)//2 , len(num)):
    sum2 += int(num[j])
# print(sum2) 

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')