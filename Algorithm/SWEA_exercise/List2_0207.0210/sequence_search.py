def seq_search(arr, N, key):
    for i in range(N):
        if arr[i] == key:
            return i
        elif arr[i] > key:
            return -1
    return -1 # 모든 원소가 key보다 작으면 못 찾으므로 -1 반환


arr = [4, 9, 11, 23, 2, 19, 7]

arr.sort()
print(arr)
print(seq_search(arr, len(arr), 11))
print(seq_search(arr, len(arr), 101))
