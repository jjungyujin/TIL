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

## HTML 이미지 태그
```
<img src="이미지 파일" width ="너비" height="높이">
```
HTML 파일이 있는 폴더에 이미지 저장  
width, height를 설정하지 않으면 기존 크기대로 설정됨  
경우에 따라 `id`를 설정하기도 함

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