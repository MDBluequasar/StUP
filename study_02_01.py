def card(N, M):
    mycards = []  # 카드 정보 저장소

    # N개의 행 입력
    for a in range(N):
        row = [] # 입력 숫자 저장 공간, 즉 각 행의 index 인자 저장소
        nums = input().split() # 공백으로 구분된 숫자들을 입력 받음
        for num in nums:
            row.append(int(num)) # 입력 받은 숫자들을 정수로 변환하여 행에 추가
        mycards.append(row) # 완성된 행을 mycards 리스트에 추가

    card_list = []  # 각 행의 최소 값 저장 리스트
    for row in mycards:
        min_value = row[0]  # 각 행의 첫 번째 값을 최소 값으로 초기화
        for num in row:
            if num < min_value:
                min_value = num
        card_list.append(min_value) # 각 행의 최소 값을 card_list에 추가

    return max(card_list) # card_list에서 가장 큰 값 반환

N = int(input("행의 수: ")) # 행의 수를 입력
M = int(input("열의 수: ")) # 열의 수를 입력
result = card(N, M) # card 함수를 호출, 결과 계산
print(result) # 결과 출력
