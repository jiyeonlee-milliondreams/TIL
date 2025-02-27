import sys
sys.stdin = open("4864_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):

    str1 = input()
    str2 = input()
    print(str1, str2)

    N1 = len(str1)
    N2 = len(str2)
    print(N1, N2)

    for i in range(N2-N1):  # 기준이 되는 i 가 0부터 N2-N1까지 반복
        if str1[0] == str2[i]:
            idx = i




