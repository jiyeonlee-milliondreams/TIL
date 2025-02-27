import sys
sys.stdin = open('ex1_postfix0_input.txt', 'r')

T= int(input())
for test_case in range(1, T+1):

    arr = input()

    # 스택 초기화
    stack = [0] * len(arr)
    top = - 1
    postfix = ''
    icp = {'+': 1, '-': 1, '*': 2, '/': 2}

    for char in arr:    # 문자열을 순회하며
        if char not in '+_*/':  # 피연산자인 경우
            postfix += char   # 후위 표기식에 추가
        else:
            # 스택에 연산자가 남아있고 넣으려는 연산자보다 작아질때까지 pop 한 뒤 push
            while top > -1 and icp[stack[top]] >= icp[char]:
                top -= 1
                postfix += stack[top + 1]
            top += 1
            stack[top] = char

    # 스택에 남아있는 연산자 모두 pop
    while top > -1:
        top -= 1
        postfix += stack[top + 1]

    print(f'#{test_case}', postfix)


'''
    # append, pop으로 구현하기
    stack = []

    for i in range(N):
        if infix[i] not in '+*': # 피연산자(숫자)인 경우
            postfix += infix[i]     # 후위연산식에 사용
        else:   # 연산자인 경우
            # 스택에 남아있는 top원소의 우선순위가 높거나 같으면
            while stack and icp[stack[-1]] >= icp[infix[i]]:    # 왜 -1이지?
                postfix += stack.pop()
            # 연산자 push
            stack.append(infix[i])
    # 스택에 남은 연산자 꺼내기
    while stack:
        postfix += stack.pop()
'''

