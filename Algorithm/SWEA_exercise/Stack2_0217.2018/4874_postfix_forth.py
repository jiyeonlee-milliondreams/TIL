import sys
sys.stdin = open('4874_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(str, input().split()))   # 후위표기식 입력
    N = len(arr)

    stack = [0] * 256
    top = -1

    icp = {'.': 0, '+': 1, '-': 1, '*': 2, '/': 2 }

    for i in range(N):    # 표기식을 순회하며
        if arr[i] not in '+-*/.':      # 피연산자라면 push
            top += 1
            stack[top] = int(arr[i])

        elif arr[i] != '.':   # 연산자라면
            # # 다음 문자열이 연산자이고 우선순위가 높다면 error >>> 아님!!!
            # if 0 <= i+1 < N and arr[i+1] in '+-*/' and icp[arr[i]] < icp[arr[i+1]]:
            #     result = 'error'
            #     break

            if top < 1:    # 계산할 숫자가 2개 이상이 아니라면 error
                result = 'error'
                break


            else:
                top -= 1
                operand2 = stack[top + 1]
                top -= 1
                operand1 = stack[top + 1]

                if arr[i] == '+':   # 연산자가 '+'라면 덧셈
                    top += 1
                    stack[top] = operand1 + operand2

                elif arr[i] == '-':   # 연산자가 '-'라면 뺄셈
                    top += 1
                    stack[top] = operand1 - operand2

                elif arr[i] == '*':   # 연산자가 '*'라면 곱셈
                    top += 1
                    stack[top] = operand1 * operand2

                elif arr[i] == '/':   # 연산자가 '/'라면 나눗셈
                    top += 1
                    stack[top] = operand1 // operand2   # "나눗셈의 경우 항상 나누어 떨어진다."이므로 몫으로 연산해야 함.

        else:       # '.'인 경우
            if top == 0:    # 정상적으로 연산이 된 경우
                top -= 1
                result = stack[top + 1]
                break
            else:   # 정상적으로 연산이 되지 않은 경우
                result = 'error'
                break

    print(f'#{test_case}', result)



'''
T = int(input())
for test_case in range(1, T+1):
    arr = list(map(str, input().split()))   # 후위표기식 입력

    stack = [0] * 256
    top = -1

    result = 0

    for char in arr:    # 표기식을 순회하며
        if char not in '+-*/.':      # 피연산자라면 push
            top += 1
            stack[top] = int(char)

        elif char != '.':   # 연산자라면
            if top <= 0:    # 계산할 숫자가 2개 이상이 아니라면
                result = 'error'
                break

            else:
                if char == '+':   # 연산자가 '+'라면 덧셈
                    top -= 1
                    operand2 = stack[top+1]
                    top -= 1
                    operand1 = stack[top+1]
                    top += 1
                    stack[top] = operand1 + operand2

                elif char == '-':   # 연산자가 '-'라면 뺄셈
                    top -= 1
                    operand2 = stack[top+1]
                    top -= 1
                    operand1 = stack[top+1]
                    top += 1
                    stack[top] = operand1 - operand2

                elif char == '*':   # 연산자가 '*'라면 곱셈
                    top -= 1
                    operand2 = stack[top+1]
                    top -= 1
                    operand1 = stack[top+1]
                    top += 1
                    stack[top] = operand1 * operand2

                elif char == '/':   # 연산자가 '/'라면 나눗셈
                    top -= 1
                    operand2 = stack[top+1]
                    top -= 1
                    operand1 = stack[top+1]
                    top += 1
                    stack[top] = operand1 / operand2

        else:       # '.'이라면
            top += 1
            stack[top] = char

    if stack[1] == '.':     # 정상적으로 연산된 경우
        print(f'#{test_case}', stack[0])

    else:   # 정상적으로 연산되지 않은 경우
        print(f'#{test_case}', 'error')
'''

