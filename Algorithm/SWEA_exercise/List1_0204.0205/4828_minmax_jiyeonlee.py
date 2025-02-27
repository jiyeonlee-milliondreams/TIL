T = int(input())            # 테스트 케이스의 수
for tc in range(1, T+1):    # T개의 테스트 케이스이므로, 1부터 T+1까지 순회

    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]           # 첫 원소를 최대값으로 가정
    min_v = arr[0]           # 첫 원소를 최소값으로 가정

    for i in range(1, N):   # 첫 원소 스스로 비교 건너뛰고 두번째 원소부터 비교
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]

    print(f'#{tc} {max_v-min_v}')