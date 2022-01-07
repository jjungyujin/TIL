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

### HTML 파일 보기
1. 크롬 브라우저 실행
2. 오른쪽 마우스 - 페이지 소스 보기

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
soup = BeatifulSoup(res.content.decode('euc-kr', 'replace'), 'html.parser')
```
`soup`에 HTML파일을 파싱한 정보가   
한글 인코딩을 위해 decode 필요

## 04. 필요한 데이터 추출하기
### 크롬 개발자 모드
단축기 Command + option + i (맥)

### 원하는 데이터 지정하기
방법 1. 태그와 속성으로 선택하기  
> html 코드
```
html = """
<html>
    <body>
        <h1 id='title'> [1] 크롤링이란? </h1>
        <p class='cssstyle'>웹페이지에서 <b>필요한</b> 데이터를 추출하는 것</p>
        <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p>
    </body>
</html>
"""
```
> 동일한 태그 문장 중 특정 문장 지정하기
- `(태그)`, `(id)`, `(class)`
- `(태그, id= )` , `(태그, class_= )`, `(태그, align= )`
- `(태그, attrs = {'속성': '속성값'})`
```
crawling_data = soup.find('h1')
crawling_data = soup.find('title')
crawling_data = soup.find('h1', class_='cssstyle')
crawling_data = soup.find('p', attrs = {'align': 'center'})
```
> 해당 태그의 모든 문장(의 리스트) 가져오기
```
crawling_data = soup.find_all('p')
```

방법 2. CSS Selector로 선택하기  
- 스페이스로 하위 태그 지정  
- 바로 아래 있는 태그를 조건으로 설정하려면 `>`로 지정
- `.클래스 이름` 또는 `#id`으로 검색 가능
- 하나의 태그에 여러개의 클래스가 있고 id까지 있는 경우 `.`으로 연결
```
crawling_data = soup.select('body b')
crawling_data = soup.select('p > b)
crawling_data = soup.select('div.article_view')
crawling_data = soup.select('#harmonyContainer')
```
결과값은 (객체들의) 리스트 형태로 반환됨  
매칭되는 첫번째 데이터만 얻으려면 `select_one()`

### 지정한 것에서 또 지정하기
- `find()`로 더 크게 감싸는 HTML 태그를 지정하고, 추출된 데이터(객체)에서 `find_all()`로 원하는 부분을 지정  
- `find() / select()`로 가져온 객체에 `find() / select()` 사용 가능(호환 가능)

### 텍스트 데이터만 추출하기
```
print(crawling_data.get_text())
print(crawling_data.get_string())
print(crawling_data.string)
```

## 05. 데이터 전처리
- `strip()` : 공백 제거
- `split()` : 지정된 값을 기준으로 좌우로 데이터를 나눔, list로 리턴