# 아래 클래스를 수정하시오.
class StringRepeater:

    def __init__(self):
        pass

    def repeat_string(self, times, string):
        return f'{string}\n' * times


repeater1 = StringRepeater()
print(repeater1.repeat_string(3, "Hello"))


'''
시행착오 일지
(1) 문자열이 한 번 밖에 출력되지 않으므로 오류.
def repeat_string(self, times, string):
    for i in range(times):
        return string

(2) print()를 활용하면 줄바꿈은 가능하지만, return 값이 없어서 요구사항과 맞지 않음.
n = 10
m = 'H'

def a(n, m):
    for i in range(n):
        print(m)


print(a(n, m))

(3) 문자열 자체에 줄바꿈을 포함시켜서 [문제] 요구사항에 맞게 수정함.
def repeat_string(self, times, string):
    return f'{string}\n' * times
'''
