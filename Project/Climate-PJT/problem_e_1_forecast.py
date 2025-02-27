# HTTP 요청을 보낼 수 있도록 도와주는 requests 라이브러리 import
import requests
from datetime import datetime, timedelta, timezone

# git push를 위해서 .env 파일에 정의한 API_KEY를 불러오기 위해 dotenv 라이브러리 import
import os
from dotenv import load_dotenv

load_dotenv()

# lat과 lon은 필수 변수이므로 현재 위치인 서울의 위도와 경도 할당. 
lat = 37.56
lon = 126.97

# 사용자의 API_KEY 할당. 상수이므로 변수명은 대문자 처리.
API_key = os.environ.get('API_KEY')

# 미래 날씨 정보를 제공해주는 API의 URL
URL = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}'

# requests.get(url)을 통해 API에 요청을 보냄
# 서버로부터 응답(Response)을 JSON 형태로 변환
data = requests.get(URL).json()

# 현재 날짜 기준 3일 후 타겟 날짜 계산
current_time = datetime.now(timezone.utc)
target_date = (current_time + timedelta(days=3)).date()

# 3일 후와 가장 가까운 예보 데이터 찾기
forecast_for_target_date = None

for forecast in data["list"]:
    forecast_time = datetime.fromtimestamp(forecast["dt"], timezone.utc)
    if forecast_time.date() == target_date:
        forecast_for_target_date = forecast
        break  # 가장 첫 번째 일치하는 데이터 사용

# 결과 출력
if forecast_for_target_date:
    temp = forecast_for_target_date["main"]["temp"]
    weather = forecast_for_target_date["weather"][0]["description"]
    print(f"📅 {target_date} 서울의 예상 날씨:")
    print(f"🌡️ 기온: {temp}°C")
    print(f"☁️ 날씨: {weather}")
else:
    print("날씨 정보를 찾을 수 없습니다.")