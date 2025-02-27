import sys
sys.stdin = open('bracket_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):

    txt = input()
    top = -1    # top의 초기값은 -1으로 설정
    stack = [0] * 100
    # 문제에 txt의 최대 길이가 명시되어있지 않으나, 교안상 100개 정도 stack 생성을 추천.
    success = True

    for bracket in txt:
        if bracket == '(':  # 여는 괄호가 있으면 stack에 추가.
            top += 1
            stack[top] = bracket
        elif bracket == ')':  # 닫는 괄호가 있으면 stack에서 '(' 삭제.
            if top == -1:    # 닫는 괄호가 있는데 top이 -1이면 짝이 맞지 않으므로 False
                success = False
            elif top > -1:  # 닫는 괄호가 있고 top이 0 이상이면 stack에서 '(' 삭제
                top -= 1
                stack[top + 1] = 0
    if top != -1:   # stack에 '('가 남아있으면 짝이 맞지 않으므로 False
        success = False

    if success:
        print(f'#{test_case}', 1)
    else:
        print(f'#{test_case}', -1)
