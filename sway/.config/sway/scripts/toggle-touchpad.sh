#!/bin/bash
DEVICE="type:touchpad"
STATE=$(swaymsg -t get_inputs | grep -A5 "Touchpad" | grep -oP '"libinput_send_events":\s*"\K[^"]+')

if swaymsg -t get_inputs | grep -q '"enabled": true'; then
    swaymsg input "$DEVICE" events disabled
    notify-send -u low -t 1500 "Touchpad" "Disabled"
else
    swaymsg input "$DEVICE" events enabled
    notify-send -u low -t 1500 "Touchpad" "Enabled"
fi
