# 중위 표기식을 후위 표기식으로 변환하는 함수
def infix_to_postfix(expression):
    # 연산자의 우선순위
    # 우선순위를 비교를 해야하는데, 값을 이용해서 비교를 할거다..
    op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

    stack = []  # 연산자를 저장할 스택
    postfix = []  # 후위 표기식을 저장할 리스트

    # 주어진 중위 표기식을 하나씩 순회
    for ch in expression:
        # 해당 값이 숫자인지 확인하는 함수
        # 1. 피연산자라면 결과로 출력
        if ch.isnumeric():
            postfix.append(ch)  

        # 2. 값이 열린괄호 => 무조건 스택에 삽입을 한다.
        elif ch == '(':  
            stack.append(ch)  

        # 3. 닫힌 괄호면 => 열린괄호를 만날 때까지 스택에서 꺼내서 결과에 추가한다.
        # 열린괄호와 닫힌괄호는 스택에 넣지 않는다.
        elif ch == ')':  
            top_token = stack.pop()  # 스택에 있는 친구를 하나 꺼내요
            while top_token != '(':  # 그 친구가 열린 괄호가 아니라면
                postfix.append(top_token)  # 꺼낸 친구를 결과에 추가하고
                top_token = stack.pop()  # 다시 또 새로운 친구를 꺼낸다.
        # 연산자 ( *, /, +, - )
        else:
            # 우선순위를 비교해서 스택에 집어넣거나, 스택에서 뺀 다음에 집어넣는 과정을 진행한다.
            # 일단 스택에서 비교를 하려면 스택에 무언가 있어야하니까.
            while stack and op_dict[stack[-1]] >= op_dict[ch]:
                postfix.append(stack.pop())
            # 우선순위 순으로 모두 빼냈다면 본인이 들어간다.
            stack.append(ch)
    # 모든 순회가 끝났는데, 스택에 연산자가 남아있으면 모두 꺼내서 결과에 추가해준다.
    while stack:  
        postfix.append(stack.pop())

    # 리스트를 문자열로 변환하여 반환
    # [1, 2, '*', 3, 4, '/']
    # join => 리스트를 문자열로 바꿔준다.
    # 1 2 * 3 4
    # ''.join(postfix) => 12*34
    # '123'.join(postfix) => 11232123*12331234123
    return ' '.join(postfix)

infix_expression = "3+(2*5)-8/4"
postfix_expression = infix_to_postfix(infix_expression)
print(f"후위 표기식: {postfix_expression}")
