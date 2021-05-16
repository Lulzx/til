# Purge Snap Apps

a small script to remove all snap apps

```
#! /bin/bash
snap_services=$(systemctl list-unit-file | grep snap|grep enabled|cut -d ' ' -f 1)
for snap_service in $snap_services; do
cmd="sudo systemctl disable $snap_service"
echo $cmd
$cmd
done
```
