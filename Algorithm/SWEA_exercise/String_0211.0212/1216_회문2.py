import sys

sys.stdin = open("1216_input.txt", "r")


def reverse_method(arr):  # 문자열 뒤집는 함수
    N = len(arr)
    for i in range(N // 2):
        arr[i], arr[N - 1 - i] = arr[N - 1 - i], arr[i]
    return arr


T = 10
for _ in range(1, T + 1):

    test_case = int(input())
    N = 100
    arr = [list(map(str, input())) for _ in range(N)]
    result = 0
    for i in range(N):
        for k in range(100, 0, -1):  # k 회문의 길이 100부터 1까지 역순으로 검증
            for j in range(N - k + 1):  # j 회문의 시작점 후보
                if arr[i][j] == arr[i][j+k-1]:  # 회문의 제일 바깥 값이 서로 같을 경우, while문 돌리기
                    o = j+1  # o의 초기값은 j를 받음.
                    while o < k // 2:  # k의 절반까지 i를 옮겨가며 회문 여부 비교
                        if arr[i][o] == arr[i][k - o]:
                            o += 1
                        else:
                            break
            if o == k // 2:
                if result < k:
                    result = k

    for j in range(N):
        for k in range(100, 0, -1):  # k 회문의 길이 100부터 1까지 역순으로 검증
            for i in range(N - k + 1):  # i 회문의 시작점 후보
                if arr[i][j] == arr[i+k-1][j]:  # 회문의 제일 바깥 값이 서로 같을 경우, while문 돌리기
                    o = i+1  # o의 초기값은 i를 받음.
                    while o < k // 2:  # k의 절반까지 j를 옮겨가며 회문 여부 비교
                        if arr[i][o] == arr[i][k - o]:
                            o += 1
                        else:
                            break
            if o == k // 2:
                if result < k:
                    result = k

    print(f'{test_case} {result}')

# for k in range(100, 0, -1): # k 회문의 길이 100부터 1까지 역순으로 검증
#     for j in range(N-k+1):  # j 회문의 시작점 후보
#         o = j   # o의 초기값은 j를 받음.
#         while o < k//2:     # k의 절반까지 i를 옮겨가며 회문 여부 비교
#             if arr[o] == arr[k-1-o]:
#                 o += 1
#             else:
#                 break
#         if o == k//2:
#             result = k
#
