# HTTP 요청을 보낼 수 있도록 도와주는 requests 라이브러리 import
import requests

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

# 받은 응답 데이터 중 Key 값 출력
print(data.keys())
