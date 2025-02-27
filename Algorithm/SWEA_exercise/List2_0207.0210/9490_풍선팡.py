import sys

sys.stdin = open("9490_input.txt", "r")

# def delta_balloon(arr, N, M):
#     for i in range(N):
#         for j in range(M):
#             standard = arr[i][j]
#             flower_sum = arr[i][j]
#             for di, dj in [0,1], [1,0], [0,-1], [-1,0]:
#                 for o in range(1, standard+1):
#                     ni = i + di * o
#                     nj = j + dj * o
#                     flower_sum += arr[ni][nj]
#     return flower_sum

T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0  # 테스트 케이스별로 최대값 0으로 초기화

    for i in range(N):  # 행 우선 순회
        for j in range(M):  # 그 다음, 열 순회
            standard = arr[i][j]    # 기준 인덱스의 꽃가루 수 읽기
            flower_sum = arr[i][j]  # 꽃가루 합 초기값을 기준 값으로 설정
            for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:  # 오른쪽으로 시계 방향으로 이동하며 반복
                for dist in range(1, standard+1):  # 기준 인덱스의 꽃가루 수만큼 1부터 standard + 1 반복
                    ni = i + di * dist  # 1이라면 그대로, 2라면 2가 곱해지는 원리
                    nj = j + dj * dist  # [ni, nj]가 [0,1], [0,2]와 같이 변함.
                    if 0 <= ni < N and 0 <= nj < M:  # out of range 방지용
                        flower_sum += arr[ni][nj]   # 읽은 인덱스의 값 추가하기
                    else:
                        break
            if max_sum < flower_sum:    # 최대값 갱신은 기준값이 바뀔때마다 진행.
                max_sum = flower_sum

    print(f'#{test_case} {max_sum}')
