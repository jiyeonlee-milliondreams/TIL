# 일단.....칠판을 다 가져오고
board = [list(input()) for _ in range(5)]

# 최대 길이를 찾는다.
max_row = 0
for i in range(5):
    max_row = max(len(board[i]), max_row)

# 세로로 순서대로 읽을때의 결과를 저장할 리스트 또는 문자열을 준비하자.
result = []

# for를 두번 하는데,
# i, j로 한다면
# board[j][i]를 읽어야 한다. 그래야 세로로 읽을 수 있다.
for i in range(max_row):
    # 다섯줄로 쓰기때문에 y는 0 ~ 4
    for j in range(5):
        # 길이가 서로 다를 수 있으므로, 최대 길이를 먼저 알아두고,
        # 현재 읽고 있는 줄이 그 길이가 안되면 스킵(continue).
        if len(board[j]) <= i:
            continue
        # 세로를 먼저 바꾸기 위해 j를 앞쪽에 둔다.
        result.append(board[j][i])

print(''.join(result))
