# 제대로 된 괄호로 구성되어 있는 지 확인하는 함수
def check_match(expression):
    # 괄호검사 => 스택을 사용한다.
    # 왜 사용한다? 닫힌 괄호가 나왔을 때, 제일 마지막에 나온 열린 괄호와 비교해야 한다.
    # 이 마지막에 들어간 데이터를 관리하기에는 "스택" 자료구조가 적합하기 때문이다.
    stack = []  # 스택을 빈 리스트로 초기화

    # 괄호 검사를 해야하니까, 괄호 데이터를 관리를 해야해요.
    # (, {, [ , ), }, ]
    # 얘네들이 서로 짝이 맞는지도 확인해야 해요. ')' => '(', '}' => '{', ']' => '['
    # 위처럼 서로 매칭되는 지 검사하기 좋은 데이터타입 뭐가 있을까요 ?
    matching_dict = {')': '(', '}': '{', ']': '['}

    # expression 변수에는 확인하고 싶은 문자열 => 순회하면서 이제 괄호를 만나면 로직을 수행
    for char in expression:
        # 열린 괄호를 만나면 => 스택에 집어넣어야 한다.
        # 검사하는 char 가 열린 괄호인지는 어떻게 알까요 ? values 를 이용해서 열린 괄호 리스트를 가져온다.
        if char in matching_dict.values():
            stack.append(char)
        # 닫힌 괄호를 만나면 ??
        # 닫힌 괄호인지는 어떻게 확인할까요?  keys를 이용해서 닫힌 괄호 리스트를 가져와서 포함관계를 본다.
        elif char in matching_dict.keys():
            # 스택에서 가장 마지막에 들어간 데이터를 꺼내서, 같은 타입의 괄호인지를 검사한다.
            # 근데 스택에서 꺼내기전에 해야할게 있어요.. 뭘까요 ?? 스택에 데이터가 있는지를 검사를 해야해요.
            if len(stack) == 0 :  # 스택이 비어있다면
            # if not stack:
                return False  # 괄호가 맞지 않아서 False 반환

            # 스택에 괄호가 들어있다 => 꺼내서 짝이 맞는 지를 확인한다.
            # 스택에 가장 마지막 원소의 열린 괄호와 닫힌 괄호의 짝 열린 괄호가 다르면 False
            # 검사를 하고, 뺀다.
            if stack[-1] != matching_dict[char]:
                return False
            stack.pop()

            # 뺀 값을 그대로 검사에 이용한다.
            # if stack.pop() != matching_dict[char]:
            #     return False

        # 괄호 검사를 모두 끝낸 다음에... 스택에 괄호가 남아있으면 그것조차 짝이 없는 것이므로
        return not stack  # 스택이 남아있지 않으면 True, 남아있으면 False


examples = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)"]
for ex in examples:
    if check_match(ex): 
        print(f"{ex} 는 올바른 괄호") 
    else:
        print(f"{ex} 는 올바르지 않은 괄호")  
