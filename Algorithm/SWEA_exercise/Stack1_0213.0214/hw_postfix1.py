import sys
sys.stdin = open('hw_postfix1_input.txt', 'r')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = input()

    stack = []      # append() pop()의 방식으로 구현
    postfix = ''    # 후위 표기식을 저장할 변수 생성

    # 후위 표기식으로 변환
    for char in arr:    # 문자열 계산식을 순회하며
        if char not in '+':     # 피연산자인 경우
            postfix += char

        else:   # 연산자인 경우
            while stack:
                postfix += stack.pop()
            stack.append(char)
            '''
            if stack:
                postfix += stack.pop()
            else:
                stack.append(char)
            '''
    while stack:    # 스택에 남은 연산자 꺼내기
        postfix += stack.pop()

    # 계산
    result = []
    char1 = ''
    char2 = ''
    for char in postfix:    # 후위 표기식을 순회하며
        if char not in '+':     # 피연산자인 경우
            result.append(char)
        else:   # 연산자인 경우
            char2 = int(result.pop())
            char1 = int(result.pop())
            result.append(char1 + char2)

    print(f'#{test_case}', result.pop())
    # print(f'{test_case}', ''.join(result))




