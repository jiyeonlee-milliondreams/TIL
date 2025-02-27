import sys

sys.stdin = open("hw_1209_input.txt", "r")

N = M = 100  # 이차원 배열의 크기

for tc in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0  # 행의 합, 열의 합, 대각선의 합 중 최대값

    for i in range(N):  # 행 먼저 순회
        row_sum = 0
        for j in range(M):  # 그 다음, 열 순회
            row_sum += arr[i][j]  # 행의 합 구하기
            if max_sum <= row_sum:  # 최대값 갱신
                max_sum = row_sum

    for j in range(M):  # 열 먼저 순회
        column_sum = 0
        for i in range(N):  # 그 다음, 행 순회
            column_sum += arr[i][j]  # 열의 합 구하기
            if max_sum <= column_sum:  # 최대값 갱신
                max_sum = column_sum

    right_diagonal_sum = 0
    left_diagonal_sum = 0
    for i in range(N):  # 행 먼저 순회
        right_diagonal_sum += arr[i][i]  # 오른쪽으로 그어지는 대각선의 합
        left_diagonal_sum += arr[i][N - 1 - i]  # 왼쪽으로 그어지는 대각선의 합

        # 대각선 합의 중복 제거
        # N이 홀수일 경우, 정중앙 값이 두 번 더해지므로 한 번 빼기
        right_diagonal_sum -= arr[N // 2][N // 2] * (N % 2)
        left_diagonal_sum -= arr[N // 2][N // 2] * (N % 2)

        if max_sum <= right_diagonal_sum:
            max_sum = right_diagonal_sum
        if max_sum <= left_diagonal_sum:
            max_sum = left_diagonal_sum

    print(f'#{test_case} {max_sum}')

'''
1) 대각선 위, 아래
if i < j
if i > j

2) 대각선 자체
for i in range(N):
    arr[i][i]

'''
