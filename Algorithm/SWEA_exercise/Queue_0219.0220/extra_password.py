T = 10
for _ in range(T):
    tc = int(input())
    arr = list(map(int, input().split()))

    diff = 0        # (diff + 1) 만큼 감소
    idx = 0         # 감소시킬 위치
    while True:
        arr[idx] -= diff+1
        if arr[idx] <= 0:
            arr[idx] = 0
            break   # while True 암호 완성
        idx = (idx + 1) % 8         # 마지막 원소에서 0번 원소로 이동
        diff = (diff + 1) % 5
    # 출력
    print(f'#{tc}', end = ' ')
    for i in range(idx+1, idx+1+8):
        print(arr[i%8], end = ' ')
    print()