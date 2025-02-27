import sys
sys.stdin = open("1974_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):

    arr = [list(map(int, input().split())) for _ in range(9)]
    print(arr)
    result = 0
    N = 9

    '''행 우선 검증'''
    for i in range(N):

        count = [0] * 10

        for j in range(N):
            count[arr[i][j]] += 1
            print(count)
    #     for c in count:
    #         if c != 1:
    #             break
    # print(result)
