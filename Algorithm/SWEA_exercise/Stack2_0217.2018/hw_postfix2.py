import sys
sys.stdin = open('hw_postfix2_input.txt', 'r')

T = 10
for test_case in range(1, T+1):

    N = int(input())    # 문자열의 길이
    arr = input()   # 문자열 입력

    stack = [0] * N     # 문자열의 길이만큼 stack 만들어서 넉넉히 활용
    top = -1
    postfix = ''    # 후위 표기식을 저장할 변수 생성

    icp = {'*': 2, '+': 1}      # 연산자 우선순위

    # 후위 표기식으로 바꾸기
    for char in arr:    # 문자열을 순회하며

        if char not in '+*':    # 피연산자인 경우
            postfix += char     # 후위 표기식에 추가
        else:   # 연산자인 경우
            # 스택 top에 있는 연산자가 char의 연산자보다 낮을 때까지 pop해서 push
            while top > -1 and icp[stack[top]] >= icp[char]:
                top -= 1
                postfix += stack[top + 1]

            # 스택에 연산자가 없는 경우
            top += 1
            stack[top] = char

            '''
            # 시행착오
            if top > -1:   # 스택에 연산자가 있는 경우
                # 스택 top에 있는 연산자가 char의 연산자보다 낮을 때까지 pop해서 push
                while icp[stack[top]] >= icp[char]:
                    top -= 1
                    postfix += stack[top + 1]

            else:   # 스택에 연산자가 없는 경우
                top += 1
                stack[top] = char
            '''

    # 스택에 남아있는 연산자 pop
    while top > -1:
        top -= 1
        postfix += stack[top + 1]


    # 계산

    result = [0] * N    # 문자열의 길이만큼 스택 넉넉히 만들기

    for char in postfix:
        if char not in '+*':    # 피연산자인 경우
            top += 1
            result[top] = int(char)

        elif char == '+':   # 연산자 '+'인 경우 덧셈
            top -= 1
            operand2 = result[top + 1]   # 먼저 꺼낸 원소 오른쪽     피연산자 영어로 operand
            top -= 1
            operand1 = result[top + 1]      # 나중에 꺼낸 원소 왼쪽
            top += 1
            result[top] = operand1 + operand2

        elif char == '*':   # 연산자 '*'인 경우 곱셈
            top -= 1
            operand2 = result[top + 1]   # 먼저 꺼낸 원소 오른쪽
            top -= 1
            operand1 = result[top + 1]      # 나중에 꺼낸 원소 왼쪽
            top += 1
            result[top] = operand1 * operand2

    # 계산 결과는 stack[0]에 저장되므로 0번 인덱스 값 출력
    print(f'#{test_case}', result[0])


