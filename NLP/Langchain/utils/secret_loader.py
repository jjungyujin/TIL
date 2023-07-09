import os
import json

# key_path: secret.json 파일이 있는 디렉토리 경로
def SecretLoader(name, key_path="C:/Users/jungyujin2/workspace/study/langchain"):
    with open(os.path.join(key_path, "secret.json"), "r") as f:
        secret = json.load(f)[name]
    return secret