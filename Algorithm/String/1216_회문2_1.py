import sys
sys.stdin = open('1216_input.txt', 'r')

T = 10
for _ in range(1, T+1):

    test_case = int(input())
    N = 100 # 열의 길이
    board = [input() for _ in range(N)]
    max_palindrome_length = 1   # 테스트 케이스별 초기화

    # 세로를 board에 추가해서 한 번의 반복문으로 처리
    for i in range(N):
        column = ''# 열별로 column 초기화
        for j in range(N):
            column += board[j][i]
        board.append(column)

    # 회문을 순회하며
    for row in board:
        # M은 길이 N부터 1까지 역순으로 반복
        for M in range(N, 0, -1):
            # 길이 M만큼의 회문이 있는지 여부를 확인
            if M > max_palindrome_length:
                for start in range(N-M+1):
                    success = True     # 회문 하나마다 성공여부 확인
                    for j in range(M//2):
                        if row[start + j] != row[start + M - 1 - j]:
                            success = False
                            break
                    if success:
                        if max_palindrome_length < M:   # M 바꾸기 전에 최대 길이 갱신
                            max_palindrome_length = M
                            break
            else:
                break
    print(f'#{test_case}', max_palindrome_length)
