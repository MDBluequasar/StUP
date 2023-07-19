k = 3
score = [10, 100, 20, 150, 1, 100, 200]
n = 0
honor = []
answer = []

while True:
    if len(score) > n:
        honor.append(score[n])
        n += 1
        top_honor = sorted(honor, reverse=True)[:k]

        answer.append(min(top_honor))   
    else:
        break

print(answer)