# 중위 표기식을 후위 표기식으로 변환하는 함수
def infix_to_postfix(expression):
    # 연산자의 우선순위를 정의
    op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []  # 연산자를 저장할 스택
    postfix = []  # 후위 표기식을 저장할 리스트

    for ch in expression:
        if ch.isnumeric():  # 숫자인 경우
            postfix.append(ch)  # 후위 표기식에 추가
        elif ch == '(':  # 여는 괄호인 경우
            stack.append(ch)  # 스택에 추가
        elif ch == ')':  # 닫는 괄호인 경우
            top_token = stack.pop()  # 스택에서 연산자를 꺼냄
            while top_token != '(':  # 여는 괄호를 만날 때까지
                postfix.append(top_token)  # 후위 표기식에 추가
                top_token = stack.pop()
        else:  # 연산자인 경우
            # 스택에 들어 있는 연산자가 지금 검사하는 연산자보다 우선순위가 더 높은 경우
            # 높은 친구들을 모두 거내서 후위 표기식에 추가하고, 검사하는 연산자를 스택에 추가
            while stack and op_dict[stack[-1]] >= op_dict[ch]:
                postfix.append(stack.pop())
            stack.append(ch)

    while stack:  # 스택에 남아 있는 모든 연산자를 후위 표기식에 추가
        postfix.append(stack.pop())
    
    return ' '.join(postfix)  # 리스트를 문자열로 변환하여 반환

# 후위 표기식 계산 함수 
def run_calculator(expr):
    stack = []  # 피연산자를 저장할 스택
    tokens = expr.split()  # 후위 표기식을 공백으로 구분하여 토큰으로 분리

    for token in tokens:
        if token.isnumeric():  # 숫자인 경우
            stack.append(int(token))  # 스택에 추가
        else:  # 연산자인 경우
            op2 = stack.pop()  # 스택에서 두 번째 피연산자를 꺼냄
            op1 = stack.pop()  # 스택에서 첫 번째 피연산자를 꺼냄
            if token == '+':
                result = op1 + op2
            elif token == '-':
                result = op1 - op2
            elif token == '*':
                result = op1 * op2
            elif token == '/':
                result = op1 / op2
            stack.append(result)  # 계산 결과를 스택에 추가

    return stack.pop()  # 최종 결과를 반환

# 예시
infix_expression = "3+(2*5)-8/4"
postfix_expression = infix_to_postfix(infix_expression)
print(f"후위 표기식: {postfix_expression}")

result = run_calculator(postfix_expression)
print(result)
