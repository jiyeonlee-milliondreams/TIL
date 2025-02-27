import sys

sys.stdin = open('testing.txt', 'r')
'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 배열의 크기
    board = [list(map(int, input().split())) for _ in range(N)]


    def ball(standard, i, j):
        visited = []
        count = 0
        max_count = 0
        for _ in range(N * N):
            around_idx = []
            for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if standard > board[ni][nj]:
                        around_idx.append([ni, nj])
                    if standard > board[ni][nj] and [ni, nj] not in visited:  # 방문한 곳이 아니라면
                        visited.append([ni, nj])  # 방문한 곳에 새로운 좌표를 추가하고
                        i = ni  # 좌표를 갱신
                        j = nj
                        standard = board[i][j]
                        count += 1
                        max_count = max(max_count, count)
                        break  # for di, dj
                continue
            if around_idx == []:
                break
        return max_count


    tc_max_count = 0
    for i in range(N):
        for j in range(N):

            standard = board[i][j]
            st_max_count = ball(standard, i, j)

            if tc_max_count < st_max_count:
                tc_max_count = st_max_count

    print(f'#{test_case} {tc_max_count}')
'''


"""
1. 높은 층에서 낮은 층으로만 공을 굴릴 수 있다.
2. 공은 사방으로만 이동할 수 있다.
3. 최대 이동거리를 구하여 # 테스트 케이스 번호와 함께 출력하라.
"""


# def around(i, j):
#     standard = board[i][j]
#     around_idx = []
#     for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
#         ni = i + di
#         nj = j + dj
#         if 0 <= ni < N and 0 <= nj < N:
#             if standard > board[ni][nj]:
#                 around_idx.append([ni, nj])
#     return around_idx


def ball(standard, i, j):
    visited = []
    count = 0
    max_count = 0
    success = True
    while success:
        around_idx = []
        for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if standard > board[ni][nj]:
                    around_idx.append([ni, nj])
                if standard > board[ni][nj] and [ni, nj] not in visited:  # 방문한 곳이 아니라면
                    visited.append([ni, nj])  # 방문한 곳에 새로운 좌표를 추가하고
                    i = ni  # 좌표를 갱신
                    j = nj
                    standard = board[i][j]
                    count += 1
                    max_count = max(max_count, count)
        if around_idx == []:
            success = False
    return max_count

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 배열의 크기
    board = [list(map(int, input().split())) for _ in range(N)]

    tc_max_count = 0
    for i in range(N):
        for j in range(N):

            standard = board[i][j]
            st_max_count = ball(standard, i, j)

            if tc_max_count < st_max_count:
                tc_max_count = st_max_count

    print(f'#{test_case} {tc_max_count}')

'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 배열의 크기
    board = [list(map(int, input().split())) for _ in range(N)]

    # 기준점 standard = board[i][j]의 사방을 탐색하여 standard 보다 낮은 값을 구한다.
    for i in range(N):
        for j in range(N):
            arounds = around(i, j)
            if arounds != []:
                for around in arounds:
                    standard = board[i][j]
                    while True:
                        for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < N and 0 <= nj < N:
                                if standard > board[ni][nj]:
'''

'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 배열의 크기
    board = [list(map(int, input().split())) for _ in range(N)]


    def around(i, j):
        standard = board[i][j]
        around_idx = []
        for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if standard > board[ni][nj]:
                    around_idx.append([ni, nj])
        return around_idx

    def ball(standard, i, j):
        visited = []
        count = 0
        max_count = 0
        success = True
        while success:
            arounds = around(i, j)
            if arounds == []:   # 기준점 사방에 기준점보다 값이 작은 지점이 없다면 반복 중지
                success = False
            else:
                for around in arounds:
                    i = around[0]
                    j = around[1]
                    standard = board[i][j]
                    count += 1
                    max_count = max(max_count, count)
                    ball(standard, i, j)

        return max_count


    tc_max_count = 0
    for i in range(N):
        for j in range(N):
            visited = []
            count = 0
            max_count = 0
            success = True
            while success:

                if around(i, j) == []:  # 기준점 사방에 기준점보다 값이 작은 지점이 없다면 반복 중지
                    success = False
                else:
                    for around in around(i, j):
                        i = around[0]
                        j = around[1]
                        standard = board[i][j]
                        count += 1
                        max_count = max(max_count, count)

            if tc_max_count < max_count:
                tc_max_count = max_count

    print(f'#{test_case} {tc_max_count}')
'''