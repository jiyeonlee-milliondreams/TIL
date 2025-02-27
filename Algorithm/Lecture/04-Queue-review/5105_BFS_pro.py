import sys
sys.stdin = open('5105_input.txt', 'r')


def bfs(i, j, N):   # 시작 위치 i, j, 크기 N
    # bfs 준비작업
    visited = [[0]*N for _ in range(N)] # visited 생성
    queue = []                              # 큐생성
    queue.append([i, j])                     # 시작점 인큐
    visited[i][j] = 1                   # 시작점 인큐 표시
    # 큐에 남은 칸이 없을 때까지 큐가 비워질때까지
    while queue:
        ti, tj = queue.pop(0)   # 디큐해서 t에 넣어주기

        # t에서 할 일 진행
        if maze[ti][tj] == '3':
            return visited[ti][tj] - 2  # 입구와 출구 사이의 빈칸 수
            # 출발에서 도착까지의 거리(간선 수)는 visited -1
            # 출발 도착 사이의 칸 수는 visited - 2

        # t에 인접 w 중 인큐되지 않은 곳이면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti+di, tj+dj
            # 미로 내부고, 인접이고 벽이 아니면(통로(0)이면이라고 하지 않은 이유는 도착(3)에 들어가야 하기 때문
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != '1' and visited[wi][wj] == 0:
                queue.append([wi, wj])  # 인큐
                visited[wi][wj] = visited[ti][tj] + 1   # 인큐 표시

    return 0    # 경로가 없는 경우 0

# 출발 좌표 탐색
def maze_start(arr):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':   # 입력을 str로 받았기 때문에 '' 추가.
                return i, j


T = int(input())
for test_case in range(1, T+1):
    N = int(input())        # 배열의 크기
    maze = [input() for _ in range(N)]  # 미로 입력

    i, j = maze_start(N)

    ans = bfs(i, j, N)


    print(f'#{test_case}', ans)
