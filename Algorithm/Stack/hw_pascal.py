T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    # 구현해야 하는 스택의 개수 구하기기
    stack_length = 0
    for i in range(1, N+1):
        stack_length += i
    
    stack = [0] * stack_length
    top = -1
    

print(stack)