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
