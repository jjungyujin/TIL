# Streamlit
해당 문서는 단순한 streamlit 기능을 설명하기 위한 목적으로 작성된 것이 아니며,  
실제 구현 과정에서 부딪혔던 난관과 해결법에 대해 정리한 것이다.  
다양한 API reference는 [공식 문서](https://docs.streamlit.io/library/api-reference)를 참고하면 된다.


## 반복 실행
streamlit은 화면에서 다음과 같은 것들이 업데이트되면 전체 streamlit 코드가 다시 실행된다.
- code가 수정되는 경우
- 사용자가 streamlit의 위젯과 상호작용하는 경우

매번 코드가 재실행되면 이벤트를 복합적으로 수행할 수 없다. 이를 해결하기 위해 개발된 것이 `session state`이다.

| 코드 예시
```python
import streamlit as st

# without session state
st.title('Counter example with session state')
count = 0

increment = st.button('Increment')
if increment:
    count += 1

# with session state
st.title('Counter example with session state')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1
```
- `session state`를 활용하지 않은 코드에서는 버튼을 아무리 눌러도 `count`가 1보다 커지지 않는다.
- 이는 코드가 재실행되면서 `count`가 계속 0으로 초기화되기 때문이다.
- `session state`를 활용한 코드에서 첫번째 if문으로 '코드가 재실행되면서 `count` 변수가 초기화되는 것'을 막을 수 있다.
- 이처럼 `session_state`는 코드가 재실행되더라도 이전 상태를 불러올 수 있도록 해주는 저장소 역할을 한다.

❗️ 간혹, streamlit을 실행하면 동시에 여러번 실행되면서 꼬이는 경우가 있다.  
🔑 streamlit은 열려있는 browser의 수만큼 실행되므로 이전에 띄워둔 streamlit 창이 남아있는지 확인한다.


## 재실행 없이 동적으로 element 수정하기
코드는 재실행되지 않는 상황에서 데이터가 변함에 따라 동적으로 화면을 띄우고 싶은 경우,  
한번 화면에 출력됐던 element는 사라지지 않아 출력할 때마다 element들이 쌓이게 된다.  

따라서 출력하기 전에 이전 element를 한번에 초기화하는 기능이 필요하다.  
예를 들어, LLMChain으로 생성한 5가지 선택지를 동적으로 출력하는 경우를 떠올리면 된다.  

이때 활용할 수 있는 게 `empty()`와 `container()`이다.

| 코드 예시
```python
import streamlit as st

# empty : single element container
placeholder = st.empty()

def show_option_list(option_list: list):
    placeholder.empty()

    # container : multi element container
    with placeholder.container():
        for i, option in enumerate(option_list):
            if i%3 == 0:
                st.info(option)
            elif i%3 == 1:
                st.success(option)
            elif i%3 == 2:
                st.error(option)
```
- `empty`에 하나의 `container`를 만들면, 여기에 여러 element(`info`, `success`, `error`)를 담을 수 있다.
- `empty`는 `empty()` 함수로 초기화시킬 수 있으며 `container`에 담긴 모든 출력을 한번에 초기화할 수 있다.