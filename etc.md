# 정보 암호화 - hashlib

비밀번호를 저장하고 관리할 때 유추나 복호화가 불가능하도록 해싱하여 저장해야 한다.  
`hashlib`은 MD5, SHA256등의 알고리즘으로 문자열을 해싱할 때 사용하는 모듈이다.  
> 해싱(hasing) : 원본 문자열을 알아볼 수 없는 난해한 문자열로 정의하는 방법

### 코드 예시  
```python
import hashlib

m = hashlib.sha256()
m.update('this is my password'.encode('utf-8'))
digest = m.hexdigest()
```
- `update` 함수는 바이트 문자열을 받으므로 `encode`를 이용하여 유니코드 문자열을 바이트 문자열로 변환한다.
- 동일한 문자에 대해서는 동일한 해시값을 얻는다.
- 해싱한 문자열은 복구할 수 없다.


# 설정 관리 - Hierarchical Yaml Config
### 디렉토리 구조
디렉토리 구조에 따라 config 파일도 hierarchy하게 관리할 수 있다.
```
conf
├── config.yaml
├── monster
├   ├── SLIM.yaml
├   └── WOLF.yaml
├── character
├   └── YUJIN.yaml
└── round
    └── base.yaml
gameroom
├── gameroom.py
└── gamemanager.py
character
└── base.py
monster
└── base.py
```

### config.yaml 코드 (예시)
- 기본적으로 dict 구조 (key, value)로 작성함
- `-`로 나열하면 리스트로 인지함
- 문자열 표기("")를 하지 않아도 알아서 문자열로 인지함

```yaml
  # hydra : 페이스북에서 머신러닝 실험 등 복잡한 어플리케이션을 구성하기 위해 사용하는 오픈소스 프레임워크
  # python class의 input/output type check 등을 도와줌
  hydra:
    job:
      # main 함수에 넘어가기 전에 os.chdir을 호출하여 working directory를 변경하도록 함
      chdir: True

  defaults:
    # dir_path@dict_name.key_name: yaml_file_name
    # dictionary 생성, Key에 (yaml file로 생성한) 객체를 value로 align
    - character@character.1: YUJIN
    - monster@monster.1: SLIM
    - monster@monster.2: WOLF
    - round: base
    - _self_

  # agenda(dictionary)에서 values를 받아옴
  monster_dict_list: ${oc.dict.values:monster} # oc : omega config

  gameroom:
    # _target_ : python code와 연결 (GameRoom : class name)
    _target_: gameroom.GameRoom
    _partial_: True
    game_manager:
      _target_: gameroom.GameManager
      parsing_num_k: 5

  plugin:
    - ChatPlugin

  plugin_path: ${cwd}/plugins

  llm_service:
    - OpenAI

  max_turn_per_monster: 4
  interface: cli # `cli` for client | `grpc` for server
  rest_port: 0000 # temporary
  debug: False

  character_list: ${oc.dict.values:character}
  skill_list:
    - SuperDagger
    - BasicShield
    - PowerArrow
  cwd: ${hydra:runtime.cwd}
```


# 예외 처리 - try and except / assert
try & except
- 개발자가 예상하지 못한 경우에 대해 예외 처리
- ex) LLM의 output 후처리 코드

assert
- 반드시 지켜야할 사항을 강제하기 위한 예외 처리
- ex) config 파일의 입력값 처리 코드