N = 5
matrix = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
# 주 대각선 합 구하기
main_diagonal_sum = 0
# i와 같은 j 부분은 주 대각선이다.
# 왼쪽 위 -> 오른쪽 아래 방향의 대각선 값들을 합해준다.
for i in range(N):
    for j in range(N):
        if i == j:
            main_diagonal_sum += matrix[i][j]

# 똑같은 코드입니다.
# for i in range(N):
#     main_diagonal_sum += matrix[i][i]

# 부 대각선의 합
# 우상단 -> 좌하단으로 가는 대각선
sub_diagonal_sum = 0
for i in range(N):
    for j in range(N):
        if i == N - 1 - j:
            sub_diagonal_sum += matrix[i][j]

# 부 대각선의 합 ( 같은 코드 입니다 )
# for i in range(N):
#     sub_diagonal_sum += matrix[i][N-1-i]

# 두 대각선의 합을 구할건데 ( 가운데 값, 즉 중복을 제거해야 한다)
# 2번 더해졌기 떄문이다 ( 주대각선에서 한번, 부대각선에서 한번)
middle_value = matrix[N // 2][N // 2]  # 가운데 원소 값입니다.

total_diagonal_sum = main_diagonal_sum + sub_diagonal_sum - middle_value
print(total_diagonal_sum)


