웹 크롤링: 웹사이트 내용을 가져와서 내용을 분석해 필요한 정보만 골라낼 수 있어야 함.

YOUTUBE: 파이썬 requests 모듈을 이용하여 웹 페이지 긁어오기
(https://www.youtube.com/watch?v=94PJY-ORQrs)
- 웹 크롤링을 하기 위해 파이썬에서 어떤 것을 이용해야 하는지?
1) requests: 모듈을 가지고, 정보를 웹에 요청해서 그 요청한 값에 대한 html 파일 형태로 가져올 수 있다.
  - 긁어서 데이터 불러오기
2) BeautifulSoup: 모듈을 통해, 보고 싶은 정보 추출 가능.

URL을 GET 요청으로 페이지를 가져와서 상태 코드와 내용 확인
import requests

url='https://naver.com'
res=requests.get(url)
res.status_code

res.text # 응답값의 텍스트 값(html, 자바스크립트 등) 출력
