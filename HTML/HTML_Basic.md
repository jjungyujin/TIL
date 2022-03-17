# Hyper Text Markup Language

# 📎 01. HTML 시작하기
## HTML의 역할
웹 사이트에 들어갈 내용을 담당

## HTML 텍스트 태그(요소)
```<시작태그> 내용 </종료태그>```  

**기본 태그**  
1. ```<!DOCTYPE>``` 선언  
HTML 파일을 쓸 때 파일의 타입 선언  
가장 최신 버전인 HTML5를 사용하려면 ```<!DOCTYPE html>```
2. ```<title>``` 태그  
페이지의 제목(브라우저의 탭이나 방문 기록에 해당)  
3. ```<h1>```~```<h6> ```태그  
중요도에 따라 머리말 작성  
머리말의 크기가 ```<h1>```부터 순서대로 작아짐  
4. ```<p>``` 태그  
문단 내용 작성  

```html
<!DOCTYPE html>
<title> My First Website </title>

<h1> My first Page </h1>
<h2> I love html ! </h2>
<h3> HTML 학습을 위한 페이지 </h3>

<p> I'm practicing html with code it lecture. </p>
```

**굵게 쓰기, 날려 쓰기, 줄바꿈**
1. 굵게 쓰기(bold) - ```<b>```
2. 날려 쓰기(italic) - ```<i>```
3. 줄바꿈(enter) - ```<br>```
```html
<h2> I <i>love</i> html ! </h2><br>

<p> I'm practicing <b>html</b> with <i>code it</i> lecture. </p>
```

**formatting**
1. 텍스트 형광펜 효과 - `<mark>`
2. 텍스트 가운데에 선 긋기 - `<del>`
3. 텍스트에 밑줄 긋기 - `<ins>`
4. 텍스트의 아래 첨자 / 위 첨자 - `<sub>`, `<sup>`

**Quotation**
1. 인용문단 / 인용문장 태그 - `<blockquote cite="">`, `<q>`  
2. 약자 태그 - `<abbr title=" ">`
```html
<!-- 태그에 mouse over 하면 title 문구가 tooltip text로 나타남 -->
<p>The <abbr title="World Health Organization">WHO</abbr> was founded in 1948.</p>
```
3. 주소 정보 태그 - `<address>`
4. 시, 영화, 노래, 그림 등과 같은 저작물 태그 - `<cite>`
5. 텍스트의 입력 방향 설정 - `<bdo>`
```html
<!-- 텍스트를 오른쪽에서 왼쪽 방향으로 쓰기 -->
<bdo dir="rtl">This text will be written from right to left</bdo>
```

## 한글 지원을 위한 인코딩
인코딩 : 0과 1로 문자를 표현하는 규칙  
브라우저에 따라 한글을 지원하지 않는 경우도 존재  
어떤 브라우저를 쓰든 깨지지 않도록 하기 위해서 한글 인코딩 설정  
```html
<meta charset = "utf-8">
<h3> HTML 학습을 위한 페이지 </h3>
```

## HTML 링크 태그
1. 외부 페이지로 이동하기
```html
<a href="가고 싶은 주소"> 내용 </a>

<!-- 새로운 탭에서 링크 열기 -->
<a target="_blank" href="가고 싶은 주소"> 내용 </a>
```

2. 사이트 내부적으로 이동하기
```html
<a href="html 파일의 상대경로"> 내용 </a>
```

3. 이메일 작성 링크
```html
<!-- a 태그에도 title 설정 가능 (mouse over 시 tooltip으로 보여주기) -->
<a href="mailto:wjd1dbwls@gmail.com" title="Send email to wjd1dbwls@gmail.com">Send email to me</a>
```

**경우에 따른 style 설정하기**
1. `a:link` : 기본적으로 보여지는 경우
2. `a:visited` : 클릭했던 기록이 있는 경우
3. `a:hover` : mouse over된 경우
4. `a:active` : 클릭이 활성화된 상태인 경우

## HTML 이미지 태그
```html
<img src="이미지 파일" width ="너비" height="높이" alt="대체할 문구">
```
alt는 해당 이미지가 화면에 제대로 나타나지 않은 경우 입력한 텍스트를 대신 보여줌
width, height를 설정하지 않으면 기존 크기대로 설정됨  

