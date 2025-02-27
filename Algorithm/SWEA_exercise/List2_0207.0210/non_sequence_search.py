def sequential_search(arr, N, key):
    for i in range(N):
        if arr[i] == key:
            return i
    return -1

arr = [4, 9, 11, 23, 2, 19, 7]
print(sequential_search(arr, len(arr), 8))

