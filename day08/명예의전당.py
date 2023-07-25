k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
n = 0
honor = []
answer = []

while True:
    if len(score) > n:
        honor.append(score[n])
        n += 1
        
        top_honor = sorted(honor, reverse=True)[:k]
        print(top_honor)
        answer.append(min(top_honor))   
    else:
        break

print(answer)