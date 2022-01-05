## 01. 라이브러리 import
**필요 라이브러리**
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
