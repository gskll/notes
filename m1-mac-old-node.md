M1 macs use different architecture (`arm64`) that's not supported on node version older than v16 (on mac)

You can install specifically on the older intel mac architecture using

`> arch -x86_64 asdf install nodejs 8.17.0`

can check computers architecture using

`> arch`
`uname -m`
`uname -a` <-- for more details
