# Git repositories 원격 저장소
  ## 1. Git repositories 연결
      git remote add origin <URL>
      git remote -v    # 연결된 URL 확인하기
  ## 2. CLONE
      git clone <URL>
      
  원격 저장소 전체를 복제(다운로드)
  - clone은 처음 받을 때 사용하는 것으로, 이후에는 pull 활용
  - clone으로 받은 프로젝트는 이미 git init 되어 있음.
  - clone 오류 ```fatal: could not create work tree dir 'test-25.01.16.': Invalid argument```
    > Git  repositories 이름 마지막을 점(.)으로 하지 말 것.<br/>
    > git 폴더가 있는 폴더에서 CLONE을 하면 되지 않음.<br/> git이 두 개가 하나의 폴더에 있으면 안 되기 때문에. ```cd ..```해서 CLONE 할 것.

 ## 3. PULL
     git pull origin master
 -  PULL 작동하지 않는 경우: 원격 저장소 변경사항이 없을 때, 즉, 로컬 저장소의 변경사항을 종전으로 되돌리고 싶을 때는 PULL이 아니라 git reset을 해야 함.

## 4. PUSH
    git push origin master   
    git switch dev    # branch를 바꾸는 명령어
- commit 이력이 없다면 push 할 수 없음. 
- origin은 “별명”. 다른 내용으로 바꿔도 된다! 관습적으로 origin 활용.
- master는 branch의 이름(dev, hello 등 다양하게 설정)
- PUSH 오류 ``` ! [rejected] master -> master (non-fast-forward) error: failed to push some refs to “” ```
  > git pull origin master --allow-unrelated-histories

## 5. RESET
    git reset <옵션> <커밋 값>
    ex. git reset --hard 61f6fe1
    
과거 특정 commit으로 되돌아가는 작업으로 해당 커밋 이후 커밋 삭제.
- a, b, c, d 커밋 중 a로 가면 b, c, d 삭제.
- 삭제되는 커밋의 기록을 어떤 영역에 남겨둘 것인지 옵션을 활용해 조정.
- 옵션
    > soft: 커밋 기록을 staging area(st 초록 부분)에 남김.<br/>
    > mixed: 커밋 기록을 working directory에 남김(기본 옵션).<br/>
    > hard: 커밋 기록을 남기지 않음. 

- 삭제한 commit 부활
    > git reflog    # 삭제된 commit 포함 모든 commit 조회<br/>
    > git log --oneline    # 현재 살아있는 commit 조회<br/>
    > git reset <옵션> <커밋 값>

## 6. REVERT
    git log --oneline    #1. 우선 커밋 리스트 확인
    git revert <커밋 harsh 값>    # 2. 특정 커밋 삭제
    git st
    git log --oneline    # 3. 커밋 삭제되었는지 확인

특정 commit을 없애는 것.
- a, b, c, d 중 b 없애면 b만 삭제.
- revert 취소 방법
    > commit이 살아있기 때문에 revert된 commit을 다시 revert하면 됨.
