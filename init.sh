#!/bin/bash
coproc bluetoothctl
echo -e 'connect 01:AC:78:E6:3B:CD\ntrust 01:AC:78:E6:3B:CD\nexit' >&${COPROC[1]}
output=$(cat <&${COPROC[0]})
echo $output
