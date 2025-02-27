import sys
sys.stdin = open('input.txt')


for _ in range(10):
    test_case = int(input())
    n = 100
    board = [input() for _ in range(n)]
    # 회문의 최대길이 저장용 변수
    max_length = 1
    # 세로줄도 보드에 추가하자.
    for i in range(n):
        col = ''
        for j in range(n):
            col += board[j][i]
        board.append(col)
    # board의 각 줄마다 확인하면서
    for row in board:
        # 검색하고자 하는 회문의 길이를 정한다.
        for m in range(n, max_length, -1):
            # 회문의 시작지점을 정한다음
            for start in range(n - m + 1):
                success = True
                # 회문인지 검사한다.
                for i in range(m // 2):
                    if row[start + i] != row[start + m - 1 - i]:
                        # 회문이 아니라면 실패!
                        success = False
                        break
                # for가 정상종료되면 회문이었다!
                if success:
                    # 그러면 max_length를 갱신하자!
                    max_length = m
                    break
            # 길이 m짜리 회문을 찾으면 max_length가 m이 된다
            if m == max_length:
                # 그러면 다음줄로 넘어가도 된다!
                break

    print(f'#{test_case} {max_length}')
