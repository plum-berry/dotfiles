#!/bin/bash
choice=$(printf "Mute\n25%%\n50%%\n75%%\n100%%\nOpen pavucontrol" | wofi --dmenu -p "Volume")
case "$choice" in
    Mute) pactl set-sink-mute @DEFAULT_SINK@ toggle ;;
    25%) pactl set-sink-volume @DEFAULT_SINK@ 25% ;;
    50%) pactl set-sink-volume @DEFAULT_SINK@ 50% ;;
    75%) pactl set-sink-volume @DEFAULT_SINK@ 75% ;;
    100%) pactl set-sink-volume @DEFAULT_SINK@ 100% ;;
    "Open pavucontrol") pavucontrol & ;;
esac
