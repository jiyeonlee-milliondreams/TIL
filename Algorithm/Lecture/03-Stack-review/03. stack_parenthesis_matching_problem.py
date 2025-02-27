def check_match(expression):
    stack = []  # 스택을 빈 리스트로 초기화
    # 괄호 짝을 맞추기 위한 사전
    matching_dict = {')': '(', '}': '{', ']': '['}
    
    # 문자열의 각 문자를 순회하면서, 괄호의 종류에 따라 push, pop을 진행 
    for char in expression:  
        # 현재 내가 검사하는 괄호가 열린 괄호라면, 스택에 추가 
        if char in matching_dict.values():
            stack.append(char)  # 스택에 추가
        # 현재 내가 검사하는 괄호가 닫힌 괄호라면,
        elif char in matching_dict.keys():
            # 스택이 비어있으면 False
            if not stack:
                return False 
            # 스택에 들어있는 마지막 값과 닫힌 괄호가 짝이 맞지 않으면 
            # 괄호가 맞지 않으므로 False
            if stack[-1] != matching_dict[char]:
                return False
            
            # 짝이 맞으므로 스택에서 가장 위의 아이템 제거
            stack.pop()  
    
    # 모든 문자를 순회한 후 스택이 비어 있으면 True 반환, 그렇지 않으면 False 반환
    return not stack  

examples = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)"]
for ex in examples:
    if check_match(ex): 
        print(f"{ex} 는 올바른 괄호") 
    else:
        print(f"{ex} 는 올바르지 않은 괄호")  
