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

```
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
```
<h2> I <i>love</i> html ! </h2><br>

<p> I'm practicing <b>html</b> with <i>code it</i> lecture. </p>
```

## 한글 지원을 위한 인코딩
인코딩 : 0과 1로 문자를 표현하는 규칙  
브라우저에 따라 한글을 지원하지 않는 경우도 존재  
어떤 브라우저를 쓰든 깨지지 않도록 하기 위해서 한글 인코딩 설정  
```
<meta charset = "utf-8">
<h3> HTML 학습을 위한 페이지 </h3>
```

## HTML 링크 태그
1. 외부 페이지로 이동하기
```
<a href="가고 싶은 주소"> 내용 </a>

// 새로운 탭에서 링크 열기
<a target="_blank" href="가고 싶은 주소"> 내용 </a>
```

2. 사이트 내부적으로 이동하기
```
<a href="html 파일의 상대경로"> 내용 </a>
```

## HTML 이미지 태그
```
<img src="이미지 파일" width ="너비" height="높이">
```
HTML 파일이 있는 폴더에 이미지 저장  
width, height를 설정하지 않으면 기존 크기대로 설정됨  

## 구조화된 태그 (표 만들기)
```
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

# 📎 02. 섹션
## 클래스(class)와 아이디(id)
태그를 구분하기 위한 속성
- 클래스 : 여러 태그를 구분짓는 단위, 여러 요소가 하나의 클래스 이름을 공유
- 아이디 : 하나의 태그에 부어하는 고유의 이름

## div 태그
여러 요소를 묶어주는 태그  
css 스타일링할 때 유용하게 쓰임
```
<div>
  <h1> </h1>
  <img>
  <p>
  </p>
</div>
```

## css 파일, js 파일 따로 쓰기
`.css`와 `.js` 파일을 따로 생성하고 html 파일에 연결
```
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
```
// css 코드 예시
td input[type=checkbox] {
  margin-left: 10px;
  margin-right: 10px;
}

// html 코드 예시
// selectAllCheckBox는 js파일에 정의된 함수
<input id="selectAll" type="button" onclick="selectAllCheckBox()">
```

# 📎 03. 꿀팁
## 코멘트
웹 사이트에 영향을 주진 않음  
코드의 가독성을 높이기 위한 문구
```
<!-- 코멘트 -->
```

## 크롬 개발자 도구
단축키 : command + option + i