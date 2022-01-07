# Cascading Style Sheets

# 📎 01. CSS 시작하기
## CSS의 역할
웹 사이트의 스타일을 담당  
HTML의 내용을 스타일링

## CSS 기본 문법
```
<style>  
스타일링할 요소 {속성 : 속성값;}  
</style>
```
**스타일링할 HTML 코드**
```
<!DOCTYPE html>

<title> My first Website </title>
<meta charset = "utf-8">

<h1> My first Page </h1>
<h2> I <i>love</i> html ! </h2>
<h3> HTML 학습을 위한 페이지 </h3>

<p> I'm practicing <b>html</b> with <i>code it</i> lecture. </p>
```
**CSS 코드**
```
<style type="text/css">
h1 {
    font-size: 64px;
    font-family: Gulim;
    text-align: center;
}

h3 {
    margin-top: 100px;
}

p i {
    font-size: 36px;
}
</style>
```
동일한 태그명이 여러번 쓰인 경우 해당 태그가 속한 바깥 태그명을 같이 명시해주면 구분 가능 (```p i``` / ```h2 i```)  
> style 태그를 HTML 문장 안에 넣어도 됨
```
<h1 style="font-size: 64px; text-align: center;"> My first Page </h1>
```
> 주로 css파일을 따로 작성하고 `<head>` 안에 링크 (권장)
```
<link rel="stylesheet" type="text/css" href="파일명(상대경로 포함)">
```

## CSS 기본 속성
- **폰트 크기**  
```font-size: 72px;```  

- **텍스트 정렬**  
```text-align: (right / left / center);```

- **텍스트 색**  
```color: lime;```  

- **여백**  
```margin-bottom: 80px;```  
```margin-left: 50px;```

## CSS 태그
1. ```<html>```  
전체 코드를 감싸주는 태그
2. ```<head>```  
title, meta, css, js 코드를 감싸주는 태그
2. ```<body>```  
웹 사이트에 보여질 내용을 감싸주는 태그
> [codeit_practice_file](https://github.com/jjungyujin/TIL/blob/main/CSS/codeit_pracitce.html)

# 📎 02. 텍스트 스타일링
## 내 CSS 스타일 만들기
**CSS파일**
```
.mystyle{
    font-size: 3em;
    text-align: center;
    color: blue;
}
```

**HTML 파일**
```
<title class="mystyle"> My first Website </title>
```