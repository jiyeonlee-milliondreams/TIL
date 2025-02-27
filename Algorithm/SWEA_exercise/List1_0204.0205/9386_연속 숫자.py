import sys
sys.stdin = open("9386_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):  # 테스트 케이스 수만큼 반복

    N = int(input())
    numbers = list(map(int, input()))

    one_count = 0  # 연속한 1의 개수
    max_one_count = 0  # 연속한 1의 최대 개수

    for i in range(N):      # 전체 반복하며 숫자 하나씩 확인
        if numbers[i] == 1:     # 1이라면 one_count 1 증가
            one_count += 1

        if numbers[i] != 1:     # 0이라면 max_one_count 갱신
            if max_one_count < one_count:
                max_one_count = one_count
            one_count = 0       # one_count 재사용위해 0으로 초기화

        if i == N - 1:  # 순열의 마지막이 1인 경우, max_one_count 갱신
            if max_one_count < one_count:
                max_one_count = one_count


    print(f'#{test_case} {max_one_count}')

