import sys
sys.stdin = open('11315_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 배열의 크기
    board = [list(map(str, input())) for _ in range(N)]
    M = 5   # 오목의 길이는 5로 고정
    result = 'NO'   # 결과는 'NO'로 초기값 설정

    # 대각선 검사하기
    for i in range(N-M+1):  # 행을 순회하며
        if board[i][i] == 'o' and board[i + 1][i + 1] == 'o' and board[i + 2][i + 2] == 'o' and board[i + 3][i + 3] == 'o' and board[i + 4][i + 4] == 'o':
            result = 'Yes'
        if board[i][N-1-i] == 'o' and board[i+1][N-2-i] == 'o' and board[i+2][N-3-i] == 'o' and board[i+3][N-4-i] == 'o' and board[i+4][N-5-i] == 'o':
            result = 'Yes'

    # 대각선 검사하기(연속 숫자 개수 활용)
    for i in range(N-M+1):
        dia = [0] * (N - M)
        if board[i][i] == 'o':
            dia[i] = 1
    for start in range(len(dia) - M + 1):
        success = True
        for i in range(M):  # 오목 길이 5만큼 구간 설정
            if dia[start + i] != 1:
                success = False
                break   # for i



    # 세로 줄 추가하기
    for i in range(N):
        column = []
        for j in range(N):
            column.append(board[j][i])
        board.append(column)

    # 가로, 세로 검사하기
    for row in board:   # 행을 순회하며
        for start in range(N-M+1):  # 시작점 0부터 N-M까지
            success = True
            for i in range(M):  # 오목 길이 5만큼 구간 설정
                if row[start + i] != 'o':     # '.'이라면 해당 구간 반복 중지
                    success = False
                    break   # for i
            if success:
                result = 'YES'
                break   # for start. 행 순회도 끝내고 싶은 데 어떻게 할까?


    print(f'#{test_case}', result)
