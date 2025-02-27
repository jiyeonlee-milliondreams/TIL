import sys
sys.stdin = open('input.txt')

# 델타 탐색 , 순서 중요 X
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

T = int(input())
for tc in range(1, T+1):
    # N = 행의 개수 , M = 열의 개수
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 꽃가루의 합 중에서 최대값을 저장할 변수
    max_value = 0

    # 모든 풍선을 순회하기로 했다.
    for i in range(N):
        for j in range(M):
            # i, j 에서 풍선을 터트렸을 때, 발생하는 꽃가루를 저장할 변수를 생성
            # 꽃가루를 계산할 때, 현재 본인의 꽃가루도 더해줘야 해요..
            sum_val = arr[i][j]

            # dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]], 델타 탐색
            for dx, dy in dxy:
                # 각 방향으로 탐색을 몇 번해야 한다 ??? 꽃가루 개수만큼 해야한다!
                for dist in range(1, arr[i][j] + 1):
                    # 델타에 퍼져나가는만큼 곱해줘서 이동한다 .
                    # dist는 1부터 시작하고, 거리가 멀어질수록 이동거리가 늘어난다.
                    ni = i + dx * dist
                    nj = j + dy * dist

                    # 범위 안에 해당할 경우에만 꽃가루를 더한다.
                    if 0 <= ni < N and 0 <= nj < M:
                        sum_val += arr[ni][nj]
                    # 범위를 한 번이라도 벗어나면, 그 방향은 앞으로 계속 벗어나 있다.
                    # 그러니까 해당 방향의 탐색을 중단한다.
                    else:
                        break

            # 여기까지 왔따는건 다 더했다는거다.
            max_value = max(max_value, sum_val)

    print(f'#{tc} {max_value}')