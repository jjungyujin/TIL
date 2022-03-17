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