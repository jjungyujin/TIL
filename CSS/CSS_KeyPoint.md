# 📎 01. Box Model
## margin과 padding
```
.p1 {
  // 요소 간의 여백
  //  top, right, bottom, left
  margin: 100px 10px 100px 10px;

  // 박스 테두리와 내용의 여백
  // top, right, bottom, left
  padding: 10px, 50px, 10px, 50px;
}
```
margin으로 가운데 정렬
```
.p1 {
  margin: 0 auto;
}
```

## width와 height
창의 크기가 변화에 따른 박스의 크기 변화 조절
```
.p1 {
  width: 1000px;
  height: 200px;

  // 최댓값과 최솟값 설정 - 창의 크기 변화에 따른 박스 크기의 변화를 조절
  min-width: 500px;
  min-height: 100px;
}
```

## overflow
- `: visible` : 넘치는 내용을 그대로 보여줌 (기본 설정)
- `: hidden` : 넘치는 내용을 숨김
- `: scroll` : 항상 스크롤바 생성
- `: auto` : 내용이 넘치는 경우에만 스크롤바 생성

## border
```
.p1 {
  // 테두리의 굵기(width), 선의 종류(style), 테두리의 색(color)
  border: 2px solid #4d9fff;
}
```
선의 종류
> solid(직선), dotted(점선), dashed(파선)

각 테두리마다 다른 설정 적용 가능
> border-top, bottom, left, right

테두리 없애기
> `border: none;` 또는 `border: 0;`

## 박스 꾸미기
- `border-radius` : 테두리 둥글게
- `background-color`: 배경색
- `box-shadow` : 그림자
```
.p1 {
  // 가로 위치, 세로 위치 - 양수 : 오른쪽, 아래 / 음수 : 왼쪽, 위
  box-shadow: 50px 30px;

  // 그림자 흐리게, 크기, 색 설정
  box-shadow: 50px 30px 50px 10px red;
}
```

## box-sizing
- `content-box;`  
`width`와 `height`가 실제 내용의 크기를 결정
실제 박스 크기는 (width/height) + padding + border  
- `border-box;` (모든 태그에 적용 권장)
전체 박스의 크기를 width와 height로 고정해줌

## 배경이미지 넣기
```
.div {
  background-image: url("이미지 파일명(상대경로 포함)");
  // cover : 사진의 비율을 유지, 박스를 꽉 채움
  background-size: cover;
  // position : 배경이미지의 위치(기준점) 설정
  // 사진이 잘리는 경우 기준점을 중점적으로 보여줌
  background-position: center center;
}
```

# 📎 02. CSS 제대로 활용하기
## 자식과 직속 자식
```
// 'div1' 클래스를 갖고 있는 요소의 자식 중 모든 <i> 태그
.div1 i {
  color: orange;
}

// 'div1' 클래스를 갖고 있는 요소의 직속 자식 중 모든 <i> 태그
.div1 > i {
  color: orange;
}
```

## 복수 선택
```
// 'two' 클래스를 가지고 있는 태그 모두와 'four' 클래스를 가지고 있는 태그 모두 선택
.two, .four {
  color: orange;
}
```

## 여러 조건
```
// 'outside' 클래스를 갖고 있으면서 'one' 클래스도 갖고 있는 태그
.outside.one {
  color: blue;
}
```

## Pseudo-class (가상 클래스)
콜론(:)으로 가상 클래스 선택

1. n번째 자식
```
// .div1의 자식인 <p> 태그 중 3번째
.div1 p:nth-child(3) {
  color: blue;
}
```

2. 마우스 오버 (hover)
```
// 마우스가 <h1> 태그에 올라갔을 때
h1:hover {
  color: green;
}
```

## CSS 상속
태그와 속성에 따라 부모 요소의 속성이 자식들에게 적용되기도 함  
> 상속되는 속성
color, font-family, font-size, list-style, text-align

위 속성들이 항상 상속되는 건 아님  
> 상속되지 않는 태그 : a