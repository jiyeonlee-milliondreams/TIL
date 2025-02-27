def selection_sort(arr, N): # 배열 이름, 크기
    for i in range(N-1):
        # 0부터 N-2인 동안 반복
        # 기준 위치가 정렬의 마지막에서 두번째에 위치할 때까지

        min_idx = i   # 최소값 인덱스 초기화, 구간의 맨 앞 원소를 최소로 가정
        for j in range(i+1, N): # 실제 최소값인지 그 다음 인덱스부터 끝까지 비교하기기
           if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [5, 1, 8, 10, 35, 20]
selection_sort(arr, len(arr))
print(arr)  # 위 함수에서 return 값이 없으므로, arr을 출력해야 함.

'''k번째로 작은 원소를 찾는 알고리즘'''
