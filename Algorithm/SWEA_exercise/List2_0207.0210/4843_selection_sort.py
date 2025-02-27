import sys

sys.stdin = open("4843_input.txt", "r")


def max_select_search(arr, N):
    for i in range(0, 5):  # 처음부터 5번째 최대 원소를 찾는 선택 정렬
        max_idx = i  # 최대 값을 순회하는 인덱스로 초기화
        for j in range(i + 1, N):  # i를 기준으로 그 다음 인덱스부터 순열 끝까지 i와 비교
            if arr[max_idx] < arr[j]:
                max_idx = j
        # i 위치에 갱신된 max_idx 값 넣기. 기준별로 반복문 다 돌았을 때 최대 원소 위치 갱신.
        arr[max_idx], arr[i] = arr[i], arr[max_idx]
    return arr[0:5]  # 처음부터 5번째로 큰 숫자 리스트로 반환

def min_select_search(arr, N):
    for i in range(0, 5):   # 처음부터 5번째 최소 원소를 찾는 선택 정렬
        min_idx = i     # 최소 값을 순회하는 인덱스로 초기화
        for j in range(i + 1, N):   # i를 기준으로 그 다음 인덱스부터 순열 끝까지 i와 비교
            if arr[min_idx] > arr[j]:
                min_idx = j
        # i 위치에 갱신된 min_idx 값 넣기. 기준별로 반복문 다 돌았을 때 최대 원소 위치 갱신.
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr[0:5]   # 처음부터 5번째로 작은 숫자 리스트로 반환

T = int(input())

for test_case in range(1, T+1): # 테스트 케이스 수만큼 반복

    N = int(input())
    arr = list(map(int, input().split()))

    max_numbers = max_select_search(arr, N) # 최대 값의 리스트 호출
    min_numbers = min_select_search(arr, N) # 최소 값의 리스트 호출

    # 문제 조건에 맞게 출력
    print(f'#{test_case}',
          max_numbers[0],
          min_numbers[0],
          max_numbers[1],
          min_numbers[1],
          max_numbers[2],
          min_numbers[2],
          max_numbers[3],
          min_numbers[3],
          max_numbers[4],
          min_numbers[4],
          )


# arr = [4, 6, 3, 5, 11, 7, 2, 1, 4, 12]
#
# print(max_select_search(arr, 10))
# print(min_select_search(arr, 10, 2))

