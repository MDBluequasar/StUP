# m = 'm번 더하기'
# k = 'k번 초과하여 더할 수 없다'

# lista = [2,4,5,4,6]
# m = 8 , k = 3
# total = '6+6+6+5+6+6+6+5' => 46 / 8번 더하고 같은 숫자는 3번까지만 더한다. 
# m >= k

# m = int(input("덧셈의 횟수를 지정하시오.: "))
# k = int(input("덧셈의 제한 횟수 지정하시오.: "))
k = 3
m = 8
local = [2,4,5,4,6]
local.sort(reverse = True)
print(local)

# 가장 큰 수
first = local[0]
print(first)

# 두번째로 큰 수
second = local[1]
print(second)

# 가장 큰 수 지정한 횟수 더하기
for num1 in range(k+1):
    sum1 = first * num1
print(sum1)

# 두 번째로 큰 수 지정한 횟수 더하기
for num2 in range(k+1):
    sum2 = second * num2
print(sum2)

# 지정 횟수 break
while True:
    sum1 = first * k
    if k == 0:
        break
    k -= 1
print(k)
    
# 덧셈의 길이 제한하기
while True:
    
    if m == 0:
        break
    m -= 1
print(m)