def practice_recursive2(x):  # 독립적이 객체
    x += 1
    print(f"in function2 {x}")  # in function2 5


def practice_recursive1(x, a):
    x += 1
    a.append(5)
    print(f"in function1 {x}")  # in function1 4
    practice_recursive2(x)
    print(f"out function1 {x}")  # recursive2 함수가 끝나면, 여기서부터 이어서 시작되는 거에요.


def main():
    x = 3
    a = [1,2,3,4]
    print(f"before {x}")  # before 3
    practice_recursive1(x, a)
    print(f"after {x}")
    print(a)

main()