# 311p
# 모험가 길드

data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in range(len(data)):
    count += 1
    if count >= data[i]:
        result += 1
        count = 0
print(result)       

