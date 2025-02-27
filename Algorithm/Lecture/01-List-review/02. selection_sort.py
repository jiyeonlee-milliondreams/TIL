# 필독!!!
# 알고리즘 구현 코드에 정답은 없습니다!!!!!
# 구현은 다양한 방식으로 할 수 있으며, 더 효율적인 방법이 존재할 수 있습니다.
# 각 알고리즘의 핵심 개념만 구현되어 있다면, 모두 훌륭한 코드입니다. 
# 따라서 아래 코드를 참고하여, 본인만의 방식으로 해당 알고리즘을 구현해보기를 권장합니다.

def selection_sort(arr):
    n = len(arr)  # 배열의 길이

    # 최소값을 찾는 행위를 n-1번 반복한다고 했죠.
    # 맨 마지막 값은 굳이 비교할 필요가 없습니다. (n-1 까지만 순회)
    for i in range(n-1):
        min_idx = i  # 인덱스로 저장합니다 why ? 위치를 교환하기 위해서

        # 최소값을 찾는 로직
        # 근데 i(최소값을 찾은 횟수), 이 횟수 + 1 에서부터 최소값을 찾아야한다. 어디까지? n 끝까지
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:  # 현재까지의 최소값보다 작은 값이 발견될 경우
                min_idx = j  # 최소값 인덱스를 갱신

        # 끝까지 돌아서 최소값을 찾았으면, i와 교환해서 최소값을 앞으로 보낸다.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [64, 25, 10, 22, 11]
selection_sort(arr)
print(arr)  # [10, 11, 22, 25, 64]
