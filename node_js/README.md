# Node.js
[node.js 맥 설치 페이지](https://nodejs.org/en/)

## 01. Node.js의 주요 기능과 웹앱
### 웹서버 만들기
자바스크립트 파일을 실행하려면 콘솔에서 해당 파일이 있는 폴더로 이동 후 `node 파일명.js` 입력  
실행 페이지의 url은 `localhost:3000`로 접근
```
var http = require('http');
var app = http.createServer(function(request, response){
  var template = '<title> hi </title>'
  response.writeHead(200);
  response.end(template);
});

// 3000번 포트에 node.js 웹 서버를 실행시킴
app.listen(3000);

```

### Template Literal
```
var name = 'inflearn'
var letter = `Dear ${name}

HI, ${name}. I'm learning node.js.`
```

### URL의 이해
```
// (protocal)://(host):(port)/(path)?(query string)
http://opentutorials.org:3000/main?id=HTML&page=12
```
1. protocal - `http`  
웹 브라우저와 웹 서버가 서로 데이터를 주고 받기 위해서 만든 통신 규칙
2. domain name(host)  
인터넷에 접속해있는 각각의 컴퓨터
3. port 번호  
한 대의 컴퓨터 안에 여러 대의 서버 중 어떤 서버와 접속할 지 지정
4. path  
어떤 디렉토리의 어떤 파일인지 명시
5. query string  
시작은 물음표로 하기로 약속
원하는 데이터를 불러오기 위한 부분

### URL을 통해서 입력된 값 사용하기
`parse`를 이용해 url을 나누고 원하는 부분 추출  
조건문에서 추출한 정보 활용
```
var url = require('url');

var queryData = url.parse(_url, true).query;
var pathname = url.parse(_url,true).pathname;
```

### 동적인 웹페이지 만들기
url 주소에 따라 특정 html 코드를 바꾸려면 `${}` 이용
> html 템플릿를 생성하는 함수 
```
function templateHTML(title, list, body){
  return `
  <!doctype html>
  <html>
  <head>
    <title>${title}</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1><a href="/">WEB</a></h1>
    ${list}
    ${body}
  </body>
  </html>  
  `;
}
```

### body : 파일을 이용해 본문 구현
각 페이지마다 달라지는 본문의 html코드는 독립적인 파일로 저장 (확장자 없음)  
📎 [본문 파일 예시 폴더](https://github.com/jjungyujin/TIL/blob/main/node_js/data)

### body : 파일 읽기
`readFile` : 파일 내용 읽기
```
fs.readFile('상대 경로 포함 파일명', function(err, data){
  // 파일을 읽고 난 후 실행할 코드, 파일 내용은 data에 받아옴
  console.log(data);
});
```

### list : Node.js의 파일 목록 알아내기
위에서 생성한 함수의 매개변수에 원하는 값을 넣어주기 위한 과정  
`readdir` : 폴더에 있는 파일명 읽기  

```
var fs = require('fs');

fs.readdir('./data', function(err, filelist){
  console.log(filelist);
})
```

### list : 함수를 이용해 정리하기
> 파일 목록을 읽어 목차 html을 생성하는 함수
```
function templateList(filelist){
  var list = '<ul>';
  var i = 0;
  while (i < filelist.length){
    list = list +`<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
    i = i + 1;
  }
  list = list + `</ul>`;
  return list
}
```

### templateHTML : 홈페이지와 Not found 구현
```
if(pathname === '/'){

  // id를 입력 받았을 때
  if(queryData.id !== undefined){
    // data 폴더에 있는 파일 리스트 가져오기
    fs.readdir('./data', function(err, filelist){
      // url에 입력 받은 id와 일치하는 파일 읽기
      fs.readFile(`data/${queryData.id}`,"utf-8", function(err, description){
        
        var title = queryData.id;
        // 폴더에 있는 파일 리스트를 html로 만들기
        var list = templateList(filelist);

        // tamplateHTML로 최종 페이지 구현
        var template = templateHTML(title, list, `<h2>${title}</h2><p>${description}</p>`);

        response.writeHead(200);
        response.end(template);
        });
    });
  }
}

// pathname이 `/`로 시작하지 않으면 비정상적인 루트이므로 오류 페이지 보여주기
else {
  response.writeHead(404);
  response.end('Not found');
}
```

📎 [최종 코드](https://github.com/jjungyujin/TIL/blob/main/node_js/main.js)