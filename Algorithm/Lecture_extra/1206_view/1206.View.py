import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, 11):
    N = int(input())  # 건물 개수
    buildings = list(map(int, input().split()))  # 건물 높이 정보

    # 조망권 확보 세대 수
    total_view = 0
    # 첫 번째 검사 대상의 건물 인덱스
    # 왼쪽에서 2번째는 검사할 필요가 없다. 왼쪽 2칸이 확보 X
    i = 2

    # 오른쪽 2칸 전까지 모든 건물의 조망권을 검사한다.
    while i < N-2:
        cnt_building_h = buildings[i]  # 현재 조망권 확인하려고 하는 건물의 높이
        left1, left2 = buildings[i - 2], buildings[i - 1]  # 기준 건물의 왼쪽 2개 건물
        right1, right2 = buildings[i + 1], buildings[i + 2]  # 기준 건물의 오른쪽 2개 건물

        max_h = max(left1, left2, right1, right2)  # 좌우 총 4개 건물에서 가장 큰 높이를 가져온다.
        # 좌우 4개의 건물들의 최대 높이가 현재 건물보다 작으면
        # 그 차이만큼 조망권을 확보한다!
        if max_h < cnt_building_h:
            total_view += (cnt_building_h - max_h)
            i += 3  # 현재 건물이 조망권을 확보했다면 => 좌우 2개의 건물들은 실제로 조망권을 무조건 확보 X
        # 그 외의 경우 ( 좌우 4개의 최대 높이가 현재 건물보다 같거나 높은 경우 => 조망권 확보 X => 옆 건물로 ㄱㄱ)
        else:
            i += 1



    print(f'#{tc} {total_view}')










