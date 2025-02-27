# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input()))

    card_counts = [0] * 10  # 0~9까지 숫자의 개수를 저장할 리스트

    # 숫자 개수 세기
    for card_num in cards:
        card_counts[card_num] += 1

    # 최빈값 찾기 (같으면 큰 숫자 선택)
    max_num = 0
    max_count = 0

    # 숫자별 등장 횟수를 저장한 배열을 탐색
    for i in range(10):
        # 등장 횟수가 더 많은 경우, 최대값과 횟수 갱신하기
        # !! 같을 경우에 값도 갱신하는 이유는??
        # => 등장 횟수가 같다면 어차피 늦게 접근하는 값이 더 크니까!!!!
        if card_counts[i] >= max_count:
            max_num = i
            max_count = card_counts[i]

    print(f"#{tc} {max_num} {max_count}")
