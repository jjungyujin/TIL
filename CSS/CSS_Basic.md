# Cascading Style Sheets

# ๐ 01. CSS ์์ํ๊ธฐ
## CSS์ ์ญํ 
์น ์ฌ์ดํธ์ ์คํ์ผ์ ๋ด๋น  
HTML์ ๋ด์ฉ์ ์คํ์ผ๋ง

## CSS ๊ธฐ๋ณธ ๋ฌธ๋ฒ
```html
<style>  
์คํ์ผ๋งํ  ์์ {์์ฑ : ์์ฑ๊ฐ;}  
</style>
```
**์คํ์ผ๋งํ  HTML ์ฝ๋**
```html
<!DOCTYPE html>

<title> My first Website </title>
<meta charset = "utf-8">

<h1> My first Page </h1>
<h2> I <i>love</i> html ! </h2>
<h3> HTML ํ์ต์ ์ํ ํ์ด์ง </h3>

<p> I'm practicing <b>html</b> with <i>code it</i> lecture. </p>
```
**CSS ์ฝ๋**
```html
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
๋์ผํ ํ๊ทธ๋ช์ด ์ฌ๋ฌ๋ฒ ์ฐ์ธ ๊ฒฝ์ฐ ํด๋น ํ๊ทธ๊ฐ ์ํ ๋ฐ๊นฅ ํ๊ทธ๋ช์ ๊ฐ์ด ๋ช์ํด์ฃผ๋ฉด ๊ตฌ๋ถ ๊ฐ๋ฅ (`p i` / `h2 i`)  
> style ํ๊ทธ๋ฅผ HTML ๋ฌธ์ฅ ์์ ๋ฃ์ด๋ ๋จ
```html
<h1 style="font-size: 64px; text-align: center;"> My first Page </h1>
```
> ์ฃผ๋ก cssํ์ผ์ ๋ฐ๋ก ์์ฑํ๊ณ  `<head>` ์์ ๋งํฌ (๊ถ์ฅ)
```html
<link rel="stylesheet" type="text/css" href="ํ์ผ๋ช(์๋๊ฒฝ๋ก ํฌํจ)">
```

## CSS ๊ธฐ๋ณธ ์์ฑ
- ํฐํธ ํฌ๊ธฐ  
`font-size: 72px;`  

- ํ์คํธ ์ ๋ ฌ  
`text-align: (right / left / center);`

- ํ์คํธ ์  
`color: lime;`  

- ์ฌ๋ฐฑ  
`margin-bottom: 80px;`  
`margin-left: 50px;`  
์ฌ๋ฐฑ์ผ๋ก ๊ฐ์ด๋ฐ ์ ๋ ฌ : `margin-left: auto;`, `margin-right: auto;`  
ํ๋๋ฆฌ ์ฌ๋ฐฑ : `padding: 50px`

## CSS ํ๊ทธ
1. ```<html>```  
์ ์ฒด ์ฝ๋๋ฅผ ๊ฐ์ธ์ฃผ๋ ํ๊ทธ
2. ```<head>```  
title, meta, css, js ์ฝ๋๋ฅผ ๊ฐ์ธ์ฃผ๋ ํ๊ทธ
2. ```<body>```  
์น ์ฌ์ดํธ์ ๋ณด์ฌ์ง ๋ด์ฉ์ ๊ฐ์ธ์ฃผ๋ ํ๊ทธ
> [codeit_practice_file](https://github.com/jjungyujin/TIL/blob/main/CSS/codeit_pracitce.html)

# ๐ 02. ํ์คํธ ์คํ์ผ๋ง
## ๋ด CSS ์คํ์ผ ๋ง๋ค๊ธฐ - ํด๋์ค
```css
.mystyle {
    font-size: 3em;
    text-align: center;
    color: blue;
}
```
```html
<title class="mystyle"> My first Website </title>
```

