# VS code Debug
## start
create launch.json file
- name : debug 이름
- program : 실행시킬 file path

> default file
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```

## add setting
- cwd : 파일을 실행할 위치 (default : 현재 디렉토리)
  - 실행되는 디렉토리 경로를 변경해야 할 때 추가
- PYTHONPATH : python의 기본 경로 설정 
  - 하위 디렉토리의 파일을 찾지 못하는 import error 해결 가능
  - ⭐️ cwd에 설정한 경로에 대한 상대 경로로 입력

> example
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "gemini",
            "type": "python",
            "request": "launch",
            "program": "main.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "cwd": "/Users/jungyujin/workspace/project/teamlab/gemini",
            "env": {
                "PYTHONPATH": "./"
            }
        }
    ]
}
```