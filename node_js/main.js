var http = require('http');
var fs = require('fs');
var url = require('url');

// html 코드를 생성하는 함수
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

// readdir로 목록을 가져와 리스트 html 코드를 생성하는 함수
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

var app = http.createServer(function(request, response){
  var _url = request.url; 
  // url 정보를 가져오는 부분
  var queryData = url.parse(_url, true).query;
  var pathname = url.parse(_url,true).pathname; 
  console.log(url.parse(_url, true));

  // 정상적인 루트
  if(pathname === '/'){
    // id가 없는 홈 화면일 때
    if(queryData.id === undefined){
      fs.readdir('./data', function(err, filelist){
      console.log(filelist);

      var title = 'Home';
      var description = 'Hello, world !';
      var list = templateList(filelist);

      var template = templateHTML(title, list, `<h2>${title}</h2><p>${description}</p>`);
      response.writeHead(200);
      response.end(template); //해당 내용을 웹에서 실행
      })
    } 

    // 목차에 있는 링크로 갔을 때
    else { 
      // 디렉토리에 있는 파일명(확장자 포함)을 filelist에 가져옴
      fs.readdir('./data', function(err, filelist){
        console.log(filelist);
        // url의 queryData.id에 입력한 값을 data 폴더에서 찾음
        // 찾은 파일의 내용을 description에 가져옴
        fs.readFile(`data/${queryData.id}`,"utf-8", function(err, description){
          
          var title = queryData.id;
          var list = templateList(filelist);

          var template = templateHTML(title, list, `<h2>${title}</h2><p>${description}</p>`);
          response.writeHead(200);
          response.end(template);
          });
      });
    }
  }
  // 비정상적인 루트
  else {
    response.writeHead(404);
    response.end('Not found');
  }
});

// 3000번 포트에 node.js 웹 서버를 실행시킴
app.listen(3000);
