n = int(input())
# 파스칼의 삼각형을 저장할 리스트를 만들자.
# 0번층은 직접 만들자.
pascal = [
    [1],
    # [1, 1],
    # [1, 2, 1],
    # [1, 3, 3, 1],
    # [1, 4, 6, 4, 1],
]

for i in range(1, n):
    # 다음줄의 첫번째 숫자는 어차피 1이다.
    row = [1]
    # 삼각형의 가로에 들어갈 숫자를 순회하는데,
    # 첫번째 1은 채웠고, 끝은 i - 1 idx까지 가야한다.
    for j in range(1, i):
        # 왼쪽 위 숫자와 바로 위 숫자를 더하고, 줄에 추가한다.
        row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
    # 마지막 숫자 1을 추가해준다.
    row.append(1)
    # 완성된 줄을 pascal에 추가한다.
    pascal.append(row)

for row in pascal:
    print(' '.join(map(str, row)))
