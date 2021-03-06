# ๐ 01. Box Model
## Box ๋ชจ๋ธ ์๊ฐ
html์ ๋ชจ๋  ์์๋ ๋ฐ์ค์ ํํ  
[๋ฐ์ค ๋ชจ๋ธ css ์คํ์ผ๋ง -  01](https://github.com/jjungyujin/TIL/blob/main/CSS/CSS_KeyPoint.md)

![Box Model](HTML_KeyPoint_BoxModel.png)

## overflow
๋ฐ์ค์ ํฌ๊ธฐ ์ค์ ์ ๋ฐ๋ผ ๋ด์ฉ์ด ๋ฐ์ค ํฌ๊ธฐ๋ฅผ ์ด๊ณผํ๊ธฐ๋ ํจ  
overflow ์์ฑ์ผ๋ก ๋์น๋ ๋ด์ฉ ์ฒ๋ฆฌ ๊ฐ๋ฅ

# ๐ 02. Display
## display ์์ฑ
inline, block, inline-block, list-item, table, flex, none ๋ฑ  
๋ชจ๋  ์์๋ ๋ฑ ํ๋์ display ๊ฐ์ ๊ฐ์ง๋ฉฐ ๋๋ถ๋ถ inline๊ณผ block ์ค ํ ๊ฐ์ง

1. inline - `<span>`, `<a>`, `<b>`, `<img>`, `<button>`  
๋ค๋ฅธ ์์๋ค๊ณผ ๊ฐ์ ์ค์ ๋จธ๋ฌด๋ฅด๋ ค๊ณ  ํ๋ ์ฑํฅ  
๊ฐ๋ก ๊ธธ์ด๋ ํ์ํ ๋งํผ๋ง ์ฐจ์งํ๋ ์ฑํฅ (๋ฐ์ค ํฌ๊ธฐ๊ฐ ์๋ ๊ฒฐ์ )  
๋, `<img>`๋ ํฌ๊ธฐ ์ค์ ์ด ๊ฐ๋ฅํ inline ์์

2. block - `<div>`, `<h1>`, `<p>`, `<ul>`, `<li>`  
์๋ก์ด ์ค์ ๊ฐ๋ ค๋ ์ฑํฅ  
๊ฐ๋ก ๊ธธ์ด๋ฅผ ์ต๋ํ ๋ง์ด ์ฐจ์งํ๋ ค๋ ์ฑํฅ

3. inline-block  
๋ค๋ฅธ ์์๋ค๊ณผ ๊ฐ์ ์ค์ ์์ผ๋ฉด์ ๋ฐ์ค ํฌ๊ธฐ ์ค์ ์ด ๊ฐ๋ฅ  
[css๋ก display ์ค์ ํ๊ธฐ - 03](https://github.com/jjungyujin/TIL/blob/main/CSS/CSS_KeyPoint.md)

inline๊ณผ inline-block ์์์ ๊ฐ์ฅ ํฐ ํน์ง : ํด๋น ์์๋ฅผ ํ์คํธ์ฒ๋ผ ๋ค๋ฃฐ ์ ์์

## ๋ค์ํ ๋งํฌ
> ํ์คํธ๊ฐ ์๋ ์์ ๋ธ๋์ ๋งํฌ๋ฅผ ์ฐ๊ฒฐ  
```html
<a href="๊ฐ๊ณ  ์ถ์ ์ฃผ์"> <๋งํฌ๋ฅผ ์ฐ๊ฒฐํ  ์์> </a>
```

> ์ฌ๋ฌ ์์๋ฅผ ๋งํฌ์ ์ฐ๊ฒฐ  
```html
<a class="google=link" href="https://google.com" target="_blank">
  <img>
  <h1> </h1>
  <p> </p>
</a>
```
```css
.a {
  /* a์ display ๋ณ๊ฒฝ */
  display: block;

  /* ํ์คํธ ๋งํฌ ๊ธฐ๋ณธ ์คํ์ผ ์ ๊ฑฐ */
  color: black;
  text-decoration: none;
}
```

## Baseline
inline ์์๋ค์ ๊ฐ ๋ฐ์ค์ baseline๋ค์ด ๋ง์ถฐ์ ธ ์ ๋ ฌ๋จ  

> ํ์คํธ์ baseline

![Baseline](HTML_Baseline.png)

> ์ด๋ฏธ์ง์ baseline : ์ด๋ฏธ์ง์ ํ๋จ  

> inline-block์ baseline  
`<div>`๋ก ๋ฌถ์ธ ์ฌ๋ฌ ์์๋ฅผ inline-block์ผ๋ก ์ค์ ํ ๊ฒฝ์ฐ ๋ง์ง๋ง ์์์ baseline์ ๋ง์ถค  

## vertical-align
๊ธฐ๋ณธ๊ฐ : baseline  
๊ทธ ์ธ : top, middle, bottom

# ๐ 03. List
## list ํ๊ทธ
1. `<ol>`  
์์๊ฐ ์๋ ๋ฆฌ์คํธ (Ordered List)   
์์๋๋ก `<li>` (list item)์ ๋ฒํธ๋ฅผ ๋ถ์ฌํด์ ์ถ๋ ฅํจ
```html
<ol>
  <li>์ง ์ฒญ์</li>            // 1. ์ง ์ฒญ์
  <li>์์ด ๋จ์ด ์ธ์ฐ๊ธฐ</li>     // 2. ์์ด ๋จ์ด ์ธ์ฐ๊ธฐ
</ol>
```
> type ์์ฑ
```html
<ol type="a">
  <li>์ง ์ฒญ์</li>            // a. ์ง ์ฒญ์
  <li>์์ด ๋จ์ด ์ธ์ฐ๊ธฐ</li>     // b. ์์ด ๋จ์ด ์ธ์ฐ๊ธฐ
</ol>

<ol type="i">
  <li>์ง ์ฒญ์</li>            // i. ์ง ์ฒญ์
  <li>์์ด ๋จ์ด ์ธ์ฐ๊ธฐ</li>     // ii. ์์ด ๋จ์ด ์ธ์ฐ๊ธฐ
```

2. `<ul>`  
์์๊ฐ ์๋ ๋ฆฌ์คํธ (Unordered List)  
`display: list-item;`์ผ๋ก ์ค์ ๋์ด ์์ ([css๋ก ๋ฆฌ์คํธ ์คํ์ผ๋ง - 06](https://github.com/jjungyujin/TIL/blob/main/CSS/CSS_KeyPoint.md))  

> [ul์ ์ด์ฉํ ์น ํ์ด์ง์ ๋ค๋น๊ฒ์ด์ ๋ฐ ๋ง๋ค๊ธฐ](https://github.com/jjungyujin/TIL/blob/main/HTML/web_nav.html)

# ๐ 04. Iframe
์น ํ์ด์ง ์์ ์น ํ์ด์ง ํ๋ฉด ๋ํ๋ด๊ธฐ
```html
<iframe src="url" title="description"></iframe>
```

๋งํฌ ํ๊ทธ์ `target` ์์ฑ์ผ๋ก Iframe์ ํ์ด์ง ์ด๋ ๊ฐ๋ฅ
```html
<iframe src="demo_iframe.htm" name="iframe_a" title="Iframe Example"></iframe>

<p><a href="https://www.w3schools.com" target="iframe_a">W3Schools.com</a></p>
```

# ๐ 05. Responsive
## Responsive web design
๋ชจ๋  ๋๋ฐ์ด์ค์์ ๋ณด๊ธฐ ์ข์ ์น ํ์ด์ง ๋ง๋ค๊ธฐ  
์คํฌ๋ฆฐ์ ํฌ๊ธฐ์ ๋ฐ๋ผ ์๋์ ์ผ๋ก ์กฐ์ ๋จ

## Setting The Viewport
`<meta>`๋ ํ์ด์ง์ viewport๋ฅผ ์ค์ ํ๊ณ , ํ์ด์ง์ ํฌ๊ธฐ์ ๋ฐฐ์จ์ ์ ์ดํ๋ ๋ฐฉ๋ฒ์ ๋ํ ๋ธ๋ผ์ฐ์ ์ ์ง์นจ์ ์ ๊ณต
```html
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

## Responsive Images
1. `width`๋ฅผ 100%๋ก ์ค์ 
```html
<img src="img_girl.jpg" style="width:100%;">
```

2. `max-width`๋ฅผ 100%๋ก ์ค์   
์๋ณธ ํฌ๊ธฐ๋ณด๋ค ์ปค์ง์ง ์๋๋ก ํ๊ธฐ ์ํ ์ค์ 
```html
<img src="img_girl.jpg" style="max-width:100%;">
```

## Responsive Text Size
`font-size`์์ ๋จ์ `vw`๋ viewport width๋ฅผ ์๋ฏธ
```html
<!-- viewport width์ 10% ํฌ๊ธฐ๋ก ์ค์  -->
<h1 style="font-size:10vw">Hello World</h1>
```

## Media Queries
์๋ก ๋ค๋ฅธ ๋ธ๋ผ์ฐ์ ์ ํฌ๊ธฐ์ ์์ ํ ๋ค๋ฅธ ์คํ์ผ ์ ์ํ๊ธฐ
```css
.left, .right {
  float: left;
  width: 20%; /* default */
}

.main {
  float: left;
  width: 60%; /* default */
}

/* ๋ธ๋ผ์ฐ์ ์ width์ breakpoint : 800px: */
@media screen and (max-width: 800px) {
  .left, .main, .right {
    width: 100%; 
    /* viewport๊ฐ 800px๋ณด๋ค ์๊ฑฐ๋ ๊ฐ์ ๊ฒฝ์ฐ์ ์ ์ฉ๋จ */
  }
}
```

# ๐ 06. Forms
## HTML Forms
์ฌ์ฉ์๋ก๋ถํฐ ์๋ ฅ์ ๋ฐ๊ณ  ์๋ ฅ๋ ๊ฐ์ ์ฒ๋ฆฌํ๊ธฐ ์ํ ๋ชฉ์ 
```html
<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname">
</form>
```

### Label ํ๊ทธ
form ์์๋ฅผ ์ ์ํ๊ธฐ ์ํ ํ๊ทธ  
`for` ์์ฑ : ์ฐ๊ฒฐ์ํฌ `input`ํ๊ทธ์ `id`๊ฐ ์๋ ฅ

### Input ํ๊ทธ์ type
- text & password & email : ํ์คํธ / ์ํธ / ์ด๋ฉ์ผ ์ฃผ์ ์๋ ฅ์ฐฝ
- radio & checkbox : ์ ํ์ง ์ค ํ๋ / 0๊ฐ ์ด์ ์ ํ
- button : ํด๋ฆญ ๊ฐ๋ฅํ ๋ฒํผ
- submit & reset ; form ์ ์ถ / form์ default ๊ฐ์ผ๋ก ์ด๊ธฐํ ๋ฒํผ
- color & date : ์์ ์ ํ ํ๋ ํธ / ๋ ์ง ์ ํ ๋ฌ๋ ฅ
- file : ์ฒจ๋ถํ์ผ ์ ํ ๋ฒํผ

### The Submit Button
`form` ๋ฐ์ดํฐ๋ฅผ `form-handler`์ ๋๊ฒจ์ฃผ๋ ๋ฒํผ  
> form-handler  
์๋ ฅ ๋ฐ์ ๋ฐ์ดํฐ๋ฅผ ์คํฌ๋ฆฝํธ๋ก ์ฒ๋ฆฌํ๋ ํ์ผ
`<form>`์ action ์์ฑ์์ ์ง์ 
```html
<!-- action_page.php ํ์ผ์ ์ ๋ณด ์ ์ก -->
<form action="/action_page.php">
  <label for="fname">First name:</label><br>
  <!-- value : default๋ก ์๋ ฅ๋ ๊ฐ -->
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" value="Submit">
</form>
```

### Input ํ๊ทธ์ name
input ๊ฐ์ `submit`์ผ๋ก ๋๊ฒจ์ฃผ๊ธฐ ์ํด์๋ `name`์์ฑ์ ๋ฐ๋์ ๊ฐ์ ธ์ผ ํจ

### Input ํ๊ทธ์ Attributes
- value & placeholder
- readonly & disabled
- size & maxlength
- min & max & pattern & step
- multiple
- required & autofocus
- height & width
- list

## Form์ ์์ฑ
### Action
`form` ์ ๋ณด๋ฅผ ๋๊ฒจ๋ฐ์์ ๋ ์ํํ  ์์์ ์ ์  
- `"action_page.php"` : `form` ์ ๋ณด๋ฅผ ๋ค๋ฃจ๋ server-side script๋ฅผ ๋ด๊ณ  ์๋ ํ์ผ  
- ์๋ ฅ ์๋ต ์ ํ์ฌ ํ์ด์ง๊ฐ default๋ก ์ค์ ๋จ

### Target
submit์ ๋ํ response๋ฅผ ๋ณด์ฌ์ค ํ๋ฉด ์ค์ 
- _blank : ์๋ก์ด ํญ์์ ๋ณด์ฌ์ฃผ๊ธฐ
- _self : ํ์ฌ ์๋์ฐ์์ ๋ณด์ฌ์ฃผ๊ธฐ (default)
- framename : ์ง์ ํ Iframe์์ ๋ณด์ฌ์ฃผ๊ธฐ

### Method
1. get : url ๋ณ์๋ก ์ ์ก
์ฌ์ฉ์์ ์๋ ฅ ์ ๋ณด๊ฐ url์ ๋ธ์ถ๋๋ค๋ ๋ฌธ์ ์   
get ์์ฒญ ๋ถ๋งํฌ ๊ฐ๋ฅ  
๋ธ๋ผ์ฐ์ ๋ง๋ค ๊ธธ์ด์ ์ ํ์ด ์์  
์๋ฒ์ ๋ฆฌ์์ค์์ ๋ฐ์ดํฐ๋ฅผ ์์ฒญํ  ๋ ์ฌ์ฉ (SELECT)  

2. post : HTTP request์ body์ ๋ด์์ ์ ์ก
url์ ๋ธ์ถ๋์ง ์์ ๋ณด์์ด ํ์ํ ๋ถ๋ถ์ ์ฌ์ฉ  
post ์์ฒญ ๋ถ๋งํฌ ๋ถ๊ฐ๋ฅ  
๋ฐ์ดํฐ ๊ธธ์ด์ ์ ํ ์์  
์๋ฒ์ ๋ฆฌ์์ค๋ฅผ ์๋ก ์์ฑํ๊ฑฐ๋ ์๋ฐ์ดํธํ  ๋ ์ฌ์ฉ (CREATE)

### Autocomplete
์๋ ฅํ๋ ๊ฐ์ ์ ์ฅํ์ฌ ์๋ ์์ฑํ๊ธฐ
```html
<form action="/action_page.php" autocomplete="on">
```

### Novalidate
์ ํจ์ฑ(์๋ ฅ๊ฐ์ ์ฌ๋ถ) ๊ฒ์ฌํ๊ธฐ  
์๋ต ์ ์ ํจ์ฑ ๊ฒ์ฌ ์์ด ์คํ
```html
<form action="/action_page.php" novalidate>
```

## Form์ ์์
### Input & Label
```html
<label for="fname">First name:</label>
<input type="text" id="fname" name="fname">
```

### Select
drop-down list ์์ฑํ๊ธฐ  
- selected
- size
- multiple
```html
<label for="cars">Choose a car:</label>
<select id="cars" name="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <!-- selected : default๋ก fiat ์ค์  -->
  <option value="fiat" selected>Fiat</option>
  <option value="audi">Audi</option>
</select>
```

### Textarea
์๋ ฅ ๊ฐ๋ฅํ ํ์คํธ ์์
```html
<textarea name="message" rows="10" cols="30">
The cat was playing in the garden.
</textarea>
```

### Button
```html
<!-- aler : ์๋ฆผ์ฐฝ ๋์ฐ๊ธฐ -->
<button type="button" onclick="alert('Hello World!')">Click Me!</button>
```

### Fieldset & Legend
`fieldset` : `form`์์ ๋ฐ์ดํฐ์ ๊ด๋ จ๋ ๊ทธ๋ฃน ๋ฌถ๊ธฐ (ํ๋๋ฆฌ ์์ ์์ฑ)  
`legend` : `fieldset`์ ํ์ 
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
์๋ ฅ ๊ฐ๋ฅํ๋ฉด์ ์ ํ์ง๊ฐ ์๋ ์๋ ฅ์ฐฝ ์์ฑ

```html
<form action="/action_page.php">
  <!-- list ์์ฑ์ ์ฐ๊ฒฐ์ํฌ datalist์ id๊ฐ ์๋ ฅ -->
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