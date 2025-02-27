def pascal_triangle(row, col):
    # 종료 조건
    if col == 0:
        return 1
    if row == col:
        return  1

    return pascal_triangle(row-1, col-1) + pascal_triangle(row-1, col)

N = int(input())
result = []
for i in range(N):
    row = []
    for j in range(i+1):
        row.append(pascal_triangle(i, j))

    result.append(row)

print(result)