import sys
sys.stdin = open('4881_input.txt', 'r')

'''
def f(i, N):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global min_v
    if i == N:
        s = 0
        for j in range(N):
            s += arr[j][p[j]]
        if min_v > s:
            min_v = s
    else:
        for j in range(i, N):   # i와 자리를 바꿀 j는 i부터 배열 끝까지 반복
            p[i], p[j] = p[j], p[i]     # 자리 교환
            f(i+1, N)   # i+1자리 결정
            p[i], p[j] = p[j], p[i]     # 원상 복구

T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # P[i] : i 행에서 고른 열 번호 저장
    p = [i for i in range(N)]

    min_v = 10000

    f(0, N)
    print(f'#{test_case} {min_v}')
'''

def f(i, N, s):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global min_v
    global count
    if i == N:  # i가 배열의 크기와 같다면
        if min_v > s:
            min_v = s
    elif min_v < s: # 중간 합계가 최소보다 크면 함수 중지(가지치기)
        return
    else:
        for j in range(i, N):   # i와 자리를 바꿀 j는 i부터 배열 끝까지 반복
            p[i], p[j] = p[j], p[i]     # 자리 교환
            f(i+1, N, s + arr[i][p[i]])   # i+1자리 결정
            p[i], p[j] = p[j], p[i]     # 원상 복구

T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # P[i] : i 행에서 고른 열 번호 저장
    p = [i for i in range(N)]

    min_v = 10000

    f(0, N, 0)
    print(f'#{test_case} {min_v}')
