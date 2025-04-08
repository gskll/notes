## Inner workings

- git commands split between plumbing and porcelain
- porcelain commands are high level like `status`, `add`, `commit`
- plumbing commands are low level like `apply`, `commit-tree`, `hash-object`

- add git data is hidden in `.git` directory: branches, commits, tags and other objects
- all objects are stored in `.git/objects` - object database
- https://git-scm.com/book/en/v2/Git-Internals-Git-Objects
- can write to object database on commit or using `git hash-object`
- `hash-object` will by default give the hash that a file 'would' have used

  - can call `git hash-object -w` to actually write the object
  - expects either a file name or can pipe in from stdin with `--stdin` flag

- you can use `git cat-file` to inspect the elements of an object
- `git cat-file -p SHA` will figure out the object type and display it appropriately, or `-t` flag will return the object type
- object type `blob` is the raw content of a file tracked by git. not the filename or anything just the content

- also `tree` object type to store filenames and group. kind of like a directory
- each `tree` contains 1+ entries, each of which has the SHA of a blob or sub-tree, with the associated filename, mode and type

- also `commit` object
- format:

  1. top-level `tree` SHA for the snapshot of the project at that time
  2. the SHA of the parent `commit` if there is one
  3. the author/committer information and timestamp
  4. blank line
  5. commit message

- git stores an entire snapshot of files on a per-commit level
- there are some performance optimisations though to stop .git getting too large

  - files are compressed and packed to store more efficiently: https://git-scm.com/book/en/v2/Git-Internals-Packfiles
  - git deduplicates files that are the same across different commits - only stored once if it doesn't change between commits - will point to the same blob hash

## Branches

- branch is just a named pointer to a specific commit
- creating a branch is just creating a pointer to a specific commit
- the commit that the branch points to is the tip of the branch: stored in `.git/refs/heads`
- because it's just a pointer a branch is very lightweight and cheap
- HEAD is a reference to the branch (or commit) you're currently on

- branch_1 is pointing to commit H, main to D, branch_2 to F

```
       G - H branch_1
      /
A - B - C - D main
  \
   E - F branch_2
```

- new branch uses the current commit as the base

## Merge

- git creates a new commit that has both branches as histories - the commit has 2 parents
- will start from the 'merge base' commit or best common ancestor, and bring the changes from the target branch into the src
- then creates a new commit with these changes
- can run git log graph commands to inspect
- e.g. `git log --oneline --decorate --graph --parents` will show ascii graph with commit and parent hashes

- fast-forward merge is the simplest type of merge where no merge commit is created - we just move the base branch pointer to the feature branch
- can only happen when the feature branch has all the commits on the base branch

```
      C     delete_vscode
     /
A - B       main
```

- if we run `git merge delete_vscode` from branch `main`

```
            delete_vscode
A - B - C   main
```

## Rebase

- rebase vs merge

  - merge will preserve true history of a project - shows when/where branches were merged
    - but creates lots of merge commits which can make history harder to read/understand
  - rebase creates a linear history which is generally easier to understand

- never rebase a public branch onto another branch as this will mess it up

```
A - B - C    main
   \
    D - E    feature_branch
```

- if we're working on `feature_branch` and we want to bring the changes other team members have made on `main`
- we can `git rebase main` from `feature_branch` and it will move the `feature_branch` commits to the new `main` base

```
A - B - C         main
         \
          D - E   feature_branch
```

## Undoing changes

- `git reset --hard <hash>` will reset to hash and remove all changes - hash optional will default to HEAD
- `git reset --soft <hash>` will reset to hash commit and keep changes unstaged

## Remote

- git itself doesn't have a central repo - even though in practice we use github
- git remote can be any other git repo `git remote add <name> <uri>`
- the remote is called `origin` by convention if it's the source of truth

- `fetch` will download copies of the remote's `.git/objects` and some other info into your current repos `objects` dir
- will download the metadata but we don't have all the files
- can run `git log <remote>/<branch>` to inspect

- can then merge/rebase branches between local/remote repos same as within one repo
- `git push <remote> <branch>` sends local changes to any remote - `<remote>` defaults to origin if not specified

  - can push to a different remote branch `git push <localbranch>:<remotebranch>`
  - can also delete a remote branch by pushing an empty branch `git push :<remotebranch>`

- `git pull [<remote>/<branch>]` will fetch the actual file changes and not just the metadata like fetch

## Fork

- creates a copy of the original repo that you can modify without affecting the original
- not a feature of git itself but of git hosting services
- can create a PR from a fork branch to the original repo

## Reflog

