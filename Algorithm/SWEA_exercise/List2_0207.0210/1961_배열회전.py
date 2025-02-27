import sys
sys.stdin = open("1961_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rotate_90_clockwise = list(zip(*arr[::-1]))     # 90도 회전

    rotate_180_clockwise = list(zip(*rotate_90_clockwise[::-1]))        # 90도 회전 결과를 받아서 180도 회전

    rotate_270_clockwise = list(zip(*rotate_180_clockwise[::-1]))       # 180도 회전 결과 받아서 270도 회전

    # 테스트 케이스 번호 우선 출력 후, 조인 활용해서 출력.
    # 90도 첫번째 줄, 180도 첫번째 줄, 270도 첫번째 줄 각각을 map으로 str 처리 후, join 처리함.
    print(f"#{test_case}")
    for row1, row2, row3 in zip(rotate_90_clockwise, rotate_180_clockwise, rotate_270_clockwise):
        print("".join(map(str, row1)), "".join(map(str, row2)), "".join(map(str, row3)))

        # print(f'#{test_case}')
        # for rotate_result in zip(rotate_90_clockwise, rotate_180_clockwise, rotate_270_clockwise):
        #     for i in range(N):
        #         result = ''.join(map(str, rotate_result[i]))
        # print(result)


# N = 3
# a = ((7, 4, 1), (9, 8, 7), (3, 6, 9))
# for i in range(N):
#     result_list = []
#     for j in range(N):
#         result_list.append(a[j])
#         print(result_list)

# def my_func(*args):
#     return *args