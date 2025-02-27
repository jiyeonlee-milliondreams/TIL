import sys
sys.stdin = open("hw_1210_input.txt", "r")

T = 10
for _ in range(1, T+1):

    test_case = int(input())    # 테스트 케이스 번호 입력 받기
    arr = [list(map(int, input().split())) for _ in range(100)]     # 배열의 크기 100*100

    starts = []    # 출발점 후보군

    for j in range(100):
        if arr[0][j] == 1:
            starts.append(j)

    for start in starts:    # 후보군 수만큼 반복
        i = 0
        j = start
        success = 0
        for i in range(100):
            if i == 0 or j == 0 or j == 99:
                i + 1
            elif 0 <= i < 99 and 0 < j < 99:  # out of range 방지용
                # arr[i][j] 기준 오른쪽과 아래쪽을 더해 2라면 오른쪽으로 이동
                if arr[i+1][j] + arr[i][j+1] == 2:
                    j += 1
                # arr[i][j] 기준 아래쪽과 왼쪽을 더해 2라면 왼쪽으로 이동
                elif arr[i+1][j] + arr[i][j-1] == 2:
                    j -= 1
                else:
                    i += 1
    print(f'#{test_case}', arr[i][j])
            # else:
            #     i += 1
            #     print(arr[i][j])

    #     if arr[100][j] == 2:
    #         success = start
    #
    # print(f'#{test_case} {success}')
