import sys
sys.stdin = open('1215_input.txt', 'r')

T = 10

for test_case in range(1, T+1):
    M = int(input())    # 회문의 길이
    N = 8   # 열의 길이
    board = [input() for _ in range(N)]
    result = 0  # 회문의 개수

    # 세로줄을 board에 추가해서 열 우선순회가 한 번의 반복으로 이뤄질 수 있도록
    for i in range(N):
        column = ''
        for j in range(N):
            column += board[j][i]
        board.append(column)

    # board의 각 행을 순회하며
    for row in board:
        # 시작점의 위치는 0부터 N-M까지 변화
        for start in range(N-M+1):
            # 시작점부터 회문의 길이인 M//2만큼 반복하며
            success = True
            for i in range(M//2):
                # 회문 첫 글자와 마지막 글자 그리고 그 안의 글자의 일치 여부 확인
                if row[start + i] != row[start + M -1 - i]:
                    success = False
                    break
            if success:     # 회문이라면 result 1 증가
                result += 1

    print(f'#{test_case}', result)



















# N = int(input())
# txt = input()
# total = 0
#
# for j in range(8-N+1):      # 회문을 확인하는 구간의 첫 글자 인덱스
#     for k in range(N//2):   # 회문의 길이 절반만큼 비교
#         if txt[j+k] != txt[j+N-1-k]:
#             break   # 비교 글자가 다르면 현재 구간 중지
#
#     else:       # break에 걸리지 않고 for문 종료 즉, 회문이면
#         total += 1
# print(total)
#
# T = int(input())
# for test_case in range(1, T+1):
#     result = 0
#     txt = input()
#     N = len(txt)
#
#     for i in range()
#
