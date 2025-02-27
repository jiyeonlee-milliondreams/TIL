T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 배열의 크기
    space = [list(map(int, input().split())) for _ in range(N)]     # 0 빈칸 1 벽  2 괴물

    alien = []

    # 우주를 순회하며
    for i in range(N):
        for j in range(N):
            # 괴물을 찾았다면
            if space[i][j] == 2:
                # 괴물 사방을 순회하며
                for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
                    # 거리는 1칸부터 N-1까지
                    for dist in range(1, N):
                        ni = i + di * dist
                        nj = j + dj * dist
                        # 배열을 벗어나면 방향 전환
                        if 0 > ni or ni >= N or 0 > nj or nj >= N:
                            break   # for dist
                        # 배열 안에서
                        else:
                            # 벽을 만나면 방향 전환
                            if space[ni][nj] == 1:
                                break   # for dist
                            # 벽이 아니라면 3으로 채우기
                            else:
                                space[ni][nj] = 3

    # 0으로 채워진 안전한 공간 찾기
    safe_area = 0

    for i in range(N):
        for j in range(N):
            if space[i][j] == 0:
                safe_area += 1

    print(f'#{test_case} {safe_area}')
