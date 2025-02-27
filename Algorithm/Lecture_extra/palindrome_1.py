# m: 찾고자 하는 회문의 길이
n = 8
m = int(input())
# 글자판을 입력받는다
board = [input() for _ in range(8)]
# 세로줄을 만드는 작업을 하자.
for i in range(8):
    col = ''
    for j in range(8):
        # print(board[j][i], end=' ')
        col += board[j][i]
    board.append(col)
# print(board)

count = 0

# 글자판에 각 줄에 대하여
for row in board:
    # 시작점을 0부터 갈수 있는 만큼 진행하자.
    for start in range(n - m + 1):
        succes = True
        # 회문 검사할때는 반복을 회문 길이의 반만 하면 된다.
        for i in range(m // 2):
            if row[start + i] != row[start + m - 1 - i]:
                # 회문이 아니다!
                succes = False
                break
        # 회문이었다면, count를 늘린다.
        if succes:
            count += 1

print(count)
