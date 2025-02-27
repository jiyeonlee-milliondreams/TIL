import sys
sys.stdin = open('4866_bracket_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    txt = input()
    top = -1
    stack = [0] * 100
    success = True

    for char in txt:
        if char in '({':    # 여는 괄호'({' 중에 하나라면 stack에 해당 char 추가.
            top += 1
            stack[top] = char
        elif char in ')}':  # 닫는 괄호 ')}' 중에 하나라면 stack 삭제.
            if top == -1:   # 닫는 괄호가 남아있는데, 여는 괄호가 없다면 False
                success = False
                break   # for char
            elif top > -1:
                if char == ')':     # char가 ')'라면 현재 top이 '('이면 삭제. 아니면 False.
                    if stack[top] == '(':
                        top -= 1
                        stack[top + 1] = 0
                    else:
                        success = False
                        break  # for char
                elif char == '}':   # char가 '}'라면 현재 top이 '{'이면 삭제. 아니면 False.
                    if stack[top] == '{':
                        top -= 1
                        stack[top + 1] = 0
                    else:
                        success = False
                        break  # for char

    if top != -1:   # for 문을 다 돌았는데 top이 -1이 아니라면 False
        success = False

    if success:
        print(f'#{test_case}', 1)
    else:
        print(f'#{test_case}', 0)
