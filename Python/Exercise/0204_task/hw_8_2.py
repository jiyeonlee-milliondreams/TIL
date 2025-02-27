# 아래 함수를 수정하시오.
def check_number():
    '''
    1. try-except 구조를 활용해 예외처리를 한다.
        (1) try에서는 예외가 발생할 수 있는 코드를 작성하므로, 사용자로부터 숫자를 입력받는 코드를 작성한다.
        (2) except에서는 예외가 발생했을 때 처리할 코드를 작성하므로, 예상되는 에러를 내장 에러 클래스명으로 작성한다.
            - 이때, 예외가 상속 계층구조를 띄므로, 구체적인 'ValueError'부터 처리한 후, 범용 예외인 Eception을 처리하도록 작성한다.
    2. if 문을 활용하여 try의 동작을 구체화한다.
        (1) 입력받은 숫자(input_number)가 양수인 경우, '양수입니다.'를 출력한다.
        (2) 입력받은 숫자(input_number)가 0인 경우, '0입니다.'를 출력한다.
        (3) 입력받은 숫자(input_number)가 음수인 경우, '음수입니다.'를 출력한다.
            - 이때, elif input_number < 0: 를 활용해도 되지만, else: 를 활용해도 된다.
    '''
    try:
        input_number = int(input('숫자를 입력하세요 : '))
        if input_number > 0:
            print('양수입니다.')
        elif input_number == 0:
            print('0입니다.')
        elif input_number < 0:
            print('음수입니다.')
    except ValueError:
        print('잘못된 입력입니다.')
    except Exception:
        print('잘못된 입력입니다.')

check_number()
