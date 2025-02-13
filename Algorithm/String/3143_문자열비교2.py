import sys
sys.stdin = open('3143_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1): # EOFError 발생시, test_case 반복 횟수 확인하기
    A, B = input().split()

    n = len(A)
    m = len(B)

    count_B = 0     # A에 B가 얼마나 있는지 개수 0 으로 초기화

    i = 0
    while i <= n-m:
        # if 0 <= i + m < n:
        if A[i:i+m] == B:
            count_B += 1
            i += m
        else:
            i += 1

    # 타이핑 횟수. B가 있는 횟수만큼 (B의 길이(m) - 1)씩 A의 길이(n)에서 줄어든다
    typing = n - ((m-1) * count_B)

    print(f'#{test_case}', typing)

''' for 문으로 구현'''
# for start in range(n-m+1):  # 비교의 시작점을 0부터 n-m까지 순회하며
#     if A[start:start + m] == B:   # B 문자열과 같은 구간이 있다면. 슬라이싱은 마지막 값 미포함.
#         count_B += 1    # 개수 1증가
