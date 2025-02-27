import sys
sys.stdin = open('4871_input.txt', 'r')


def dfs(S, E, V):  # 출발 정점, 도착 정점, 정점의 수

    visited = [0] * (V + 1)     # 정점의 수 + 1 해서 노드와 번호 맞춰주기
    stack = []

    while True:     # 종료조건 대신 break를 사용할 때, 무한 루프 활용.
        # 방문하지 않았다면 방문 처리
        if visited[S] == 0:
            visited[S] = 1

        if S == E:
            return 1
            break   # while True

        # 기준점 S의 인접 정점을 순회하며
        for adj in adj_list[S]:
            # 방문하지 않았다면
            if visited[adj] == 0:
                # stack에 추가, 방문 처리 후 이동
                stack.append(adj)
                S = adj
        else:   # 모두 방문했다면
            if stack:   # 스택에 있는 직전 방문지로 이동
                S = stack.pop()
            else:   # 모두 방문했는데, 직전 방문지도 없다면 경로가 없으므로 break
                return 0
                break


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())    # 정점의 수 V 간선의 수 E
    graph = [list(map(int, input().split())) for _ in range(E)]
    S, E = map(int, input().split())    # 출발 노드 S 도착 노드 E

    adj_list = [[] for _ in range(V+1)]     # 인접 리스트 생성     정점의 수 +1로 해서 인덱스 맞춰주기

    for adj in graph:   # 입력받은 간선을 순회하면서
        v, w = adj[0], adj[1]
        adj_list[v].append(w)

    result = dfs(S, E, V)
    print(f'#{test_case}', result)
