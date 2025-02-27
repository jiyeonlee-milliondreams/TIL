T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    card = list(map(int, input()))
    COUNTS = [0] * (max(card) + 1)
    max_COUNTS_idx = 0

    for i in range(N):
        COUNTS[card[i]] += 1

    for i in range(len(COUNTS)):
        if COUNTS[max_COUNTS_idx] <= COUNTS[i]:
            max_COUNTS_idx = i

    print(f'#{test_case}', max_COUNTS_idx, COUNTS[max_COUNTS_idx])