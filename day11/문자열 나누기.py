
s = "aaabbaccccabba"


answer = 1 # s는 1개의 문단, 나눌 수록 +1 해준다

string = s[0] 

first_count = 0  # 첫번째 문자가 같았을 때 +1
x_count = 0     # 첫번째 문자가 같지 않았을 때 +1

for i in s:   # 돌려 돌려 돌림판~
    if first_count != 0 and first_count == x_count: 
    # 첫번째 문자가 같았을 떄와 같지 않을 때의 숫자가 같다면 문자열을 나뉘어준다. => 그 후 다시 첫번째 값을 초기화
    
        
        answer += 1      # 문자열 나누기 횟수 증가
        first_count = 0  # 다시 초기화 
        x_count = 0      # 다시 초기화
        string = i       # 다음 문자를 첫번째값으로 다시 지정

    if string == i: # 동일한 값이면 first_count를 하나 올림.
        first_count += 1
    else: #아닐 경우에는, notX_conut를 하나 올림.
        x_count += 1

print(answer) 