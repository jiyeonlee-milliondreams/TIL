import sys

sys.stdin = open("5356_input.txt", "r")

# import re

T = int(input())
for test_case in range(1, T + 1):
    arr = ''
    N = 5  # words 배열 행의 길이
    words = [list(map(str, input())) for _ in range(N)]

    M = []
    for i in range(5):  # words 배열 열 길이 구하기
        M.append(len(words[i]))

    sum_M = 0
    for i in range(5):  # 열의 길이 합 구하기
        sum_M += M[i]

    row1 = row2 = row3 = row4 = row5 = 0  # 0번째 인덱스부터 읽기 위해 초기값 0으로 설정

    while row1 + row2 + row3 + row4 + row5 < sum_M:  # 열의 길이의 합 동안 반복
        if row1 < M[0]:  # words[0]의 길이동안 arr에 words[0][row1] 추가하기
            arr += words[0][row1]
            row1 += 1
        if row2 < M[1]:  # words[1]의 길이동안 arr에 words[1][row2] 추가하기
            arr += words[1][row2]
            row2 += 1
        if row3 < M[2]:  # words[2]의 길이동안 arr에 words[2][row3] 추가하기
            arr += words[2][row3]
            row3 += 1
        if row4 < M[3]:  # words[3]의 길이동안 arr에 words[3][row4] 추가하기
            arr += words[3][row4]
            row4 += 1
        if row5 < M[4]:  # words[4]의 길이동안 arr에 words[4][row5] 추가하기
            arr += words[4][row5]
            row5 += 1

    print(f'#{test_case}', arr)

    # result = arr.replace('\s', '')
    # result = re.sub('\s+', '', arr)

    # while row1 + row2 + row3 + row4 + row5 < sum_M:  # 열의 길이의 합 동안 반복
    #     for i in range(5):  # 반복문 활용하여 최적화
    #     if row1 < M[0]:  # words[0]의 길이동안 arr에 words[0][row1] 추가하기
    #         arr += words[0][row1]
    #         row1 += 1
    #     if row2 < M[1]:  # words[1]의 길이동안 arr에 words[1][row2] 추가하기
    #         arr += words[1][row2]
    #         row2 += 1
    #     if row3 < M[2]:  # words[2]의 길이동안 arr에 words[2][row3] 추가하기
    #         arr += words[2][row3]
    #         row3 += 1
    #     if row4 < M[3]:  # words[3]의 길이동안 arr에 words[3][row4] 추가하기
    #         arr += words[3][row4]
    #         row4 += 1
    #     if row5 < M[4]:  # words[4]의 길이동안 arr에 words[4][row5] 추가하기
    #         arr += words[4][row5]
    #         row5 += 1

# A = 'a b   c d  e'
#
# print(result)

# while row1 + row2 < M[0] + M[1]:   # 열의 길이의 합 동안 반복
#     if row1 < M[0]:
#         arr += words[0][row1]
#         row1 += 1
#     if row2 < M[1]:
#         arr += words[1][row2]
#         row2 += 1
# print(arr)


# N = 5
# arr = [list(map(str,input())) for _ in range(N)]
# for j in range(N):
#     for i in range(N):
# for 를 i, j로 한다면
# [j][i]를 읽어야 한다. 그래야 세로로 읽을 수 있다.

# board = [list(input()) for _ in range(N)]
#
# max_row = 0
# for i in range(5):
#     max_row = max(len(board[i]), max_row)
#
# result = []
#
# for i in range(max_row):
#     for j in range(5):
#         # 열의 길이가 서로 다를 수 있으므로 최대 길이를 먼저 알아두고
#         # 현재 알고 있는 줄이 그 길이가 안되면 스킵 컨티뉴뉴
#         if len(board[j]) <= i:
#             continue
#         # 세로를 먼저 바꾸기 위해 j를 앞쪽에 둔다.
#         result.append(board[j][i])
#
# print(&apos;&apos;.join(result))
