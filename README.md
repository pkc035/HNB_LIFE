# HNB_LIFE

---

## 환경 설정
- python==3.8.12
- django==3.2.5
- django-cors-headers==3.10.0
- django-filter==21.1
- djangorestframework==3.12.4
- mysql==5.7.24
- mysqlclient==2.0.3

---

## 테스트
- URL(예시)
  : http://127.0.0.1:8000/Search/shop?lat=37.00145&lon=127.11736&search=카페

- 필수 파라미터
  : lat, lot
  
- 선택 파라미터
  : search

- Output
  : [{"name":"골프연습장2","gps":{"lat":37.22222,"lon":127.22222},"tags":["카페테리아"]},{"name":"골프연습장1","gps":{"lat":37.11111,"lon":127.11111},"tags":["휴게시설","카페테리아"]},{"name":"골프연습장5","gps":{"lat":37.55555,"lon":127.55555},"tags":["실내연습장","카페테리아"]}]
