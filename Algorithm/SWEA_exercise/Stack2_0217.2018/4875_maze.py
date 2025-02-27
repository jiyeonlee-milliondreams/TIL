import sys
sys.stdin = open('4875_input.txt', 'r')


def dfs(i, j, N):   # 출발 좌표 i, j, 미로의 크기 N

    # 준비 작업
    visited = [[0]*N for _ in range(N)]     # visited 생성 이차원 배열
    stack = [[i, j]]    # 시작점 stack에 넣기

    while True:
        # 방문하지 않았다면 방문 처리
        if visited[i][j] == 0:
            visited[i][j] = 1
            # print(i, j)

        # 출구에 도착하면 1 아니면 0
        if maze[i][j] == 3:
            return 1

        # 기준점 사방에 방문 안 한 정점 w 가 있으면 방문
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = i+di, j+dj
            # 미로 내부 인접이고 벽이 아니면(통로(0)이면이라고 하지 않은 이유는 도착(3)에 들어가야 하기 때문)
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                stack.append([wi, wj])
                i = wi
                j = wj
                break

        # 다 방문 했다면
        else:
            if stack:
                temp = stack.pop()
                i = temp[0]
                j = temp[1]
            else:
                return 0
                break
    return 0


# 출발 좌표 탐색
def maze_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:  # 입력을 정수로 받았기 때문에 정수로 표시
                return i, j

T = int(input())
for test_case in range(1, T+1):

    N = int(input())    # 배열의 크기
    maze = [list(map(int, input())) for _ in range(N)]  # 미로 입력. 0 통로, 1 벽, 2 출발, 3 도착

    # 미로 시작점 '2'를 찾는 함수 호출하여 초기값 설정
    i = maze_start(maze)[0]
    j = maze_start(maze)[1]

    ans = dfs(i, j, N)

    print(f'#{test_case}', ans)

'''
*제한 조건*
- 배열 밖을 벗어나면 0
- 사방을 순회했을 때, 0이 없어서 더이상 갈 곳이 없는 경우 0
'''

'''
        # t에서 할 일 진행
        # 출구 에 도착하면 1 아니면 0
        if maze[ti][tj] == 3:
            return 1
    return 0    # 출구 에 도착하면 1 아니면 0
'''



    # candidates = around(maze_start(maze)[0], maze_start(maze)[1])

    # stack = [0] * (N * N)   # 배열의 크기만큼 스택 생성
    # top = -1
    # visited = []



'''
# 출발 지점 사방 탐색
def around(i, j):
    global N
    result = []
    for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:
            result.append([ni, nj])
    return result
'''


'''
    for candidate in candidates:    # 미로의 후보군을 순회하며
        i = candidate[0]
        j = candidate[1]
        for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:   # 0이라면 사방을 순회했을 때 더이상 갈 곳이 없을때까지 진행
                visited.append([di, dj])
                top += 1
                stack[top] = [ni, nj]
                i = ni
                j = nj
            else:   # 0이 아니라면 이전 경로로 돌아가서 다시 탐색 반복

                top -= 1
                i = stack[top + 1][0]
                j = stack[top + 1][1]
'''





