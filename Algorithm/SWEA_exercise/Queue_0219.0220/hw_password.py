import sys
sys.stdin = open('hw_password_input.txt', 'r')

T = 10
for _ in range(1, T+1):
    test_case = int(input())

    numbers = list(map(int, input().split()))   # 숫자 입력받기
    variable = 1    # 1, 2, 3, 4, 5가 반복되어서 뺄셈.
    password = []
    # idx = 0     # 인덱스 번호 0, 1, 2, ... 7이 반복되도록 % 활용

    # 무한 루프를 돌면서
    while True:

        temp = numbers.pop(0) - variable        # numbers의 첫 원소에서 variable을 뺀다.
        if temp <= 0:
            temp = 0

        variable += 1
        if variable == 6:        # variable 6이라면 다시 1로 초기화
            variable = 1
        
        # 뺄셈이 완료되면 해당 값을 numbers 마지막에 append()
        numbers.append(temp)

        # 뺄셈이 완료된 값이 0과 같거나 작을 경우 암호 저장 후 while 종료.
        if temp == 0:
            for number in numbers:  # 숫자열을 순회하며
                password.append(number)
            break

    print(f'#{test_case}', ' '.join(map(str,password)))

