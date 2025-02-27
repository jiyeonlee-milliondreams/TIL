T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각 처리.

for test_case in range(1, T + 1):

    good_view_house = 0     # 조망권이 확보된 세대수를 0으로 가정
    tested_list = []
    N = int(input())        # 건물의 수
    arr = list(map(int, input().split()))   # 각 건물의 층수

    for i in range(2, N-2):     # 양쪽 2칸은 건물이 없으므로, 인덱스 2부터 N-1까지

        # [i] 기준 양옆 두 칸 중 최대 층수
        max_level = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        if max_level < arr[i]:
            good_view_house += arr[i] - max_level

    print(f'#{test_case} {good_view_house}')


# T = 10
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리.
# for test_case in range(1, T + 1):
#
#     good_view_house = 0     # 조망권이 확보된 세대수를 0으로 가정
#     tested_list = []
#     N = int(input())        # 건물의 수
#     arr = list(map(int, input().split()))   # 각 건물의 층수

    # for i in range(2, N-2):
    #     for j in range(i):
    #         test_list = arr[j] - arr[j-2], arr[j] - arr[j-1], arr[j] - arr[j+1], arr[j] - arr[j+2]
    #
    #         for test in test_list:
    #             if test > 0:
    #                 tested_list.append(test)
    #
    #         if len(tested_list) == 4:
    #             good_view_house += min(tested_list)
    #
    #
    # print(f'#{test_case} {good_view_house}')
    # # print(type(test_list))