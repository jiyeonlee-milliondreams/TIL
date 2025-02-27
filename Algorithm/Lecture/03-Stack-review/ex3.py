'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v, N):            # v출발, N마지막 정점
    # visited와 stack은 문제에 따라 함수 외부에서도 정의 가능.
    # visited N + 1로 해서 정점 번호와 맞춰주기.
    visited = [0] * (N + 1)     # 방문표시 0(False)으로 초기화. 방문 후 1(True) 입력. 방문 여부 확인시 인덱스로 접근.
    stack = []                  # 스택

    while True:
        if visited[v] == 0: # 첫 방문이면
            visited[v] = 1
            print(v)
        for w in adj_list[v]:   # v에 인접하고 방문안한 w가 있으면(방문 여부를 먼저 확인 하고)
            if visited[w] == 0: # 인접한 리스트에서 하나씩 꺼내서 확인하고 방문 안 했으면 바로 이동하고 반복 종료
                stack.append(v)   # 현재 정점 push
                v = w               # w로 이동
                break       # for w
        else:                       # 더이상 갈 곳이 없는 경우(스택의 pop을 진행함.)
            if stack:                   # 스택이 비어있지 않으면 pop  # if top > -1:(top을 활용할 경우)
                v = stack.pop()
            else:                   # 스택이 비어있으면
                break       # for while

# input 받는 법
V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]         # 인접 리스트
for i in range(E):
    v, w = graph[i*2], graph[i*2+1]     # 간선 수만큼 반복, 인덱스를 2개씩 건너뛰면서 읽기

    adj_list[v].append(w)
    adj_list[w].append(v)                 # 방향이 없는 경우(인접한 정점 간 탐색 순서 무방한 경우)

dfs(1, V)                           # 1번부터 탐색
