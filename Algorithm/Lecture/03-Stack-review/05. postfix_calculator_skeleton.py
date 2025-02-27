# 후위 표기식 계산 함수 
def run_calculator(expr):
    stack = []  # 피연산자를 저장할 스택
    tokens = expr.split()  # 후위 표기식을 공백으로 구분하여 토큰으로 분리

    # 주어진 토큰을 하나씩 접근한다.
    for token in tokens:
        # 1. 피연산자(숫자) => 스택에 삽입
        if token.isnumeric():  # 토큰이 숫자인 경우
            # token 계산할거잖아요. => 문자열을 숫자로 바꿔서 저장을 해주자.
            stack.append(int(token))

        # 2. 연산자를 만나면, 스택에서 2개 뽑아서 계산하고, 다시 집어넣기
        # for loop 끝나면, 마지막 스택에 들어있는 값 꺼내서 출력
        else:  # 연산자를 만난 경우
            # 빨리 들어간 애가 앞에 있어야 한다.
            val1 = stack.pop()  # 먼저 꺼낸 애 (늦게 들어간 애)
            val2 = stack.pop()  # 2번째로 꺼낸 애 (빨리 들어간 애)
            # 주어진 token(연산자) 와 뽑아낸 숫자 2개(val1, val2)를 사칙연산하는 코드를 작성해야한다.
            # +, -, *, / => if문으로 나눠서 구현을 하면 된다.
            result = None
            if token == '+':
                result = val2 + val1
            elif token == '-':
                result = val2 - val1
            elif token == '*':
                result = val2 * val1
            elif token == '/':
                result = val2 / val1
            # 계산한 결과는 스택에 집어넣는다.
            stack.append(result)

    return stack.pop()

# 예시
postfix_expression = "3 2 5 * + 8 4 / -"
result = run_calculator(postfix_expression)
print(result)
