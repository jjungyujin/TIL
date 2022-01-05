# Hyper Text Markup Language

# 📎 01. HTML 시작하기
## HTML의 역할
웹 사이트에 들어갈 내용을 담당

## HTML 태그(요소)
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

**굵게 쓰기, 날려 쓰기**
1. 굵게 쓰기(bold) - ```<b>```
1. 날려 쓰기(italic) - ```<i>```
```
<h2> I <i>love</i> html ! </h2>

<p> I'm practicing <b>html</b> with <i>code it</i> lecture. </p>
```

## 한글 지원을 위한 인코딩
브라우저에 따라 한글을 지원하지 않는 경우도 존재  
어떤 브라우저를 쓰든 깨지지 않도록 하기 위해서 한글 인코딩 설정  
```
<meta charset = "utf-8">
<h3> HTML 학습을 위한 페이지 </h3>
```