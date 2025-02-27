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
URL = f'https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_key}'

# requests.get(url)을 통해 API에 요청을 보냄
# 서버로부터 응답(Response)을 JSON 형태로 변환
response = requests.get(URL)
data = response.json()

# 응답 데이터 확인
if response.status_code != 200:
    print(f"API 요청 실패! 상태 코드: {response.status_code}")
    print("응답 데이터:", data)
else:
    # 대기오염 데이터 추출
    air_quality = data["list"][0]["main"]["aqi"]  # AQI (Air Quality Index)
    components = data["list"][0]["components"]  # 주요 오염물질

    # AQI 지수 설명 (1~5)
    aqi_description = {
        1: "좋음 (Good) 😊",
        2: "보통 (Fair) 🙂",
        3: "나쁨 (Moderate) 😐",
        4: "상당히 나쁨 (Poor) 😷",
        5: "매우 나쁨 (Very Poor) 😨"
    }

    print(f"📍 서울({lat}, {lon})의 대기질 정보:")
    print(f"🌍 대기질 지수 (AQI): {air_quality} - {aqi_description.get(air_quality, '알 수 없음')}")
    print(f"💨 주요 오염물질:")
    print(f"   - CO (일산화탄소): {components['co']} μg/m³")
    print(f"   - NO (일산화질소): {components['no']} μg/m³")
    print(f"   - NO₂ (이산화질소): {components['no2']} μg/m³")
    print(f"   - O₃ (오존): {components['o3']} μg/m³")
    print(f"   - SO₂ (아황산가스): {components['so2']} μg/m³")
    print(f"   - PM2.5 (초미세먼지): {components['pm2_5']} μg/m³")
    print(f"   - PM10 (미세먼지): {components['pm10']} μg/m³")
    print(f"   - NH₃ (암모니아): {components['nh3']} μg/m³")