# 재귀 함수의 형태로 부분집합 구현
# ""if bit[i]:""   ==   ""if bit[i] == 1:""

# 원소의 포함 여부를 결정한 후, 해당 단계에서의 원소의 합을 구해놓는 것.
def f(i, N, s):
    if i == N:
        print(bit, s)
    else:
        bit[i] = 1
        f(i+1, N, s+A[i])
        bit[i] = 0
        f(1+i, N, s)

A = [1, 2, 3]
bit = [0] * len(A)
cnt = 0
f()
