# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 초기 최소값, 최대값을 설정하자!
    # 첫 번째 값으로 설정하자!
    # max_num = 0 으로 해도 되고, min_num = 1000000 으로 해도 된다.
    max_num = nums[0]
    min_num = nums[0]

    # 주어진 배열을 순회하면서, 최대/최소값을 갱신하자.
    for num in nums:
        # 순회한 값이 현재 최대값보다 크면, 최대값 갱신!!
        if num > max_num:
            max_num = num
        # 순회한 값이 현재 최소값보다 작으면, 최소값이 갱신된다!
        if num < min_num:
            min_num = num
    result = max_num - min_num

    print(f"#{tc} {result}")
