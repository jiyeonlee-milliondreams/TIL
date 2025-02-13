# 준비작업(1차원 배열 만들기)
top = -1
stack = [0] * 10

# 삽입(push)
top += 1
stack[top] = 1

top += 1
stack[top] = 2

top += 1
stack[top] = 3

# 삭제(pop)
'''
삭제를 함수로 정의할 때, 
return stack[top]을 하고나서
top -= 1을 하면, 
함수에서 return 이후는 실행되지 않으므로, 순서를 아래와 같이!
'''
top -= 1
print(stack[top + 1])

top -= 1
print(stack[top + 1])

top -= 1
print(stack[top + 1])