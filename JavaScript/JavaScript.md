# JavaScript
# 웹 개발을 위해 꼭 필요한 프로그래밍 언어

## 00. Intro
### html 파일과 연결 시키기
`body`태그가 닫히기 전 아래 코드 추가
```
<script src="파일명.js"></script>
```

### 출력 함수
```
console.log('출력할 내용');
```

### 변수 선언
```
let 변수명 = 변수값;
const 변수명 = 변수값;
```
let과 const의 차이점
> `let`은 변수에 재할당 가능  
> `const`는 변수 재선언, 재할당 불가능

### 함수 선언
```
fuction 함수 이름() {
  명령;
  명령;
};
```

### 작명 가이드
1. 식별자 : 문자, 밑줄(`_`), 달러 기호(`$`)로 시작
2. 대문자와 소문자 구분
3. 변수 이름은 `camelCase`로 표기

## 01. 인터랙티브 자바스크립트 시작하기
### id로 태그 선택하기
id : 하나의 태그에 부여하는 고유한 값  
해당 태그 내부에 있는 내용을 모두 불러옴  
없는 태그를 선택 시 `null` 반환
```
document.getElementById('id 값');

// 예시
const myNumberTag = document.getElementById('myNumber');
console.log(myNumberTag);
```

### class로 태그 선택하기
여러 태그를 동시에 선택할 때  
유사 배열(리스트) 형태로 태그들을 불러오며 인덱스로 접근 가능  
하나의 태그만 선택하더라도 인덱스 `[0]`으로 접근해야 함
없는 클래스 선택 시 `null`이 아닌 빈 배열 반환 
```
document.getElementsByClassName('class 이름');

// 예시
const myTags = document.getElementByClassName('color-btn');
console.log(myTags);
console.log(myTags[1]);
```

### css 선택자로 태그 선택하기
css Selector 문법 적용 : `.클래스 이름` 또는 `#id`  
최초 발견된 태그만 불러오려면 `document.querySelector`  
해당 태그 모두 불러오려면 `document.querySelectorAll`
```
document.querySelector('css 선택자');

// 예시
const myTag = document.querySelector('.color-btn');
console.log(myTag);
const myTags = document.querySelectorAll('.color-btn');
console.log(myTags);
```

### 이벤트와 버튼 클릭
버튼의 클릭 이벤트에 원하는 동작 실행 시키기 : 이벤트 핸들링  
구체적인 동작을 구현한 함수 : 이벤트 핸들러(이벤트 리스너)
```
const btn = document.querySelector('#myBtn');
btn.onclick = function() {
  console.log('Hello Codeit!');
}
```