#!/bin/bash

swayidle -w \
timeout 400 'bash /home/dmarshall/.config/hypr/lock.sh' \ 
timeout 800 'hyprctl dispatch dpms off' \
timeout 3600 'systemctl suspend' \
resume 'hyprctl dispatch dpms on' \
before-sleep 'bash /home/dmarshall/.config/hypr/lock.sh'