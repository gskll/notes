- fish uses `fish_variables` file for universal variables
- useful to have this in git as has various plugin/script config vars
- some variables are secret / machine-specific
  - export globally in `~/.profile.fish` and source it in `config.fish`
  - `source $HOME/.profile.fish`
  - set -gx SECRET xxxx

fish shell reads variables in following order: local>global>universal
