# CRAWLING

## 00. INTRO
### 배경
1. 컴퓨터에 Network device라는 모듈이 들어가면서 컴퓨터 간의 통신이 가능해짐
2. 통신할 컴퓨터를 지칭하기 위해 IP 주소가 생김
3. IP 주소를 외우기가 어려워 웹 브라우저의 주소로 매칭하는 기술이 개발됨

### 웹 기본 구조 이해
1. 웹 브라우저에서 주소를 입력
2. 해당 컴퓨터(통신하려는 컴퓨터)에 가서 주소에 알맞는 HTML 파일을 전송받음
3. HTML 파일을 변환하여 내 컴퓨터의 웹 브라우저에서 보여줌

### 모듈 설치
```
python3 -m pip install --upgrade pip
pip install requests
pip install bs4
```
이미 pip가 업그레이드 되어있다면 바로 install하기

## 01. 라이브러리 import
### 필요 라이브러리
- requests  
웹페이지 가져오기 라이브러리
- bs4 (BeautifulSoup)  
웹페이지 분석(크롤링) 라이브러리
```
import requests
from bs4 import BeautifulSoup
```

## 02. 웹페이지 가져오기
```
res = requests.get('크롤링할 사이트의 주소')
```
`res.content`에 해당 사이트의 HTML 파일이 저장됨

## 03. 웹페이지 파싱(parsing)하기
### 파싱이란 ?
문자열의 의미 분석

### 파싱하기 (BeatifulSoup)
```
soup = BeatifulSoup(res.content, 'html.parser')
```
`soup`에 HTML파일을 파싱한 정보가 들억감

## 04. 필요한 데이터 추출하기
### 원하는 데이터 지정하기
방법 1. 태그와 속성으로 선택하기
```
crawling_data = soup.find('h1')
crawling_data = soup.find(id = 'title')
crawling_data = soup.find('p', attrs = {'align': 'center'})
```

방법 2. CSS Selector로 선택하기
```
crawling_data = soup.select('html > title')
crawling_data = soup.select('div.article_view')
crawling_data = soup.select('#harmonyContainer')
```

### 데이터 추출하기
`.get_text()` 함수로 필요한 부분을 가져옴
```
print(crawling_data.get_text())
```