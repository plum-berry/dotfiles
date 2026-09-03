#!/bin/bash
# wifi-menu.sh
selected=$(nmcli -f SSID dev wifi list | tail -n +2 | wofi --dmenu -p "Wi-Fi")
[ -n "$selected" ] && nmcli dev wifi connect "$selected"
