import sys
sys.stdin = open('21649_input.txt', 'r')

def dfs(start, N):  # 출발, 마지막 정점

    visited = [0] * (N + 1)  # 미방문 0, 방문 1
    stack = []
    result = []

    while True:     # while True는 처음 써보는 구문
        if visited[start] == 0:
            visited[start] = 1
            result.append(f'{start}')   # f-string으로 변수를 리스트에 append 가능

        for w in adj_list[start]:
            if visited[w] == 0:
                stack.append(start)
                start = w
                break
        else:
            if stack:   # 스택이 비어있지 않으면 pop
                start = stack.pop()
            else:   # 스택이 비어있으면
                break
    return result

test_case = 1
V, E = map(int, input().split())    # 정점의 수 V, 간선의 수 E
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]     # 인접 리스트 V + 1만큼 생성

for i in range(E):  # 간선 수만큼 반복하면서 인덱스를 2개씩 건너뛰면서 읽기
    v, w = graph[i*2], graph[i*2+1]
    adj_list[v].append(w)
    adj_list[w].append(v)   # 방향이 없는 경우(인접한 정점 간 탐색 순서 무방한 경우)

result = dfs(1, V)  # 함수 호출 반환 값은 변수에 할당해서 받기
print(f'#{test_case}', '-'.join(result))
