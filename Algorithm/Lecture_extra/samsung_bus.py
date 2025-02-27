# 버스의 갯수
n = int(input())
# 각 버스들의 정보 받기
bus_routes = [
    list(map(int, input().split())) for _ in range(n)
]
# 알고싶은 정류장의 갯수
p = int(input())
# 확인할 정류장들 정보 받기
check_stations = [int(input()) for _ in range(p)]

# 모든 정류장들에 방문하는 버스를 리스트로 만들어두자.

# 각 버스 마다 한번씩
    # 노선의 출발과 시작점 사이의 모든 정류장들을
        # 하나씩 증가시킨다.

# 이제 확인하고 싶은 정류장별로 몇번 정차했는지를 확인하고,

# 정리해서 출력하자.

