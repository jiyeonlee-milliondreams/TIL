import sys
sys.stdin = open('2805_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 배열의 크기(홀수)
    field = [list(map(int, input())) for _ in range(N)]
    profit = 0

    # 범위를 정해진 변수 i, N으로 표현하는 게 쟁점!!
    for i in range(N):  # 행을 순회하며
        # 정중앙 가로선을 기준으로 경우의 수를 나눈다.
        if i <= N//2:   # 더해야 할 범위가 1, 3, 5, 7과 같이 정중앙 가로선까지는 증가하다가
            for j in range(N//2 - i, N//2 + i + 1):     # N//2 - i부터 N//2 + i까지 순회하며
                profit += field[i][j]

        else:           # 더해야 할 범위가 5, 3, 1과 같이 정중앙 가로선 이후에는 감소한다.
            for j in range(i - N//2, N + N//2 - i):     # i - N//2부터 N + N//2 - i -1까지 순회하며
                profit += field[i][j]

    print(f'#{test_case} {profit}')

# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())  # 배열의 크기
#
#     # 0으로 N 크기의 이차원 배열 만들기
#     board = [[0] * N for _ in range(N)]
#
#     # 숫자의 초기값은 1으로 설정
#     number = 1
#     max_number = N ** N
#
#     # 초기 위치 board[0][0]으로 설정
#     i = j = 0
#
#     # 오른쪽으로 시계방향 전환
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#
#     # 방향은 오른쪽이 초기값
#     dir = 0
#
#     board[i][j] = number  # 초기 위치에 1을 넣고
#     number += 1  # 숫자를 1 증가시키고
#
#     # 숫자가 max_number 이하일 때에만 반복
#     while number <= max_number:
#         ni = i + di[dir]  # 새로운 위치를 변경한다.
#         nj = j + dj[dir]
#
#         # 새로운 위치가 배열 안에 있고 0이라면
#         if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:
#             i, j = ni, nj  # 위치를 새로운 위치로 바꾼 후
#             board[i][j] = number  # 숫자를 넣는다.
#             number += 1  # 숫자를 1 증가시키고
#
#         # 그렇지 않으면 방향을 전환한다.
#         else:
#             dir = (dir + 1) % 4
#             # 짝수 홀수 (N%2) 한 것처럼 4로 나눈 나머지로 하면 0123을 돌게 된다.
#
#     print(f'#{test_case}', board)
