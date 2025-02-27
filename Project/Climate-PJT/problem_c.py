# HTTP 요청을 보낼 수 있도록 도와주는 requests 라이브러리 import
import requests
import pprint

# git push를 위해서 .env 파일에 정의한 API_KEY를 불러오기 위해 dotenv 라이브러리 import
import os
from dotenv import load_dotenv

load_dotenv()

# lat과 lon은 필수 변수이므로 현재 위치인 서울의 위도와 경도 할당. 
lat = 37.56
lon = 126.97

# 사용자의 API_KEY 할당. 상수이므로 변수명은 대문자 처리.
API_key = os.environ.get('API_KEY')

# 날씨 정보를 제공해주는 API의 URL
URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

# requests.get(url)을 통해 API에 요청을 보냄
# 서버로부터 응답(Response)을 JSON 형태로 변환
data = requests.get(URL).json()

# main과 weather의 데이터를 추출하는 함수 정의
def main_and_weather():
    global data # data가 global에 정의되어있으므로, 함수에서 활용하기 위해 전역 변수로 선언
    return data["main"], data["weather"]

# 인덱스를 활용하기 위해 리스트로 형변환
result = list(main_and_weather())

# 수시로 결과를 확인하기위해 pprint 활용
# print.pprint(result)

# 한글 key에 result로부터 인덱스를 활용하여 value를 불러와서 key-value 형태로 딕셔너리 정의
korean_dic_result = {
    '기본' : {
        '체감온도' : result[0]['feels_like'],
        '지표면수준' : result[0]['grnd_level'],
        '습도' : result[0]['humidity'],
        '기압' : result[0]['pressure'],
        '해수면수준' : result[0]['sea_level'],
        '온도' : result[0]['temp'],
        '최고온도' : result[0]['temp_max'],
        '최저온도' : result[0]['temp_min']
        },
    ' 날씨' : {
        '요약' : result[1][0]['description'],
        '아이콘' : result[1][0]['icon'],
        '식별자' : result[1][0]['id'],
        '핵심' : result[1][0]['main']
    }
}

pprint.pprint(korean_dic_result)
