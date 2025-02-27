
SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing
$ git init
Initialized empty Git repository in C:/Users/SSAFY/Desktop/git_undoing/.git/

SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing (master)
$ ls -alf
./  ../  .git/

SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing (master)
$ git commit -m "first"
[master (root-commit) e94921c] first
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md

SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing (master)
$ git st
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing (master)
$ git restore README.md


SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing (master)
$ git stash
Saved working directory and index state WIP on master: e94921c first

SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing (master)
$ git stash list
stash@{0}: WIP on master: e94921c first

SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing (master)
$ git stash pop
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (2c453b0e562b260cf0470ffc4d673556a06d1f1f)


SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing (master)
$ git restore --staged README.md

SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing (master)
$ git st
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")


SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing (master)
$ git restore README.md 

SSAFY@2□□223 MINGW64 ~/Desktop/git_undoing (master)
$ git st
On branch master
nothing to commit, working tree clean

