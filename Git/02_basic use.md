## 1. 현황 파악
    git status
    현재 저장소의 파일 상태 보기
    
    git st
    git config --global alias.st 'status'
    status = st로 짧게 해서 자주 확인하기
    
    git config --global -l
    git global 설정 정보 보기

## 2. Working Directory > Staging Area '스테이지 올리기'
    git add <file_name>
    git add <file_name> <file_name> <file_name>
    여러 파일은 한 칸 띄고 쓰기
    
    git add -A
    모든 변경 및 추가 사항 스테이지 올리기

## 3. Staging Area > Repository '커밋하기'
    git config –global user.email “메일 주소”
    git config –global user.name “유저 네임”
    사용자 설정하기

    git commit -m <커밋명>
    커밋하기
    git commit <커밋명> 하지 않도록 유의!
    
    git log
    git log --oneline
    커밋 히스토리 보기

## 4. 바로 직전 생성한 commit 수정
    git commit --amend
    
    i = 텍스트 입력하기
    Esc - 텍스트 입력 후 나가기
    :wq = 저장 후 나가기
