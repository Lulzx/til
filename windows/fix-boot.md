# Unable to boot windows?

_If windows gets fucked, put these commands in grub rescue_

```
insmod part_gpt
insmod chain
set root=(hd0,gpt1)
chainloader /EFI/Microsoft/Boot/bootmgfw.efi
boot
```
