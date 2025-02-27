t = 'TTTTTATTAATA'
p = 'TTA'


def search(p, t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):  # t에서 p를 비교할 첫 위치 인덱스
        for j in range(M):  # t와 비교할 p의 인덱스
            if t[i+j] != p[j]:
                break
        else:   # break에 걸리지 않고 for가 끝난 경우, else를 실행.
            return i    # 패턴이 처음 나타난 인덱스 리턴.
            # 개수를 세고 싶으면 여기서 return하지 말고 cnt += 1
    return -1   # t에 p가 없는 경우
    # 여기서 return cnt 하면 됨.


print(search(p, t))

# if t[i:i+M] == p:
