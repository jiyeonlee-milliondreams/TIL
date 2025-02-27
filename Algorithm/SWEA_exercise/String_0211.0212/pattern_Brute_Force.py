def pattern_count(p, t):    # 패턴의 횟수 리턴
    N = len(t)
    M = len(p)
    i = j = 0
    cnt = 0
    while i < N:  # j가 M을 벗어나더라도 i가 끝날때까지 반복
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i-j 비교를 시작했던 위치
            j = 0
        else:  # 같으면
            i += 1
            j += 1
        if j == M:  # 패턴을 찾은 경우
            cnt += 1
            i = i - j + 1
            j = 0
    return cnt

t = 'TTTTTATTAATA'
p = 'TTA'
print(pattern_count(p, t))

"""
패턴이 txt에 존재하는지 여부 리턴
def bruteforce(p, t):
    N = len(t)
    M = len(p)
    i = j = 0
    while i < N and j < M:  # i와 j가 N과 M 안에 있으면 반복
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i-j 비교를 시작했던 위치
            j = 0
        else:  # 같으면
            i += 1
            j += 1
    if j == M:  # 패턴 마지막까지 같아서 j가 1이 더 커져서 M이 되면
        return i - j  # 비교를 시작했던 위치 즉, 패턴의 시작 인덱스
    else:
        return -1  # 패턴을 못찾은 경우이므로 -1 출력


t = 'TTTTTATTAATA'
p = 'TTA'
print(bruteforce(p, t))
"""

"""
손코딩
t = 'TTTTTATTAATA'
p = 'TTA'
N = len(t)
M = len(p)
i = j = 0
while i < N and j < M:   # i와 j가 N과 M 안에 있으면 반복
    if t[i] != p[j]:    # 다르면
        i = i-j+1       # i-j 비교를 시작했던 위치
        j =0
    else:   # 같으면
        i += 1
        j += 1
if j == M:   # 패턴 마지막까지 같아서 j가 1이 더 커져서 M이 되면
    print(i-j)  # 비교를 시작했던 위치 즉, 패턴의 시작 인덱스
else:
    print(-1)   # 패턴을 못찾은 경우이므로 -1 출력
"""
