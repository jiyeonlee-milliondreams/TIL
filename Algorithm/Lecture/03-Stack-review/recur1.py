def f(i, N):
    if i==N:    # 중단조건
        return
    else:  # 재귀호출
        f(i+1, N)

f(0, 3)
# f(0, 2000)
# 재귀를 너무 많이 호출한 경우 오류
# RecursionError: maximum recursion depth exceeded in comparison
