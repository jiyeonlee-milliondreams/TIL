'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''

# 함수 만들기
def bfs(s, V):  # 시작 정점 s, 마지막 정점 V
    # visited 생성
    visited = [0] * (V + 1)     # 1부터 V까지 정점
    # Queue 생성
    q = []
    # 시작점 인큐
    q.append(s)
    # 시작점 인큐 표시
    visited[s] = 1
    # 큐가 비워질 때까지 반복     "front != rear"와 같은 의미
    while q:
        # 디큐해서 t에 저장    리스트의 제일 앞 원소 pop
        t = q.pop(0)
        # t 정점에 대한 처리   미로는 출구인지 확인하면 됨
        print(t)
        # t에 인접한 정점 w 중 인큐되지 않은 정점이 있으면
        for w in adj_l[t]:
            if visited[w] == 0:
                # 인큐하고 visited에 인큐 표시
                q.append(w)
                # 시작점으로부터의 거리가 얼마인지를 저장해두기위해 1이 아니라 visited[t] + 1로 저장함.
                visited[w] = visited[t] + 1
    # print(visited)


# 입력 받기
V, E = map(int, input().split()) # **1번**부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
# 인접리스트 -------------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]   # 정점을 두 개씩 입력받아오기
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우
# 여기까지 인접리스트 -----------------

# 함수 호출
bfs(1, 7)
