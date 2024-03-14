# Running multiple nvim configs

- create new config in a folder with a new name
- symlink this to $HOME/.config as with normal
  e.g. `ln -s ~/dotfiles/nvim-lazy/ ~/.config`
- can now run this version with the following
  `NVIM_APPNAME="nvim-lazy" nvim`
- add an zsh alias
  `alias nviml='NVIM_APPNAME="nvim-lazy" nvim'`
