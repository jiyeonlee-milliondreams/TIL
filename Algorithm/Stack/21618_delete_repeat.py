import sys
sys.stdin = open('21618_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    txt = input()
    top = -1
    stack = [0] * 1000  # 문자열의 최대 개수 1000개
    result = 0  # 중복 제거된 글자의 수

    for char in txt:
        if top == -1:   # txt의 첫 문자는 우선 stack에 저장해야 하므로, if-else 구문 활용
            top += 1
            stack[top] = char
        else:
            # 중복을 제거하기 위해우선 현재 stack[top]에 저장된 값과 char가 일치하는지 확인
            if stack[top] == char:  # 일치하면 stack에서 문자 삭제
                top -= 1
                stack[top + 1] = 0
            else:   # 일치하지 않으면 stack에 문자 추가
                top += 1
                stack[top] = char

    for stack_indent in stack:  # stack을 순회하며 문자가 있는 경우 1 증가.
        if stack_indent == 0:   # 0이 나오면 반복 중지
            break   # for stack_indent
        else:
            result += 1

    print(f'#{test_case}', result)
