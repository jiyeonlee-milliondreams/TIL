import sys
sys.stdin = open("4834_숫자카드_input.txt", "r")

T = int(input())            # 테스트 케이스의 수

for test_case in range(1, T+1):    # T개의 테스트 케이스이므로, 1부터 T+1까지 순회

    N = int(input())
    card = list(map(int, input()))

    COUNTS = [0] * (max(card) + 1)
    max_COUNTS_idx = 0

    for i in range(N):    # 카드에 적힌 숫자별 개수
        COUNTS[card[i]] += 1

    for i in range(len(COUNTS)):    # 가장 많은 카드에 적힌 숫자
        if COUNTS[max_COUNTS_idx] <= COUNTS[i]:
            max_COUNTS_idx = i

    print(f'#{test_case}', max_COUNTS_idx, COUNTS[max_COUNTS_idx])

# elif COUNTS[max_COUNTS_idx] == COUNTS[i]:
# max_COUNTS_idx = i