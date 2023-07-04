# 코딩테스트
# 322p
# 문자열 재정렬

monum = input('이 문자열은 영국에서부터 시작하여 주저리 주저리:')

moon = []
num = 0

for i in monum:
    if '0' <= i <= '9':
        num += int(i)
    else:
        moon.append(i)
# print(num)
# print(moon)

answer = ''.join(moon)

print("%s%d" % (answer, num))
