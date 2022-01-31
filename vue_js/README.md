# Vue.js 

## 01. Vue.js 소개
### MVVM 모델에서의 Vue
MVVM 패턴의 뷰모델(ViewModel) 레이어에 해당하는 화면(View)단 라이브러리  
- `View` (DOM)  
- `View Model` (Vue)  
> 데이터 바인딩 : 데이터의 변화를 라이브러리에서 감지하여 화면(View)을 자동으로 보여줌  
> 돔 리스너 : 화면(View)에서 발생하는 이벤트를 감지하여 데이터를 변화시킴  

- `Moel` (Plain JavaScript Objects)

### 기존 웹 개발 방식 (HTML, Javascript)
새로운 값을 할당할 때마다 innerHTML을 재정의  
📎 [기존 웹 개발 코드](https://github.com/jjungyujin/TIL/blob/main/vue_js/inflearn_playground/web-dev.html)

### Reactivity 구현
데이터 바인딩을 위한 속성과 함수 정의
> 기본 문법
```
Object.defineProperty(대상 객체, 객체의 속성, {
  정의할 내용
})
```
📎 [Reactivity 코드](https://github.com/jjungyujin/TIL/blob/main/vue_js/inflearn_playground/vue-way.html)

## 02. 인스턴스
### 인스턴스 생성
인스턴스 : 뷰로 개발할 때 필수로 생성해야 하는 코드  
- 생성된 인스턴스는 변수에 담을 수 있음  
- Vue에서 기본적으로 제공하는 기능과 속성 사용 가능
```
var vm = new Vue();
```

### 인스턴스와 생성자 함수
생성자 함수 : 인스턴스를 생성하는 함수
> 예시 -  person 인스턴스 생성자 함수
```
// 생성자 함수명 : 알파벳 대문자로 시작
function Person(name, job) {
  this.name = name;
  this.job = job;
  this.logText = function() {
    console.log('hello');
  }
}

// 함수로 객체 생성
var p = new Person('josh', 'developer');

// 미리 정의된 함수 불러오기
p.logText();
```

### 인스턴스 옵션 속성
dictionary type으로 속성 정의
- `el` : 인스턴스가 그려지는 화면의 시작점 (특정 html태그)
- `data` : 뷰의 반응성(Reactivity)이 반영된 데이터의 속성

📎 [Vue 인스턴스 생성자 함수 코드](https://github.com/jjungyujin/TIL/blob/main/vue_js/inflearn_playground/instance.html)

## 03. 컴포넌트
### 컴포넌트 소개
컴포넌트 : 화면의 영역을 구분하여 개발할 수 있는 뷰의 기능

### 컴포넌트 등록 
전역 컴포넌트 등록
```
Vue.component('컴포넌트 이름', {컴포넌트 내용});
```

자역 컴포넌트 등록
```
<script>
  new Vue({
    el: '#app',
    components: {
      // '컴포넌트 이름', {컴포넌트 내용}
      'app-footer': {
          emplate: '<footer>footer</footer>'
      }
    }
  });
</script>
```
📎 [컴포넌트 등록 코드](https://github.com/jjungyujin/TIL/blob/main/vue_js/inflearn_playground/component.html) 

### 전역 컴포넌트와 지역 컴포넌트의 차이
지역 컴포넌트는 해당 인스턴스의 `components`에 어떤 컴포넌트들이 등록돼있는지 확인 가능  
(서비스를 구현할 때 대부분 지역 컴포넌트를 사용)  
서비스에서 전역으로 사용해야 하는 컴포넌트만 전역 컴포넌트로 등록  

### 컴포넌트와 인스턴스와의 관계
지역 컴포넌트는 자신이 속한 인스턴스에서만 사용 가능

## 04. 컴포넌트 통신 방법 - 기본
### 컴포넌트 통신 규칙
- props 속성 : 상위에서 하위로는 데이터를 내려줌  
- 이벤트 발생 : 하위에서 상위로는 이벤트를 올려줌

### props 속성
📎 [props 속성 코드](https://github.com/jjungyujin/TIL/blob/main/vue_js/inflearn_playground/props.html) 

### props 속성의 특징
상의 컴포넌트에서 data의 값이 바뀌면 props로 가져온 하위 컴포넌트의 값도 바뀜

### event emit
📎 [event emit 코드](https://github.com/jjungyujin/TIL/blob/main/vue_js/inflearn_playground/event-emit.html) 

## 05. 컴포넌트 통신 방법 - 응용
### 같은 컴포넌트 레벨 간의 통신 방법
상위 컴포넌트 Root
- 하위 컴포넌트 1. AppHeader
- 하위 컴포넌트 2. AppContent  

하위 컴포넌트에서 상위 컴포넌트로 데이터를 전달하고,  
다른 하위 컴포넌트가 상위 컴포넌트에서 props로 가져옴  
📎 [같은 레벨의 컴포넌트 통신 코드](https://github.com/jjungyujin/TIL/blob/main/vue_js/inflearn_playground/component-same-level.html)

## 06. 라우터
### 뷰 라우터 소개와 설치
뷰 라우터 : 뷰 라이브러리를 이용하여 페이지 이동을 구현할 때 사용하는 라이브러리
> CDN 방식 설치 : vue.js 불러오는 코드 아래에 router 추가 (순서 유의)
```
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>
```

### 뷰 라우터 등록 및 인스턴스 연결
라우터 인스턴스 생성
```
var router = new VueRouter({
  // 라우터 옵션
})
```
인스턴스 연결
```
new Vue({
      el: '#app',
      // 인스턴스의 router 속성에 연결할 VueRouter 지정
      router: router
    });
```

### routes 속성
routes : 페이지의 라우팅 정보를 배열로 담고 있음  
> 라우팅 정보 : 어떤 url로 이동했을 때 뿌려질 페이지의 정보
> 페이지의 갯수 만큼 배열 안에 객체가 필요함
```
var router = new VueRouter({
      routes: [
        // 객체 1. 로그인 페이지 정보
        {
          // 페이지의 url
          path: '/login',
          // 해당 url에서 표시될 컴포넌트
          // 각 페이지마다 뿌려질 컴포넌트는 무조건 1개
          component: LoginComponent
        },
        // 객체 2. 메인 페이지 정보
        {
          path: '/main',
          component: MainComponent
        }
      ]
    });
```

### router-view 태그와 router-link 태그
- router-view : url에 따른 컴포넌트가 뿌려질 영역  
- router-link : 사용자가 url 입력 없이 페이지를 이동할 수 있도록 하기 위한 링크 태그

📎 [라우터 정리 코드](https://github.com/jjungyujin/TIL/blob/main/vue_js/inflearn_playground/router.html)
