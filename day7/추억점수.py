# programmers
# 추억점수

name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]


dic = {}
answer = []

for id, x in enumerate(name):
    dic[x] = yearning[id] # 딕셔너로 이름이 가지는 추억점수를 만든다.
# print(dic)

for a in photo: # 포토의 리스트 값을 받아온다.
    # print(a)
    score = 0
    for s in a: # 받아온 포토의 리스트를 다시 돌려준다.
        # print(s)
        if s in dic: # 딕셔너리에 이름값이 존재여부를 알아본다.
            score += dic[s] # 딕셔너리 key에 해당하는 value 값을 score에 차례대로 더해준다.
    answer.append(score) # 더해준 점수를 다시 합쳐준다.

print(answer)