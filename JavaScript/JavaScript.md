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

## 02. 브라우저와 자바스크립스
### 브라우저 객체
`window` : 전역객체 (Global Object)  
자바스크립트의 최상단에 존재하는 객체

### DOM
Document Object Model (문서 객체 모델)  
html 문서 내의 모든 태그들은 개별적인 객체로 다룰 수 있음
```
console.log(document); // 태그 형태로 반환
console.log(typeof document); // object
console.dir(document); // 객체 형태로 반한
```

### DOM 트리
DOM 트리 내의 객체 : `Node` 
- 태그를 표현하는 노드 : 요소 노드  
- 텍스트를 표현하는 노드 : 텍스트 노드  

계층 구조 (부모 노드 - 자식 노드, 형재 노드)
> `document - html - head, body`  

### DOM 트리 여행하기
> (html 코드)[]
```
const myTag = document.querySelector('#list-1');
console.log(myTag);

// 형제 요소 노드
console.log(myTag.previousElementSibling);
console.log(myTag.nextElementSibling);

// 부모 요소 노드
console.log(myTag.parentElement);

// 자식 요소 노드
console.log(myTag.children[1]);
console.log(myTag.firstElementChild);
console.log(myTag.lastElementChild);
```

### 요소 노드 주요 프로퍼티
1. innerHTML
요소 안의 html을 문자열로 리턴  
태그들 사이의 들여쓰기와 줄바꿈 포함  
요소 안의 html을 수정/추가할 때 사용
```
console.log(myTag.innerHTML);
myTag.innerHTML += '<li>Exotic</li>';
```

2. outerHTML
해당 요소를 포함한 전체의 html 코드를 리턴  
단, 요소에 새로운 html 요소를 할당하면 기존의 html 요소는 완전히 사라짐

3. textContent
요소 안의 내용 중 html 태그 부분을 제외한 부분 리턴  
```
myTag.textContent = 'new text';
```

### 요소 노드 추가하기
1. 요소 노드 만들기
```
const first = document.createElement('li');
```

2. 요소 노드 꾸미기
```
first.textContent = '처음';
```

3. 요소 노드 추가하기
```
// 자식 노드로 추가 : Node.prepend, append
// 형제 노드로 추가 : Node.before, after
tomorrow.prepend(first);
```

## 03. 이벤트 살펴보기
### 하나의 이벤트에 여러 개의 독립적인 핸들러 등록하기
```
let btn = document.querySelector('#myBtn');

function event1(){
  console.log('Hi codeit!');
}
function event2(){
  console.log('Hi again!');
}

// elem.addEventListener(event, handler);
btn.addEventListener('click', event1);
btn.addEventListener('click', event2);
```
> 핸들러 제거하기
```
btn.removeEventListener('click', event2);
```