- `git reflog` is like `git log` but logs the changes to a reference over time
- shows where HEAD was over time - can be used to recover lost commits
- can run `git cat-file -p SHA` with SHA from reflog
- then can use the `tree` hash to find `blob` hash and recover lost contents

- or easier you can just do `git merge HEAD@{1}`
- `git show SHA` will show the commit contents

## Merge conflict

- when two commits modify the same line and git can't automatically decide which change to keep
- resolve and commit

- The git checkout command can checkout the individual changes during a merge conflict using the --theirs or --ours flags.
- "ours" refers to the branch you are on, "theirs" refers to the branch being merged
- ours will overwrite the file with the changes from the branch you are currently on and merging into
- theirs will overwrite the file with the changes from the branch you are merging into the current branch

`git checkout --theirs path/to/file`

## Rebase conflicts

- can lose history in an unrecoverable way because edits history
- rebasing puts you in a detached HEAD state
- 'theirs' and 'ours' are flipped
- temporarily checkout rebase branch - ours are rebase branch changes, theirs are our changes
- once conflicts are resolved, add the changes but don't commit. `git rebase --continue`

- sometimes have to manually resolve the same conflicts over and over
- with long-running feature branch, or multiple branches being rebased onto main
- `git rerere` 'reuse recorded resolution' - git remembers how you resolved a hunk conflict so it can resolve it automatically
- applies to both rebasing and merging
- rerere cache is stored at `.git/rr-cache`
- `git config --local rerere.enabled true`

## Squashing commits

- `git rebase -i HEAD~n` where n is the number of commits you want to squash
- change `pick` to `squash` for all but the first commit
- we're telling git to replay all the changes from the current branch onto that commit
- squashing is destructive - changes are all there but the individual markers are gone

- if working on a copy of a branch, can delete the original and rename the temp using `git branch -m new-name`

- after squashing remote branch will be out of sync containing commits that are no longer in local
- force push

- common workflow to develop on feature branch making commits as you go
- then when ready to merge into main you squash all commits to make it look like one commit
- then push to remote

## Stash

- records the current state of your working directory and the index (staging area)
- reverts your working directory to HEAD
- can stash with a message `git stash -m`
- `git stash apply` keeps the stash in the list
- `git stash drop`
- `git stash apply stash@{2}`

## Revert

- an anti-commit, doesn't remove the commit like `git reset`
- creates a new commit that does the opposite of the reverted commit
- undoes the change but keeps a full history of the change and its undoing

## Diff

- `git diff` shows changes between working tree and last commit
- `git diff HEAD~1` shows changes between previous commit and current state, including last commit and working tree
- `git diff SHA_1 SHA_2` shows changes between two commits

- can run `git blame filename` to see who made changes

## Cherry pick

- when you don't want the changes from all commits, but just want a single commit from the branch
- `git cherry-pick SHA`

## Bisect

- how to find out when a change was introduced?
- `git bisect start`
- select a good commit where the bug wasn't present `git bisect good SHA`
- select a bad commit where the bug is present `git bisect bad SHA`
- git will checkout a commit between good and bad for you to test and see if bug is present
- execute `git bisect good` or `git bisect bad` to say the current commit is good or bad
- loop until bisect completes
- `git bisect reset`

- can also automate bisect by running a script that returns 0 if commit is good, or 1-127 if bad
- `git bisect run my_script arguments`

## Worktrees

- worktree or working directory is just the directory on your filesystem where the code you're tracking with git lives
- usually it's the root of your git repo (where .git/ is)
- contains tracked/untracked/modified files

- `git worktree` allows us to work with worktrees
- `git worktree list`
- allows you to work on different changes without stash/branch workflow
- main worktree - contains .git directory with the entire repo state - heavy
- linked worktree - contains .git file with path to main working tree - light (similar to branch) - can be complicated working with secrets and env variables

- `git worktree add <path> [<branch>]`
- works like any other repo - you can create/delete/switch branches - but you can't checkout a branch checked out by any other working tree (main or linked)

- references are stored in `.git/worktrees`
- a change in a linked worktree is automatically reflected in the main worktree
- you can almost think of a worktree as another branch in the repo but with it's own space on the filesystem

- cleanup with `git worktree remove <name>`
- can also delete the directory and run `git worktree prune`

## Tags

- tag is a name linked to a commit that doesn't move between commits, unlike a branch
- tags can be created/deleted but not modified
- list tags `git tag`
- create a tag on current commit `git tag -a "tag name" -m "tag message"`

- almost anywhere you can use a SHA you can use a tag name
- usually for releases

