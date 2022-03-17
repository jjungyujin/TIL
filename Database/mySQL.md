# MySQL

## 01. 데이터베이스 기본 설정
### MySQL 설치
macOS ~ , DMG Archive라고 쓰인 곳의 Download 버튼을 누르기  
가장 처음에 root라는 사용자가 기본으로 설정됨  
root 사용자로 서버에 접속하면 되는데, 이때 사용할 비밀번호 입력 (앞으로 db 접속 시 필요)  
[MySQL 설치 페이지](https://dev.mysql.com/downloads/mysql/)

### MySQL Workbench 설치
macOS 버전에 따라 사용 가능한 Workbench의 버전이 다름  
아래 링크에서 8.0.22 버전 설치  
[MySQL Workbench 설치 페이지](https://downloads.mysql.com/archives/workbench/)

### MySQL 서버 실행하기
맥의 시스템 환경설정 > MySQL 아이콘 > Start MySQL Server  
Workbench에서 Connection 접속

### 데이터베이스 생성하기
```sql
CREATE DATABASE gemini
```

## 02. 테이블 생성하기
### CSV 파일로 테이블 생성하기
1. 데이터베이스 이름에 커서를 대고 오른쪽 마우스 버튼 > Table Data Import Wizard
2. 테이블 이름 설정 후 스패너 모양 아이콘을 클릭
3. Field Separator(컬럼 구분자) 부분의 기호를 ,(콤마) 표시로 바꾸기

> csv 파일의 열 이름 영문화, 한글 인코딩 설정 후 테이블 생성 가능