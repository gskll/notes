currently main plugin doesn't work so have to use branch with fix on it

- issue: https://github.com/nvim-treesitter/nvim-treesitter-angular/issues/3
- fix: https://github.com/elgiano/nvim-treesitter-angular/tree/topic/jsx-fix

steps to get it working:

1. add to packer and install/sync
2. :TSInstallFromGrammar angular -- necessary to fix the ABI version mismatch

can get the same error if run :TSUpdate
if that happens need to completely uninstall it: - remove from packer - remove from treesitter - reinstall in packer - _:TSInstallFromGrammar_
