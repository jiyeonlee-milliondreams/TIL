import sys
sys.stdin = open("1954_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    arr = [[0] * N for _ in range(N)]
    number = 0  # 빈칸에 넣을 숫자 테스트 케이스별 초기화

    # [0,0], [1,1]과 같이 대각선 인덱스를 시작점으로 해서 회전
    # 단, 반복 횟수는 홀수는 N//2 + 1 짝수는 N//2이므로 N % 2(홀수일때 1, 짝수일때 0) 활용
    if N % 2 != 0:
        M = N//2 + 1
    else:
        M = N//2
    for i in range(M):
        j = i
        for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]: # 오른쪽부터 시계방향으로 변화
            for dist in range(N):    # 0부터 N-1까지 반복 후 위 for문으로 올라가서 di, dj 변화
                if dist < N-1:
                    ni = i + di * dist  # di에 dist를 곱해서 반복
                    nj = j + dj * dist  # dj에 dist를 곱해서 반복
                    if 0 <= ni < N and 0 <= nj < N:
                        number += 1  # 빈칸에 넣을 숫자 1 증가 후
                        print(number)
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = number  # 해당 칸에 할당
                else:
                    i = i + di * dist
                    j = j + dj * dist


    print(f'#{test_case}', arr)




    #
    # for i in range(1):
    #     for j in range(N-1):
    #         if j <= N-2 and arr[i][j] == 0:
    #             numbers += 1
    #             arr[i][j] = numbers
    #         else:
    #             for i in range(1, 2):
    #
    #         elif j == N-1 and arr[i][j] == 0:
    #             numbers += 1
    #             arr[i][j] += 1
    #         elif j == N-1 and arr[i]


