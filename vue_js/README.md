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
[기존 웹 개발 코드](https://github.com/jjungyujin/TIL/blob/main/vue_js/inflearn_playground/web-dev.html)

### Reactivity 구현
데이터 바인딩을 위한 속성과 함수 정의
> 기본 문법
```
Object.defineProperty(대상 객체, 객체의 속성, {
  정의할 내용
})
```
[Reactivity 코드](https://github.com/jjungyujin/TIL/blob/main/vue_js/inflearn_playground/vue-way.html)

## 02. 인스턴스