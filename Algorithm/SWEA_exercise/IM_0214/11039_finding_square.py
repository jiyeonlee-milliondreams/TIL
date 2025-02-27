T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 배열의 크기
    board = [list(map(int, input().split())) for _ in range(N)]   # 0 공백 영역 1 사각형 영역
    result = []     # 가로와 세로를 곱한 값을 저장할 변수 생성

    # 이차원 배열을 순회하며
    for i in range(N):
        for j in range(N):
            # 1이라면
            square_row = 0  # 사각형 가로의 길이
            square_column = 0  # 사각형 세로의 길이
            max_square_row = 0
            max_square_column = 0
            if board[i][j] == 1:
                # 오른쪽 그리고 아래로 순회하며
                for di, dj in [0, 1], [1, 0]:
                    # 거리는 1부터 N-1까지
                    for dist in range(N):
                        ni = i + di * dist
                        nj = j + dj * dist
                        # 배열 밖이라면 방향 전환
                        if 0 > ni or N <= ni or 0 > nj or N <= nj:
                            break
                        # 배열 안이면서
                        else:
                            # 0이라면 방향 전환
                            if board[ni][nj] == 0:
                                break   # for dist
                            # 1이면서 오른쪽 방향이라면 사각형 가로 1증가. max 가로 갱신.
                            elif [di, dj] == [0, 1]:
                                square_row += 1
                                max_square_row = max(max_square_row, square_row)
                            # 1이면서 아래쪽 방향이라면 사각형 세로 1증가. max 세로 갱신.
                            else:
                                square_column += 1
                                max_square_column = max(max_square_column, square_column)

            # max 초기화 전에 곱한 값을 결과에 더해주기
            result.append(max_square_row * max_square_column)

    # 결과가 하나라면 그대로 출력
    if len(result) < 2:
        print(f'#{test_case} {result}')
    # 결과가 둘 이상이라면 최대값 출력
    else:
        print(f'#{test_case}', max(result))





