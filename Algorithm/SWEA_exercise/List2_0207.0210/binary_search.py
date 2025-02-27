def binary_search(arr, N, key):
    # 검색 구간 설정
    start = 0
    end = N - 1

    while start <= end:  # 검색 구간에 1개 이상의 원소가 있으면 검색
        middle = (start + end) // 2 # 기준 위치 계산

        if arr[middle] == key:  # 검색 성공
            return middle
        elif arr[middle] > key: # key 보다 크다면 end가 middle의 하나 왼쪽으로 재설정.
            end = middle - 1
        else:   # key 보다 작으면 start가 middle의 하나 오른쪽으로 재설정.
            start = middle + 1
    return -1   # 검색 구간이 남아있지 않으면 검색 실패

arr = [2, 4, 7, 9, 11, 19, 23]  # 이진 검색은 반드시 배열이 오름차순 정렬 상태여야 함.
print(binary_search(arr, len(arr), 11))