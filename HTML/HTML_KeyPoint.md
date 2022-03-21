# 📎 01. Box Model
## Box 모델 소개
html의 모든 요소는 박스의 형태  
[박스 모델 css 스타일링 -  01](https://github.com/jjungyujin/TIL/blob/main/CSS/CSS_KeyPoint.md)

![Box Model](HTML_KeyPoint_BoxModel.png)

## overflow
박스의 크기 설정에 따라 내용이 박스 크기를 초과하기도 함  
overflow 속성으로 넘치는 내용 처리 가능

# 📎 02. Display
## display 속성
inline, block, inline-block, list-item, table, flex, none 등  
모든 요소는 딱 하나의 display 값을 가지며 대부분 inline과 block 중 한 가지

1. inline - `<span>`, `<a>`, `<b>`, `<img>`, `<button>`  
다른 요소들과 같은 줄에 머무르려고 하는 성향  
가로 길이는 필요한 만큼만 차지하는 성향 (박스 크기가 자동 결정)  
딘, `<img>`는 크기 설정이 가능한 inline 요소

2. block - `<div>`, `<h1>`, `<p>`, `<ul>`, `<li>`  
새로운 줄에 가려는 성향  
가로 길이를 최대한 많이 차지하려는 성향

3. inline-block  
다른 요소들과 같은 줄에 있으면서 박스 크기 설정이 가능  
[css로 display 설정하기 - 03](https://github.com/jjungyujin/TIL/blob/main/CSS/CSS_KeyPoint.md)

inline과 inline-block 요소의 가장 큰 특징 : 해당 요소를 텍스트처럼 다룰 수 있음

## 다양한 링크
> 텍스트가 아닌 요소 노드에 링크를 연결  
```html
<a href="가고 싶은 주소"> <링크를 연결할 요소> </a>
```

> 여러 요소를 링크와 연결  
```html
<a class="google=link" href="https://google.com" target="_blank">
  <img>
  <h1> </h1>
  <p> </p>
</a>
```
```css
.a {
  /* a의 display 변경 */
  display: block;

  /* 텍스트 링크 기본 스타일 제거 */
  color: black;
  text-decoration: none;
}
```

## Baseline
inline 요소들은 각 박스의 baseline들이 맞춰져 정렬됨  

> 텍스트의 baseline

![Baseline](HTML_Baseline.png)

> 이미지의 baseline : 이미지의 하단  

> inline-block의 baseline  
`<div>`로 묶인 여러 요소를 inline-block으로 설정한 경우 마지막 요소의 baseline에 맞춤  

## vertical-align
기본값 : baseline  
그 외 : top, middle, bottom

# 📎 03. List
## list 태그
1. `<ol>`  
순서가 있는 리스트 (Ordered List)   
순서대로 `<li>` (list item)에 번호를 부여해서 출력함
```html
<ol>
  <li>집 청소</li>            // 1. 집 청소
  <li>영어 단어 외우기</li>     // 2. 영어 단어 외우기
</ol>
```
> type 속성
```html
<ol type="a">
  <li>집 청소</li>            // a. 집 청소
  <li>영어 단어 외우기</li>     // b. 영어 단어 외우기
</ol>

<ol type="i">
  <li>집 청소</li>            // i. 집 청소
  <li>영어 단어 외우기</li>     // ii. 영어 단어 외우기
```

2. `<ul>`  
순서가 없는 리스트 (Unordered List)  
`display: list-item;`으로 설정되어 있음 ([css로 리스트 스타일링 - 06](https://github.com/jjungyujin/TIL/blob/main/CSS/CSS_KeyPoint.md))  

> [ul을 이용한 웹 페이지의 네비게이션 바 만들기](https://github.com/jjungyujin/TIL/blob/main/HTML/web_nav.html)

# 📎 04. Iframe
웹 페이지 안에 웹 페이지 화면 나타내기
```html
<iframe src="url" title="description"></iframe>
```

링크 태그의 `target` 속성으로 Iframe의 페이지 이동 가능
```html
<iframe src="demo_iframe.htm" name="iframe_a" title="Iframe Example"></iframe>

<p><a href="https://www.w3schools.com" target="iframe_a">W3Schools.com</a></p>
```

# 📎 05. Responsive
## Responsive web design
모든 디바이스에서 보기 좋은 웹 페이지 만들기  
스크린의 크기에 따라 자동적으로 조절됨

## Setting The Viewport
`<meta>`는 페이지의 viewport를 설정하고, 페이지의 크기와 배율을 제어하는 방법에 대한 브라우저의 지침을 제공
```html
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

## Responsive Images
1. `width`를 100%로 설정
```html
<img src="img_girl.jpg" style="width:100%;">
```

2. `max-width`를 100%로 설정  
원본 크기보다 커지지 않도록 하기 위한 설정
```html
<img src="img_girl.jpg" style="max-width:100%;">
```

## Responsive Text Size
`font-size`에서 단위 `vw`는 viewport width를 의미
```html
<!-- viewport width의 10% 크기로 설정 -->
<h1 style="font-size:10vw">Hello World</h1>
```

## Media Queries
서로 다른 브라우저의 크기에 완전히 다른 스타일 정의하기
```css
.left, .right {
  float: left;
  width: 20%; /* default */
}

.main {
  float: left;
  width: 60%; /* default */
}

/* 브라우저의 width의 breakpoint : 800px: */
@media screen and (max-width: 800px) {
  .left, .main, .right {
    width: 100%; 
    /* viewport가 800px보다 작거나 같은 경우에 적용됨 */
  }
}
```

# 📎 06. Forms
## HTML Forms
사용자로부터 입력을 받고 입력된 값을 처리하기 위한 목적
```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
</form>
```

### Label 태그
form 요소를 정의하기 위한 태그  
`for` 속성 : 연결시킬 `input`태그의 `id`값 입력

### Input 태그의 type
- text & password & email : 텍스트 / 암호 / 이메일 주소 입력창
- radio & checkbox : 선택지 중 하나 / 0개 이상 선택
- button : 클릭 가능한 버튼
- submit & reset ; form 제출 / form의 default 값으로 초기화 버튼
- color & date : 색상 선택 팔레트 / 날짜 선택 달력
- file : 첨부파일 선택 버튼

### The Submit Button
`form` 데이터를 `form-handler`에 넘겨주는 버튼  
> form-handler  
입력 받은 데이터를 스크립트로 처리하는 파일
`<form>`의 action 속성에서 지정
```html
<!-- action_page.php 파일에 정보 전송 -->
<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <!-- value : default로 입력된 값 -->
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>
```

### Input 태그의 name
input 값을 `submit`으로 넘겨주기 위해서는 `name`속성을 반드시 가져야 함

### Input 태그의 Attributes
- value & placeholder
- readonly & disabled
- size & maxlength
- min & max & pattern & step
- multiple
- required & autofocus
- height & width
- list

## Form의 속성
### Action
`form` 정보를 넘겨받았을 때 수행할 작업을 정의  
- `"action_page.php"` : `form` 정보를 다루는 server-side script를 담고 있는 파일  
- 입력 생략 시 현재 페이지가 default로 설정됨

### Target
submit에 대한 response를 보여줄 화면 설정
- _blank : 새로운 탭에서 보여주기
- _self : 현재 윈도우에서 보여주기 (default)
- framename : 지정한 Iframe에서 보여주기

### Method
1. get : url 변수로 전송
사용자의 입력 정보가 url에 노출된다는 문제점  
get 요청 북마크 가능  
브라우저마다 길이에 제한이 있음  
서버의 리소스에서 데이터를 요청할 때 사용 (SELECT)  

2. post : HTTP request의 body에 담아서 전송
url에 노출되지 않아 보안이 필요한 부분에 사용  
post 요청 북마크 불가능  
데이터 길이에 제한 없음  
서버의 리소스를 새로 생성하거나 업데이트할 때 사용 (CREATE)

### Autocomplete
입력했던 값을 저장하여 자동 완성하기
```html
<form action="/action_page.php" autocomplete="on">
```

### Novalidate
유효성(입력값의 여부) 검사하기  
생략 시 유효성 검사 없이 실행
```html
<form action="/action_page.php" novalidate>
```

## Form의 요소
### Input & Label
```html
<label for="fname">First name:</label>
<input type="text" id="fname" name="fname">
```

### Select
drop-down list 생성하기  
- selected
- size
- multiple
```html
<label for="cars">Choose a car:</label>
<select id="cars" name="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <!-- selected : default로 fiat 설정 -->
  <option value="fiat" selected>Fiat</option>
  <option value="audi">Audi</option>
</select>
```

### Textarea
입력 가능한 텍스트 상자
```html
<textarea name="message" rows="10" cols="30">
The cat was playing in the garden.
</textarea>
```

### Button
```html
<!-- aler : 알림창 띄우기 -->
<button type="button" onclick="alert('Hello World!')">Click Me!</button>
```

### Fieldset & Legend
`fieldset` : `form`에서 데이터와 관련된 그룹 묶기 (테두리 상자 생성)  
`legend` : `fieldset`의 표제
```html
<form action="/action_page.php">
  <fieldset>
    <legend>Personalia:</legend>
    <label for="fname">First name:</label><br>
    <input type="text" id="fname" name="fname" value="John"><br>
    <label for="lname">Last name:</label><br>
    <input type="text" id="lname" name="lname" value="Doe"><br><br>
    <input type="submit" value="Submit">
  </fieldset>
</form>
```

### Datalist
입력 가능하면서 선택지가 있는 입력창 생성

```html
<form action="/action_page.php">
  <!-- list 속성에 연결시킬 datalist의 id값 입력 -->
  <input list="browsers">
  <datalist id="browsers">
    <option value="Internet Explorer">
    <option value="Firefox">
    <option value="Chrome">
    <option value="Opera">
    <option value="Safari">
  </datalist> 
</form>
```