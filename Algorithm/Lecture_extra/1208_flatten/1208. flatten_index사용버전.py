import sys

sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    dump = int(input())  # 상자를 옮길 수 있는 횟수
    box_heights = list(map(int, input().split()))

    # 여기 왜 언더바로 하나요 ? =>
    # 이 for문은 반복문에 불가하다.
    for _ in range(dump):
        max_box_height = max(box_heights)  # 이번 덤프해야 되는 타이밍에 가장 높은 상자의 높이를 구한다.
        min_box_height = min(box_heights)  # 가장 낮은 높이의 상자

        # 평탄화 높이 차이가 1이하이면, 굳이 평탄화를 할 필요가 없다.
        if max_box_height - min_box_height <= 1:
            break

        # 가장 높은 상자의 높이를 1 낮추고, 가장 낮은 상자의 높이를 1 높힌다.
        max_idx = box_heights.index(max_box_height)
        min_idx = box_heights.index(min_box_height)

        box_heights[max_idx] -= 1
        box_heights[min_idx] += 1

    # 평탄화 끝나고 나서도, 또 최대 높이의 상자와 최소 높이의 상자가 바뀌었을 수도 있다.
    print(f'#{test_case} {max(box_heights) - min(box_heights)}')
