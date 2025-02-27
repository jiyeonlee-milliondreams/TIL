import sys
sys.stdin = open("11092_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):  # 테스트 케이스 수만큼 반복

    N = int(input())
    numbers = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0

    for i in range(N):  # 최대값, 최소값 인덱스 구하기
        if numbers[max_idx] <= numbers[i]:  # 최대값은 마지막 인덱스
            max_idx = i
        if numbers[min_idx] > numbers[i]:   # 최소값은 첫 인덱스
            min_idx = i

    if max_idx >= min_idx:  # 절대값 구하기
        result = max_idx - min_idx
    else:
        result = -(max_idx - min_idx)

    print(f'#{test_case} {result}')
