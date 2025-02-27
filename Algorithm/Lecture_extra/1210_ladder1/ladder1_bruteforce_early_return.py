import sys
sys.stdin = open('ladder_1_input.txt')

# 아래, (우, 좌) => 순서 상관 x
dxy = [[1, 0], [0, 1], [0, -1]]

# 시작점에서 끝까지 내려가서 "2"에 걸맞는 시작점인지 확인하는 함수
# x, y 는 시작점 !
def search_ladder(x, y):
    # 원본을 훼손하지 않기 위해서 복사본을 만들어야 한다.
    # 방문 여부를 확인하기 위한 복사본을 생성
    # N * N  크기의 0인 값의 MAtrix
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1  # 초기 시작 위치도 방문 체크를 하자

    # 맨 밑에 도달할 때까지 계속 반복해서 내려갈겁니다.
    # x => 행을 의미하죠.
    # x != 99 가 아니다는 결국 아직 맨 마지막에 도달하지 않았다.
    # x 가 99에 도달했다는 건 맨 마지막에 도달했다는 것 !
    while x != 99:
        # 3방향으로 델타 탐색 시작
        for dx, dy in dxy:
            # 다음에 이동할 좌표 (nx, ny)
            nx, ny = x + dx, y + dy

            """
            이동하기 위한 조건 
            1. 범위 안에 들어야 한다. 
            2. 사다리가 놓여있어야 한다. 
            3. 방문한 적이 없어야 한다. 
            """
            # 범위를 벗어난 경우에는 이건 옳지 않은 케이스
            if nx < 0 or nx >= 100 or ny < 0 or ny >= 100:
                continue

            # 길이 아닌 경우 ( 사다리가 놓여 있지 않은 경우 )
            if not data[nx][ny]:
                continue

            # 이미 방문한 경우 (되돌아 가지 않도록 conitnue)
            if visited[nx][ny]:
                continue

            # 방문할 수 있는 곳임을 확인했기 때문에, 방문 처리
            visited[nx][ny] = 1

            # 현재 좌표를 다음 좌표로 갱신
            x, y = nx, ny



    # 마지막에 도달하고, 맨 마지막의 목적지의 값
    return data[x][y] == 2  # 2인 경우에는 True, 2가 아닌 경우에는 False

for _ in range(1, 11):
    tc = int(input())
    N = 100
    result = -1  # 못 찾는 경우 -1로 세팅하고, 찾으면 시작 인덱스를 설정한다.
    data = [list(map(int, input().split())) for _ in range(N)]

    # 출발점을 찾아야한다.
    # 1행에서 "1" 인 친구들만 시작점으로 한다.
    for j in range(N):  # 모든 열을 검사해서 1인 친구들만 시작한다.
        # data[0] => 1행
        if data[0][j] == 1:
            # 사다리 탐색을 시작한다.
            # 도착점이 "2"인 경우에는 True, 아닌 경우에는 False
            if search_ladder(0, j):
                # "X"에 도달할 수 있는 출발지는 반드시 1군데에요.
                result = j
                break

    print(f"#{tc} {result}")

