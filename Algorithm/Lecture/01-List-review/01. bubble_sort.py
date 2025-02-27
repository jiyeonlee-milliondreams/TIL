# 필독!!!
# 알고리즘 구현 코드에 정답은 없습니다!!!!!
# 구현은 다양한 방식으로 할 수 있으며, 더 효율적인 방법이 존재할 수 있습니다.
# 각 알고리즘의 핵심 개념만 구현되어 있다면, 모두 훌륭한 코드입니다. 
# 따라서 아래 코드를 참고하여, 본인만의 방식으로 해당 알고리즘을 구현해보기를 권장합니다.

def bubble_sort(arr):  # 오름차순 정렬!
    n = len(arr)  # 배열의 길이
    # 아래 코드 작성

    # 최대값을 n번 찾아야 한다. ( 정렬되지 않은 리스트 중에서)
    for i in range(n):
        # 오른쪽으로 이동하면서, 인접한 원소와 크기를 비교하면서
        # 제일 끝에 최대값을 옮긴다.
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:  # 현재 요소가 다음 요소(인접 요소)보다 크면 => 교환
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [55, 7, 78, 12, 42]
bubble_sort(arr)
# print(arr)  # [7, 12, 42, 55, 78]