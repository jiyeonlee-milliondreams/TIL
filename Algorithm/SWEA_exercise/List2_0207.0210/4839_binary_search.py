import sys

sys.stdin = open("4839_input.txt", "r")


def binary_search(arr, N, key):
    start = 0  # 수열의 처음을 start로 설정
    end = N - 1  # 수열의 마지막을 end로 설정
    result = []

    while start <= end:  # 비교 구간이 1개 이상 있을 때 반복
        middle = (start + end) // 2  # 중간 값(기준 값)
        # 각 조건문별로 result에 중간 값 추가하기
        if arr[middle] == key:
            result.append(middle)
            return result
        elif arr[middle] > key:
            result.append(middle)
            end = middle - 1
        else:
            result.append(middle)
            start = middle + 1

    return result


T = int(input())

for test_case in range(1, T + 1):
    N, Pa, Pb = map(int, input().split())   # 수열의 수 N, a가 찾아야 하는 페이지 수 Pa, b가 찾아야 하는 페이지 수 Pb
    arr = list(range(1, N + 1)) # 1부터 N까지 숫자로 리스트 생성

    a = binary_search(arr, N, Pa)   # a가 찾아야 하는 페이지 수를 인자로 받아 함수 호출
    b = binary_search(arr, N, Pb)   # b가 찾아야 하는 페이지 수를 인자로 받아 함수 호출

    if len(a) < len(b):     # A, B, 0으로 결과 출력
        print(f'#{test_case} A')
    elif len(a) > len(b):
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} 0')
