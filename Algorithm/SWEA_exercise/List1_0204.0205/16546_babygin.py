import sys
sys.stdin = open("16546_input.txt", "r")

T = int(input())    # 테스트 케이스의 수

for test_case in range(1, T+1):

    arr = list(map(int, input().strip()))
    counts = [0] * 12
    # c[10], c[11]은 항상 0, 마지막 인덱스의 run, triplet 확인을 위한 여분

    for i in range(6):  # 단순 반복일 경우, _ 로 표시.
        counts[arr[i]] += 1     # counts 인덱스에 arr[i] 넣어서 값 1 증가

    t = r = 0
    j = 0
    while j < max(arr) + 1:   # 카드 번호 9까지이기 때문
        if counts[j] >= 3:  # triplet 확인
            counts[j] -= 3
            t += 1
            continue
        if counts[j] >= 1 and counts[j+1] >= 1 and counts[j+2] >= 1:    # run 확인
            counts[j] -= 1
            counts[j+1] -= 1
            counts[j+2] -= 1
            r += 1
            continue
        j += 1

    if r+t == 2:
        print(f'#{test_case} true')
    else:
        print(f'#{test_case} false')
