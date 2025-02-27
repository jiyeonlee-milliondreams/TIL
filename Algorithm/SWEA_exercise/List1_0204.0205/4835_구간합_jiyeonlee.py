T = int(input())  # 테스트 케이스의 수


def sum(numbers):  # 내장함수 sum 대신 sum을 직접 정의하는 연습
    sum_numbers = 0
    for number in numbers:
        sum_numbers += int(number)
    return sum_numbers


for test_case in range(1, T + 1):  # T개의 테스트 케이스이므로, 1부터 T+1까지 순회

    N, M = map(int, input().split())  # 정수의 개수 N, 구간의 개수 M
    num = list(map(int, input().split()))  # 정수 리스트

    max_sum = sum(num[0:0 + M])  # 최대합의 초기값은 첫 원소부터의 합
    min_sum = sum(num[0:0 + M])  # 최소합의 초기값은 첫 원소부터의 합

    for i in range(N - (M - 1)):  # 첫 원소부터 마지막에서 M-1까지
        if max_sum < sum(num[i:i + M]):
            max_sum = sum(num[i:i + M])
        if min_sum > sum(num[i:i + M]):
            min_sum = sum(num[i:i + M])

    print(f'#{test_case} {max_sum - min_sum}')
