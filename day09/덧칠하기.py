n = 8
m = 4

answer = 0

section = [2, 3, 6]

while section :
    s = section[0] + m
    print(s)
    while section and section[0] < s:
        section.pop(0)
        # print(section)
    answer += 1
print(answer)


