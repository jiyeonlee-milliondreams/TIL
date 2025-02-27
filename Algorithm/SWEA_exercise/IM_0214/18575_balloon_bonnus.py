import sys
sys.stdin = open('18575_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    ballon = [list(map(int, input().split())) for _ in range(N)]


    for i in range(N):
        for j in range(N):


            # for di, dj in [0, 1], [1, 0], [0, -1], [-1, 0]:
            #     for dist in range():

