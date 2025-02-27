# 아래 클래스를 수정하시오.
class UserInfo:
    '''
    1. get_user_info() 메서드 정의
        (1) 이름과 나이를 사용자로부터 입력받는다.
            - 이름은 input()의 data type이 str이므로, input()으로 받아 input_user_name에 할당하고
            - 나이는 정수이므로, int()로 형변환하여 input_user_age에 할당한다.
        (2) 사용자가 잘못된 형식으로 입력해 예외가 발생했을 경우, except로 예외처리를 한다.
        (3) 예외가 발생하지 않을 경우, else로 추가 코드를 작성한다.
            - 클래스에 정의된 딕셔너리 self.user_data에 key-value 쌍을 추가한다.
    2. display_user_info 메서드 정의
        (1) 사용자가 올바른 형식으로 정보를 입력한 경우, if문을 활용하여 이를 출력한다.
            - 올바른 형식으로 정보를 입력한 경우는
            딕셔너리의 길이를 len으로 재서 추가된 key-value 쌍이 있어 딕셔너리 길이가 0이 아닌 경우이므로,
            이때 사용자 정보를 출력한다.
            - f-string에서 [대괄호]를 쓸 수 없으니, print문을 여러번 활용한다. 
        (2) 사용자가 정보를 입력하지 않은 경우를 else로 포괄하여 안내문을 출력한다.
    '''
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        try:
            input_user_name = input('이름을 입력하세요: ')
            input_user_age = int(input('나이를 입력하세요: '))
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')
        else:
            self.user_data['이름'] = input_user_name
            self.user_data['나이'] = input_user_age

    def display_user_info(self):
        if len(self.user_data) != 0:
            print('사용자 정보:')
            print('이름:', self.user_data['이름'])
            print('나이:', self.user_data['나이'])
        else:            
            print('사용자 정보가 입력되지 않았습니다.')


user = UserInfo()
user.get_user_info()
user.display_user_info()

'''
* 시행착오 일지
딕셔너리에 len()함수가 작동하는지 확인해보았다.
# my_dict_2 = {}
# print(len(my_dict_2))
'''

'''
* 시행착오 일지
예외 상황을 내장 오류 클래스가 아닌 직접 정의하고 싶어 아직 관련내용을 배우지 않았지만, 
아래와 같이 시도해보았다. 실행결과 문법 오류가 뜨지는 않았지만 그렇다고 의도한 결과가 구현되지도 않았다.
이에 여기에 남겨둔다.
        # except:
        #     if type(input_user_name) != str:
        #         print('이름은 한글 또는 영어로 입력해야 합니다.')
        #         print('사용자 정보가 입력되지 않았습니다.')
        #     elif type(input_user_age) != int:
        #         print('나이는 숫자로 입력해야 합니다.')
        #         print('사용자 정보가 입력되지 않았습니다.')

'''
