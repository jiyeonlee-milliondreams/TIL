import sys
sys.stdin = open("hw_1210_input.txt", "r")

dxy = [[1, 0], [0, 1], [-1, 0]]

def search_ladder(x,y): # 좌표 x, y
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1

    while x != 99:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                x, y = nx, ny

            '''
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if not arr[nx][ny]:
                continue
            if visited[nx][ny]:
                continue
            
            visited[nx][ny] = 1
            x, y = nx, ny
            '''

    return arr[x][y] == 2


T = 10
for _ in range(1, T+1):

    test_case = int(input())    # 테스트 케이스 번호 입력 받기
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]     # 배열의 크기 100*100
    result = -1

    for j in range(N):  # 시작점 후보 찾기.

        if arr[0][j] == 1:

            if search_ladder(0, j):
                result = j
                break


