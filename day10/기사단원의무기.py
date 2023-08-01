
number = 10

limit = 3

power = 2




dlist = []                             # 약수 list

for i in range(1, number+1):              # 1부터 number까지 반복
    dn = 0
    for j in range(1, int(i**(1/2)) + 1): # 1부터 i의 제곱근까지 반복
        if i % j == 0:
            dn += 1
            if j**2 != i:                 # 제곱의 수는 count +1 을 하여 중복 방지.
                dn += 1
        if dn > limit:               # 제한 값을 초과 시 power값
            dn = power
            
    dlist.append(dn)
print(sum(dlist))