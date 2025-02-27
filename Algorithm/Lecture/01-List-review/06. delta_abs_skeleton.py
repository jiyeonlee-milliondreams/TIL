N=5
matrix = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# 상, 하, 좌, 우
# (-1, 0) , (1, 0), (0, -1), (0, 1)
# 방법 1
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# 방법 2
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상, 하, 좌, 우

total_sum = 0

# 모든 요소를 순회한다.
for i in range(N):
    for j in range(N):
        cnt_val = matrix[i][j]  # 그냥 앞으로 매번 martix[i][j]를 적을 자신이 없어서...

        # 4방향 델타 탐색
        # 방법 1
        # for k in range(4):
        #     # 다음에 이동할 좌표 할당
        #     ni, nj = i + dx[k], j + dy[k]

        # 방법 2
        for dx, dy in dxy:
            ni, nj = i + dx, j + dy
            # 범위를 벗어난 경우에는 탐색하면 안된다
            # 범위를 벗어나지 않은 경우메나 탐색!!

            # 방법 1
            # 버그가 나면 찾기 힘들다.
            # if 0 <= ni < N and 0 <= nj < N:
            #     # abs 는 절대값 구하는 함수
            #     # 현재 값 - 인접한 요소의 절대값을 누적 합
            #     total_sum += abs(cnt_val - matrix[ni][nj])

            # 방법 2 ( 퀵 리턴, early return)
            # 틀린 조건이 나오면, 난 아래를 실행하지 않겠다!
            # 단점 : ? 코드가 길어진다. ㅋㅋㅋㅋ
            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                print("범위를 벗어나서 에러 ")
                continue

            total_sum += abs(cnt_val - matrix[ni][nj])










