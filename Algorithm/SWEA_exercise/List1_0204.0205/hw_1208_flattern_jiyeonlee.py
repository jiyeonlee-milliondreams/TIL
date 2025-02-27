import sys
sys.stdin = open("hw_1208_input.txt", "r")

'''방법(1)'''
T = 10

# 여러개의 테스트 케이스가 주어지므로, 각각 처리.
for test_case in range(1, T + 1):

    dump = int(input())  # 덤프 횟수
    numbers = list(map(int, input().split()))  # 각 상자의 높이

    max_idx = 0  # 첫 인덱스를 최대 높이로 가정
    min_idx = 0  # 첫 인덱스를 최소 높이로 가정

    for i in range(dump):  # 덤프 횟수만큼 평탄화 반복
        for j in range(100):  # 최대 높이, 최소 높이 찾기
            if numbers[max_idx] < numbers[j]:
                max_idx = j
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        if numbers[max_idx] > numbers[min_idx]:
            numbers[max_idx] -= 1
            numbers[min_idx] += 1

    for j in range(100):  # 평탄화 후에도 최대 높이의 상자와 최소 높이의 상자를 구해야 한다.
        if numbers[max_idx] < numbers[j]:
            max_idx = j
        if numbers[min_idx] > numbers[j]:
            min_idx = j

    print(f'#{test_case}', numbers[max_idx] - numbers[min_idx])

'''방법(2)'''
# dump = int(input())  # 덤프 횟수
# numbers = list(map(int, input().split()))  # 각 상자의 높이
#
# max_idx = 0  # 첫 인덱스를 최대 높이로 가정
# min_idx = 0  # 첫 인덱스를 최소 높이로 가정
#
# def dump_function(num):
#     for j in range(1, len(num)):  # 최대 높이, 최소 높이 찾기
#         if num[max_idx] < num[j]:
#             max_idx = j
#         if num[min_idx] > num[j]:
#             min_idx = j
#
#     num[max_idx] -= 1
#     num[min_idx] += 1
#
# # 여러개의 테스트 케이스가 주어지므로, 각각 처리.
# for test_case in range(1, T + 1):
#     for i in range(dump):  # 덤프 횟수만큼 평탄화 반복
#         dump_function(numbers)
#     print(f'#{test_case} {numbers[max_idx] - numbers[min_idx]}')




'''방법(3)'''
# # 여러개의 테스트 케이스가 주어지므로, 각각 처리.
# for test_case in range(1, T + 1):
#     dump = int(input())  # 덤프 횟수
#     numbers = list(map(int, input().split()))  # 각 상자의 높이
#
#     max_idx = 0  # 첫 인덱스를 최대 높이로 가정
#     min_idx = 0  # 첫 인덱스를 최소 높이로 가정
#
#     for i in range(dump):  # 덤프 횟수만큼 평탄화 반복
#         max_v = max(numbers)
#         min_v = min(numbers)
#         max_idx = numbers.index(max_v)
#         min_idx = numbers.index(min_v)
#         numbers[max_idx] -= 1
#         numbers[min_idx] += 1
#
#     print(f'#{test_case}', numbers[max_idx] - numbers[min_idx])
