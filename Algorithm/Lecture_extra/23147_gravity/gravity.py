# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZTP6dSqXwrHBIRD&categoryId=AZTP6dSqXwrHBIRD&categoryType=CODE

import sys
sys.stdin = open('sample_input.txt')

# 테스트 케이스 개수 입력
T = int(input())

for tc in range(1, T + 1):
    width = int(input())  # 방의 가로 길이
    box_heights = list(map(int, input().split()))  # 각 열의 상자 높이

    max_drop = 0  # 최댓값 낙차 저장

    # 왼쪽에 있는 상자 위치부터 오른쪽 열에 자신보다 높이가 같거나 높은 상자의 개수를 파악하고, 
    # 그 수만큼 낙차 감소
    for i in range(width):
        current_height = box_heights[i]  # 현재 열의 상자 높이
        # 현재 위치의 다음 칸부터 박스의 너비를 뺀 거리가 최대로 떨어질 수 있는 거리
        drop_height = width - (i + 1)
        high_box_count = 0  # 현재 박스에서 오른쪽에 있는 박스 중에 현재 박스보다 같거나 높은 박스의 수

        # 현재 위치 이후의 상자들과 비교하여 같거나 큰 박스의 수 계산하기
        for j in range(i + 1, width):
            if box_heights[j] >= current_height:  # 오른쪽에 현재보다 높은 상자가 있다면
                high_box_count += 1

        # 같거나 높은 박스의 수만큼 최대로 떨어질 수 있는 거리에서 감소하기
        drop_height -= high_box_count

        # 최대로 떨어질 수 있는 높이 갱신
        max_drop = max(max_drop, drop_height)

    print(f'#{tc} {max_drop}')