**Image Map : 이미지 내에 클릭 가능한 영역 만들기**
```html
<img src="workplace.jpg" alt="Workplace" usemap="#workmap">

<map name="workmap">
  <!-- area 태그의 속성
  shape : 영역의 모양 설정
  coords : 영역의 위치 및 크기 설정 (이미지의 왼쪽 상단 모서리 기준)
  href : 클릭 시 이동할 페이지
  -->

  <area shape="rect" coords="34,44,270,350" alt="Computer" href="computer.htm">
  <area shape="rect" coords="290,172,333,250" alt="Phone" href="phone.htm">
  <area shape="circle" coords="337,300,44" alt="Coffee" href="coffee.htm">
</map>>
```

**picture 태그**
브라우저 창의 크기(`media`)에 따라 보여줄 이미지(`srcset`) 설정  
여러 `<source>`를 포함하는 태그  
마지막 `<img>`는 조건에 맞는 source가 없을 경우 보여줄 이미지 태그
```html
<picture>
  <source media="(min-width: 650px)" srcset="img_food.jpg">
  <source media="(min-width: 465px)" srcset="img_car.jpg">
  <img src="img_girl.jpg">
</picture>
```
> picture 태그를 사용하는 또다른 목적  
> : 일부 브라우저 또는 장치는 이미지 형식을 지원하지 않을 수 있으므로 `<picture>` 요소를 사용하여 모든 형식의 이미지를 추가  
> 브라우저는 인식하는 첫 번째 형식을 사용하고 다음 요소를 무시함
```html
<picture>
  <source srcset="img_avatar.png">
  <source srcset="img_girl.jpg">
  <img src="img_beatles.gif" alt="Beatles" style="width:auto;">
</picture>
```

## 구조화된 태그 (표 만들기)
```html
<table border="1" width="500">
    <thead>
        <tr>
            <th>학번</th>
            <th>이름</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>202012452</td>
            <td>정유진</td>
        </tr>
    </tbody>
</table>
```
- `border` : 테이블의 경계선 굵기  
- `thead` : 테이블의 가장 상단 (주로 머리글)  
- `tbody` : 테이블의 본문  
- `tr` : 테이블의 한 행  
- `th`, `td` : 해당 행의 열, 머리글에서의 열과 본문에서의 열의 수가 같아야 함

**Table Borders**
`border-collapse` : 중복되는 경계선 없애기
```css
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
```

**Table Headers**
- `colspan` : 2개 이상의 열을 하나의 Header로 묶기
- `rowspan` : 2개 이상의 행을 하나의 Header로 묶기
```html
<table style="width:100%">
  <tr> 
  	<th colspan="2">Info</th>
  </tr>
  <tr>
    <th>Name</th>
    <td>Jill</td>
  </tr>
  <tr>
    <th rowspan="2">Phone</th>
    <td>555-1234</td>
  </tr>
  <tr>
    <td>555-8745</td>
  </tr>
</table>
``` 
- `<caption>` : 테이블 제목

# 📎 02. 섹션
## 클래스(class)와 아이디(id)
태그를 구분하기 위한 속성
- 클래스 : 여러 태그를 구분짓는 단위, 여러 요소가 하나의 클래스 이름을 공유
- 아이디 : 하나의 태그에 부어하는 고유의 이름

## div 태그
여러 요소를 묶어주는 태그  
태그 안의 요소를 단독적인 단락으로 넣음
```html
<div>
  <h1> </h1>
  <img>
  <p>
  </p>
</div>
```

## span 태그
하나의 단락 내에서 특정 부분을 묶어주는 태그  
div와는 다르게 단독적인 단락으로 나누지 않음

## css 파일, js 파일 따로 쓰기
`.css`와 `.js` 파일을 따로 생성하고 html 파일에 연결
```html
<html>
<head>
  <link rel="stylesheet" type="text/css" href="파일명(상대경로 포함)">
</head>
<body>
  <script src="파일명(상대경로 포함)"></script>
</body>
</html>
```

css 파일에서는 html의 태그를 지정하여 style을 정의하고  
js 파일에 있는 함수를 태그에 적용할 때는 html 파일의 태그에 속성으로 넣어줌
```css
td input[type=checkbox] {
  margin-left: 10px;
  margin-right: 10px;
}
```
```html
<!-- selectAllCheckBox는 js파일에 정의된 함수 -->
<input id="selectAll" type="button" onclick="selectAllCheckBox()">
```
html 파일을 실행하여 브라우저를 열기 - css 적용 확인  
개발자 도구로 html 코드 변화 확인 - js 기능 구현 확인

# 📎 03. 꿀팁
## 코멘트
웹 사이트에 영향을 주진 않음  
코드의 가독성을 높이기 위한 문구  
단축키 : command + /
```html
<!-- comment -->
```

## 크롬 개발자 도구
단축키 : command + option + i
