# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input()))

    card_cnt_dict = {}  # 숫자 개수를 저장할 딕셔너리

    # 등장 횟수 계산
    for card_num in cards:
        # 딕셔너리에서 없는 키에 접근하면 에러가 나기 때문에
        # 키가 존재하지 않다면, 해당 카드를 딕셔너리에 초기화한다.
        if card_num not in card_cnt_dict:
            card_cnt_dict[card_num] = 0

        # 현재 카드의 등장 횟수 + 1
        card_cnt_dict[card_num] += 1

    max_count = 0
    max_num = 0

    # 카드 등장 횟수를 저장한 딕셔너리를 순회하면서
    # 등장 횟수가 갱신되면, 최대 등장 횟수와 값을 갱신한다.
    for card_num in card_cnt_dict:
        # 현재까지의 최대 등장 횟수보다 큰 횟수가 나타난다면
        # 최댓값 및 최대 등장 횟수 갱신
        if card_cnt_dict[card_num] > max_count:
            max_count = card_cnt_dict[card_num]
            max_num = card_num

        # 최대값과 동일한 경우에는 적힌 숫자가 큰 쪽으로 최대값 갱신
        elif card_cnt_dict[card_num] == max_count and card_num > max_num:
            max_num = card_num

    print(f"#{tc} {max_num} {max_count}")
