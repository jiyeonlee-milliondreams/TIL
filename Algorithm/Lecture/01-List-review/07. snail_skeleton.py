N = 5 
matrix = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]

# 값의 목록을 만들거다. 이 값을 이용해서 빈 2차원 리스트를 채워갈거다.
# 지금 몰라도 됨.. 달팽이를 위해서 잠시 쓴겁니다..
# 버블 정렬, 삽입 정렬, 선택 정렬 직접 구현해서 쓰시면 됩니다.
sorted_matrix = sorted([num for row in matrix for num in row])

result = [[0] * N for _ in range(N)]

# 달팽이 순회를 할건데, 델타 탐색을 이용하기로 했어요
# 우 -> 하 -> 좌 -> 상
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 0, 0 좌표에서부터 시작하고, 시작방향은 오른쪽 (즉, 0)
x, y, direction = 0, 0, 0

for value in sorted_matrix:
    result[x][y] = value
    # 방향에 따른 다음에 이동할 좌표
    nx, ny = x + dxy[direction][0], y + dxy[direction][1]

    # 범위를 벗어나거나, 이미 값을 채워진 칸을 만나면, 방향을 꺽는다.
    if not (0 <= nx < N and 0 <= ny < N and result[nx][ny] == 0):
        direction = (direction + 1) % 4  # 방향 바꿔주고, %4로 항상 0~3범위로 설정하게 하기
        # 방향을 꺽고, 다시 이동해줘야한다. 왜냐면 기존에는 인덱스가 넘쳐서 이동을 못했으니까
        nx, ny = x + dxy[direction][0], y + dxy[direction][1]

    # 이동한 위치를 현재 좌표로 재설정
    x, y = nx, ny

print(result)