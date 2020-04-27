# Setting Touchpad gestures on Ubuntu

> steps to follow:

```
sudo apt-get install libinput-tools xdotool
sudo gem install fusuma
mkdir ~/.config/fusuma && nano ~/.config/fusuma/config.yml
```

put the config in then file,

```
swipe:
  3: 
    left: 
      command: 'xdotool key alt+Right'
    right: 
      command: 'xdotool key alt+Left'
    up: 
      command: 'xdotool key super'
    down: 
      command: 'xdotool key super'
  4:
    left: 
      command: 'xdotool key ctrl+alt+Down'
    right: 
      command: 'xdotool key ctrl+alt+Up'
    up: 
      command: 'xdotool key ctrl+alt+Down'
    down: 
      command: 'xdotool key ctrl+alt+Up'
pinch:
  in:
    command: 'xdotool key ctrl+plus'
  out:
     command: 'xdotool key ctrl+minus'

threshold:
  swipe: 0.4
  pinch: 0.4

interval:
  swipe: 0.8
  pinch: 0.1
```

run using, `sudo fusuma`

Also, add to startup.

voila!

link: https://italolelis.com/posts/multitouch-gestures-ubuntu-fusuma/
