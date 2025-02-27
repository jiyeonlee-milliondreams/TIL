N = 2
M = 3
for i in range(N):
    for i in range(M):
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni = i + di
            nj = i + dj
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)

'''연습문제(2)'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0

for i in range(N):
    for i in range(M):
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni = i + di
            nj = i + dj
            if 0 <= ni < N and 0 <= nj < M:
                total += abs(arr[ni][nj] - arr[i][j]) # 차이의 절대값
print(total)

'''
1) 대각선 위, 아래
if i < j
if i > j

2) 대각선 자체
for i in range(N):
    arr[i][i]

'''