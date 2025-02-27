def power(x, n):
    # 종료조건
    # x의 값과 상관없이 n 이 0이면, 무조건 1을 반환한다.
    if n == 0:
        return 1

    return x * power(x, n-1)

print(power(2, 10))
print(power(3, 3))
