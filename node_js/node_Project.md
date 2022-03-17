# GEMINI PROJECT 기반 정리

## 01. 프로젝트 생성하기
### express-generator 설치
터미널에서 아래 코드 실행
```terminal
// node 설치 버전 확인
node

// 관리자 권한으로 generator 설치하기
sudo npm install -g express-generator

// generator로 프로젝터 폴더 생성하기
express backend
```

### 필요한 모듈 설치
- dotenv  
env 파일을 읽어들이기 위한 모듈

- cors  
frontend 서버가 backend 서버에 접속할 수 있도록 하기 위한 모듈

- moment  
datetime 설정을 위한 모듈

```terminal
// package.json에 지정된 모듈 설치
npm install

// 추가적으로 필요한 모듈 설치
npm install mysql --save
npm install dotenv
npm install cors
npm install moment
```

## 02. 프로젝트 폴더 다루기
### routes
url에 따른 connection 코드 파일을 담는 폴더

### app.js
설치한 모듈 중 사용할 모듈 선언  
`routes`와 해당 url 연결  
```js
var cors = require('cors');
var areaRouter = require('./routes/areaConcert');

app.use(cors());
app.use('/area', areaRouter);
```

### database
1. `config.js`  
`.env` 파일의 host, user, password, db 정보를 읽어오는 파일

2. `index.js`  
db와의 connection을 위한 함수  
연결 성공 시 connection을 callback

### .env
데이터베이서 정보를 담는 파일  
해당 파일은 보안 상의 이유로 github에 업로드 하지 않도록 함
```py
DB_HOST = localhost
DB_USER = root
DB_PASSWORD = *****
DB_NAME = GEMINI
```

### bin
1. `www`  
생성되는 서버의 정보를 담고 있음  
`npm run start`에 의해 실행될 파일

### .json 파일
1. `package.json`  
설치한 모듈 정보를 간략히 담고 있는 파일  
`script`에 설정된 명령어로 실행되는 코드 확인 가능
```json
"scripts": {
  "start": "node ./bin/www"
}
```
```terminal
npm run start
```

2. `package-lock.json`  
설치한 모듈 정보를 자세히 담고 있는 파일

## 03. 오류 다루기
1. MySQL 8.0 버전 이후 node와의 접속 관련 에러  

"Client does not support authentication protocol requested by server;"  
> 아래 SQL문 실행 후 재시도
```sql
-- password에 실제 암호 입력
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```
