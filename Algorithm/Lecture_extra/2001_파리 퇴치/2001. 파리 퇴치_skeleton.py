# 파일 입출력을 사용하는 경우 (local 테스트용)
import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스 수 입력
T = int(input().strip())
for test_case in range(1, T + 1):
    # N: 배열의 크기, M: 파리채의 크기
    N, M = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 우리가 원하는 건 , 파리채로 죽일 수 있는 최대 파리의 수
    kill_flies = 0

    # 파리를 순회하면서 각각 파리채로 찍어본다.
    # 파리채만큼의 범위를 확보하기 위해서 N-M+1 까지만 순회를 해야한다.
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            #  (i,j)가 이동할 때마다 매번 초기화해서 다시 죽이 파리수를 구해야함
            tmp_sum = 0
            for m in range(M):
                for n in range(M):
                    tmp_sum = grid[i + m][j + n]
            # 파리채 영역만큼 다 더해주고 나서 도달..
            # if kill_flies < tmp_sum:
            #     kill_flies = tmp_sum
            kill_flies = max(kill_flies, tmp_sum)

    print(f"#{test_case} {kill_flies}")
