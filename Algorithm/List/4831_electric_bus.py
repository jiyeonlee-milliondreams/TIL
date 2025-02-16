import sys
sys.stdin = open('4831_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):

    K, N, M = list(map(int, input().split()))  # 1회 충전시 최대 이동 정류장 수 K, 0부터 N까지 운행하는 버스, 충전기가 설치된 정류장 개수 M
    charging_st = list(map(int, input().split()))

    stations = [0] * (N + 1)     # 정류소 0으로 초기화
    for charge in charging_st:  # 충전 가능한 정류소 1로 표시
        stations[charge] = 1

    i = 0
    while i < N:
        if stations[i + K + 1] == 1:
            i += (k+1)



    # for i in range(len(stations)):    # 정류소를 순회하며
    #     # 정차 지점 기준 + K 만큼의 구간 동안 반복하며 값이 1인 인덱스를 구하고 이때 가장 마지막 인덱스를 저장
    #
    #     for start in range(i+K+1):  # K만큼의 구간동안 반복하며 최대 인덱스 찾기
    #         max_idx = start + i  # 최대 인덱스를 구간의 첫 인덱스로 설정
    #         if max_idx <= stations[start + i]:
    #             max_idx = start + i
