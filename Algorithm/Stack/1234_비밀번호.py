import sys
sys.stdin = open('1234_input.txt', 'r')

T = 10
for test_case in range(1, T+1):
    N, numbers = list(map(str, input().split()))    # class <str>
    top = -1
    stack = [10] * int(N)  # stack에 입력할 숫자가 0부터 9이므로, 초기값 10으로 설정

    for number in numbers:  # 순열을 순회하면서
        if top == -1:   # 우선 첫 숫자는 stack에 추가해야 하므로, if-else 구문 활용
            top += 1
            stack[top] = number
        else:
            if stack[top] == number:    # 만약 현재 top의 숫자가 number와 같다면 삭제
                top -= 1
                stack[top + 1] = 10
            else:   # 같지 않으면 추가
                top += 1
                stack[top] = number

    password = ''   # password 이름의 빈 문자열 생성
    for key in stack:   # stack을 순회하며
        if key == 10:   # 10과 같으면 반복 중지
            break   # for key
        else:   # 10이 아닌 숫자라면 password에 추가
            password += key

    print(f'#{test_case}', password)
