def b(x_value):  # x_value 는 새로 생성된 객체
    x_value += 1
    print("x_value: ", x_value)


def a():
    x = 3
    b(x)
    print('x: ', x)  # 3 이 그대로 나온다.

a()