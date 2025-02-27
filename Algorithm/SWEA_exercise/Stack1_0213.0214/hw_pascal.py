T = int(input())

for test_case in range(1, T+1):

    N = int(input())    # 파스칼 행의 길이

    pascal = [[1]]

    for i in range(1, N):    # i = N-1까지 반복하며 pascal 행 추가 # 0번 인덱스의 행을 1로 미리 채워뒀으므로 i = 1부터 시작
        row = [0] * (i+1)  # pascal에 추가할 행을 빈 리스트 row로 생성. 행이 변화할 때마다 초기화
        row[0] = 1
        for j in range(1, i):    # 열이 i-1까지 반복
            row[j] = pascal[i-1][j-1] + pascal[i-1][j]      # 파스칼 왼쪽 위, 바로 위 인덱스의 값 더해서 받기

        row[i] = 1   # 반복을 돌고나서 row 마지막에 1 추가
        pascal.append(row)  # 완성된 열을 pascal에 추가

    print(f'#{test_case}')
    for row in pascal:
        print(' '.join(map(str, row)))

        # print(''.join(row))     # type이 int 이므로 str로 바꿔줘야 함.
        # print(''.join(str(row)))    # 리스트 형태로 출력됨.
        # print(''.join(map(str, row)))   # 글자가 모두 붙어서 출력됨
