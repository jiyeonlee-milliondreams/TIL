'''패키지에서 모듈 호출하기'''
from conf import settings
from utils import create_url

'''creat_url 함수에 인자를 할당하여 결과 출력하기'''
result = create_url.create_url(settings.NAME, settings.MAIN_URL)
print(result)
