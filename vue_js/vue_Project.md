## 01. 프로젝트 생성하기

### Vue 설치

터미널에서 아래 코드 실행

```terminal
// 가상환경 활성화
conda activate dssa

npm install vue
```

### Vue-cli 설치

프로젝트 생성을 돕는 vue 공식 CLI

```terminal
npm install -g @vue/cli
```

### 프로젝트 생성하기

```terminal
// 공식 템플릿으로 프로젝트 생성하기
// vue init webpack 생성할 프로젝트 이름
vue init webpack gemini-project
```

프로젝트 생성 시 터미널에 뜨는 질문에 enter 키 입력 시 기본값으로 설정됨

### 프로젝트 시작하기

```terminal
// 실행 환경 구축
npm install

// 실행
npm run dev
```

> chromedriver 설치 오류 (On a Mac with an M1 processor)

```terminal
npm ERR! Only Mac 64 bits supported.
```

아래 코드로 87.0.1 버전(혹은 더 상위 버전) 설치 후 환경 구축

```terminal
npm install chromedriver@87.0.1
```

## 02. 프로젝트 폴더 다루기

### html 관련 폴더

1. `src` > `components`  
   컴포넌트 파일(확장자 : `.vue`)을 담는 폴더  
   웹 페이지를 구성하는 블록을 컴포넌트 파일로 각각 작성

2. `src` > `router` > `page`  
   `components`에 담긴 컴포넌트의 조합을 통해 만든 웹 페이지 컴포넌트를 담는 폴더

3. `index.html`  
   최소한의 html 정보를 담는 파일

4. `src` > `App.vue`  
   모든 컴포넌트를 관리하는 또 하나의 컴포넌트
   해당 파일에서 `style.css` 연결 필요

```vue
<!-- 모든 라우터가 아래 view 태그에서 보여짐 -->
<template>
  <router-view />
</template>

<!-- 다른 파일에서 해당 파일을 import 하기 위해 필요한 코드 -->
<script>
export default {
  name: "App",
};
</script>

<!-- style.css와 연결되는 코드 -->
<style>
@import "../styles.css";
</style>
```

### css 관련 폴더

1. `style.css`  
   모든 html에 적용될 서식 파일

### js 관련 폴더

1. `src` > `router` > `index.js`  
   라우터(url 주소와 `page` 컴포넌트의 연결) 정보를 담는 파일

2. `main.js`  
   `index.html`의 인스턴스에 라우터(`router` > `index.js`)와 컴포넌트(`App.vue`) 등록

## 03. vue 파일 작성 관련 로직

1. `<template>` 태그 안의 html 코드는 하나의 태그로 묶여있어야 함
2. 마지막에 빈 줄이 추가되어 있어야 함
