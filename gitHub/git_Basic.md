# 📎 01. Git 시작하기
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

# 📎 02. Git 써보기
## 레포지토리(repository)
> git이 프로젝트 디렉토리의 변화 과정을 기록하는 곳  
> 프로젝트 디렉토리의 변화 과정을 기록하는 곳  
> commit이 저장되는 곳  

```terminal
mkdir (폴더명)
cd (폴더명)
git init
```

## 커밋(commit)
프로젝트 디렉토리의 특정 모습을 하나의 버전으로 저장  

1. 개발자의 정보 설정
```terminal
git config user.name "(사용자명)"
git config user.email "(이메일 주소)"
```
2. 파일 add (tracked 상태로 만들기)
```terminal
git add (파일명)
```
3. 커밋 메세지 남기기
```terminal
git commit -m "(커밋메세지)"
```

## Git의 세가지 작업영역
1. working directory  
작업을 하는 프로젝트 디렉토리  

2. staging area  
```git add```한 파일들이 존재하는 영역  
커밋을 하게 되면 이곳에 있는 파일들만 커밋에 반영  
단, 커밋을 한다고 해서 staging area에 있던 파일이 사라지는 것이 아니라 그냥 그대로 남아있다.

3. repository  
working directory의 변경 이력들이 저장되어 있는 영역  

working directory에서 작업을 하고, 작업한 파일을 ```git add```하여 staging area로 올리고. ```git commit```하여 repository에 저장  

## HEAD의 의미
어떤 커밋 하나(주로 최신 커밋)를 가리킴  
HEAD가 가리키는 커밋에 따라 working directory 구성

# 📎 03. GitHub 시작하기
## Push와 Pull
로컬 레포지토리를 리모트 레포지토리와 연결
```terminal
git remote add origin (리모트 레포지토리의 주소)
```

push 하기  
> 처음 push를 할 때에만  `-u origin master` 옵션을 사용하고 이후에는 `git push`로 변경사항 반영
```terminal
git push -u origin master
```

pull 하기
```terminal
git pull
```

## README.md
GitHub의 레포지토리에서는 README.md를 화면에 보여주도록 설정되어 있다.  
주로 프로젝트의 목차나 핵심 내용을 작성해두면 된다.

# 📎 04. 커밋 다루기
## 커밋 히스토리 살펴보기
```terminal
git log
git log --pretty=oneline
git show (커밋 해시)
```
긴 명령어에 alias 설정  
```terminal
git config alias.history 'log  --pretty=oneline'
```

## 최신 커밋 수정하기
```terminal
git commit --amend
```
위 코드를 실행하면 최신 커밋에 대한 창이 뜬다.  
> **i**를 누르면 입력 모드로 전환되어 메세지를 수정할 수 있고,  
**esc**를 누른 후 ```:wq```를 입력하면 수정이 완료된다.

## 두 커밋 간의 차이 보기
```terminal
git diff (앞선 커밋 해시) (이후 커밋 해시)
```

## 이전 커밋으로 git reset
```terminal
git reset --(옵션) (커밋 해시)
```

reset의 세가지 옵션
1. ```--soft```  
 레포지토리만 바뀜  
2. ```--mixed```  
 레포지토리와 staging area만 바뀜(working directory만 남음)
3. ```--hard```  
 세가지 영역 모두 바뀜  
 전부 예전으로 돌리고 싶을 때

 > 커밋 해시(아이디) 대신 ^ 또는 ~n 사용  
 > `HEAD^` : HEAD의 바로 이전 커밋 의미  
 > `HEAD~2` : HEAD의 2단계 이전 커밋 의미

## 커밋에 tag 달기
보통 프로젝트에서 주요 버전의 시작점이 되는 커밋에 태그 이용
```terminal
git tag (태그 이름) (커밋 해시)
```  

tag 조회
```terminal
git tag
git show (tag 이름)
```

# 📎 05. GitHub 협업하기
## 프로젝트 레포지토리 복사하기
github의 프로젝트 레포지토리에서 `fork`를 누르면 내 github 레포지토리에 복사가 된다.  
터미널에서 내가 원하는 디렉토리로 이동하고 아래와 같은 코드를 실행하면 working directory가 생성된다.
```terminal
git clone (내 리모트 레포지토리의 GitHub 상 주소)
```

## branch 따기
협업을 위해 생성된 프로젝트 레포지토리는 작업자들이 `fork`한 후 각자 작업하여 프로젝트 레포지토리에 PR을 요청한다.  
fork한 레포지토리에서 작업하기 전 branch를 생성하여 각 기능마다 따로 작업한다.
> main - develope - feature#1 / feature#2 / feature#3  

내 main branch는 PR이 반영된 프로젝트 레포지토리의 main을 pull해올 때만 사용한다.

## PR 하기 전 여러개의 commit 합치기
아래 코드는 HEAD부터 최근 3개의 커밋을 합치는 코드이다.
```terminal
git rebase -i HEAD~3
```
위 코드를 실행하면 해당 선택한 커밋들에 대한 창이 뜬다.  
> 입력 모드로 전환 : **i**  
가장 상단에 있던 커밋은 `pick`으로, 나머지는 `s`로 설정  

설정창을 닫으면 커밋 메세지에 대한 창이 뜬다.  
> 입력 모드에서 rebase 커밋에 대한 메세지를 작성하고 입력 모드를 닫기

## 강제로 push하기
리모트 레포지토리의 commit을 로컬 레포지토리의 commit이 포함하고 있지 않으면 push 작업에 오류가 발생한다.  
이런 경우 `-f` 옵션을 통해 강제로 `push`할 수 있다.
```terminal
git push -f
```

## 프로젝트 레포지토리 main을 내 main으로 가져오기
프로젝트 레포지토리 main을 pull 해오려면 내 로컬 레포지토리의 remote에 추가해주어야 한다.
```terminal
git remote add teamlab (프로젝트 레포지토리 주소)
git pull teamlab main
git push
```
> remote 확인하기 : `git  remote -v`  
내 리모트 레포지토리는 `origin`, 프로젝트 레포지토리는 `teamlab`으로 설정되어 있을 것이다.
