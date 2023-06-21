'''
N이 1이 될 때까지 1을 빼거나 K로 나누는 과정 중 하나를 반복적으로 선택해 수행하되
나눗셈은 N이 K로 나눠떨어질 때만 선택
N = 17, K = 4일 경우 뺴기를 한 번 수행하면 N =16, 이후 나눗셈을 두 번 수행하면 N = 1로
전체 과정을 실행한 횟수는 3 출력'''

'''answer = 0 # N을 1로 만드는 계산 횟수 
(UnboundLocalError: cannot access local variable 'answer' where it is not associated with a value)'''
def count_num(N, K):
    answer = 0
    while N != 1:
        '''answer = 0 # N을 1로 만드는 계산 횟수 <answer가> 계속 초기화,
        마지막 반복에서의 answer 값만 반환'''
        if N % K == 0:
            N = N / K # N에 새로운 몫을 할당 
        else:
            N -= 1
        answer += 1  # 계산 횟수를 1 증가시킴
    return answer
print(count_num(17, 4))
print(count_num(16, 4))