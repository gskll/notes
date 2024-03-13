# Moving in netrw

- only works if the vim working directory is the same as the files you want to move
- can use `cd` commands to update
- `:cd %` will set the working directory to the current buffer (netrw)
- can also use `:cd %:h` from within a file to set the working directory to the directory containing that file
- should then be able to perform the move operations
- can then return to the previous working directory with `:cd! -`

- note: the difference between `:cd` and `:cd!` is that with the bang it affects the whole session, without only for current window
