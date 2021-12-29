# 01. Git 시작하기
## Git과 GitHub란 ?
> Git : 버전관리를 위한 도구  
> Github : 원격 저장소, 외부의 서버 제공

## Git과 GitHub를 왜 사용해야 할까 ?
1. 지난 과정 확인 가능  
2. 이전 버전으로 돌아갈 수 있음
3. 개발자간의 협업 가능
4. 다른 컴퓨터에 작업물 보내기

## Git의 역사
Git은 리눅스(Linux)라는 운영 체제를 만든 리누스 토발즈가 만들었다.

# 02. Git 써보기
## 레포지토리(repository)
git이 프로젝트 디렉토리의 변화 과정을 기록하는 곳  
프로젝트 디렉토리의 변화 과정을 기록하는 곳  
commit이 저장되는 곳  

**레포지토리 만들기**
```
mkdir (폴더명)
cd (폴더명)
git init
```

## 커밋(commit)
프로젝트 디렉토리의 특정 모습을 하나의 버전으로 저장  

**커밋하기**
1. 개발자의 정보 설정
```
git config user.name "(사용자명)"
git config user.email "(이메일 주소)"
```
2. 파일 add (tracked 상태로 만들기)
```
git add (파일명)
```
3. 커밋 메세지 남기기
```
git commit -m "(커밋메세지)"
```

## Git의 세가지 작업영역
**1. working directory**  
작업을 하는 프로젝트 디렉토리  

**2. staging area**
```git add```한 파일들이 존재하는 영역  
커밋을 하게 되면 이곳에 있는 파일들만 커밋에 반영  
단, 커밋을 한다고 해서 staging area에 있던 파일이 사라지는 것이 아니라 그냥 그대로 남아있다.

**3. repository**
working directory의 변경 이력들이 저장되어 있는 영역  

> working directory에서 작업을 하고
> 작업한 파일을 ```git add```하여 staging area로 올리고
> ```git commit```하여 repository에 저장

# 03. 커밋 다루기
## 커밋 히스토리 살펴보기
```
git log
git log --pretty=oneline
git show (커밋 해시)
```
> 긴 명령어에 alias 설정
> ```git config alias.history 'log  --pretty=oneline'```

## 최신 커밋 수정하기
```
git commit --amend
```
위 코드를 실행하면 최신 커밋에 대한 창이 뜬다.  
**i**를 누르면 입력 모드로 전환되어 메세지를 수정할 수 있고,  
**esc**를 누른 후 ```:wq```를 입력하면 수정이 완료된다.

## 두 커밋 간의 차이 보기
```git diff (앞선 커밋 해시) (이후 커밋 해시)```

## HEAD의 의미
어떤 커밋 하나(주로 최신 커밋)를 가리킴  
**HEAD가 가리키는 커밋에 따라 working directory 구성**

## 이전 커밋으로 git reset
```git reset --(옵션) (커밋 해시)```

**reset의 세가지 옵션**
1. ```--soft```
 레포지토리만 바뀜  
2. ```--mixed```
 레포지토리와 staging area만 바뀜(working directory만 남음)
3. ```--hard```
 세가지 영역 모두 바뀜  
 전부 예전으로 돌리고 싶을 때

 > 커밋 해시(아이디) 대신 ^ / ~n 사용
 > HEAD^ : HEAD의 바로 이전 커밋 의미
 > HEAD~2 : HEAD의 2단계 이전 커밋 의미

## 커밋에 tag 달기
```git tag (태그 이름) (커밋 해시)```
보통 프로젝트에서 주요 버전의 시작점이 되는 커밋에 태그 이용

**tag 조회**
```
git tag
git show (tag 이름)
```