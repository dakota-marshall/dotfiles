#!/usr/bin/env bash
# /* ---- 💫 https://github.com/JaKooLit 💫 ---- */  ##
# searchable enabled keybinds using rofi

# kill yad to not interfere with this binds
# pkill yad || true

# check if rofi is already running
if pidof wofi > /dev/null; then
  pkill wofi
fi

# define the config files
keybinds_conf="$HOME/.config/hypr/keybinds.conf"
# user_keybinds_conf="$HOME/.config/hypr/UserConfigs/UserKeybinds.conf"
laptop_conf="$HOME/.config/hypr/UserConfigs/Laptops.conf"
wofi_theme="$HOME/.config/wofi/config"
msg='☣️ NOTE ☣️: Clicking with Mouse or Pressing ENTER will have NO function'

# combine the contents of the keybinds files and filter for keybinds
keybinds=$(cat "$keybinds_conf" | grep -E '^bind')

# check if laptop.conf exists and add its keybinds if present
if [[ -f "$laptop_conf" ]]; then
    laptop_binds=$(grep -E '^bind' "$laptop_conf")
    keybinds+=$'\n'"$laptop_binds"
fi

# check for any keybinds to display
if [[ -z "$keybinds" ]]; then
    echo "no keybinds found."
    exit 1
fi

# replace $mainmod with super in the displayed keybinds for rofi
display_keybinds=$(echo "$keybinds" | sed 's/\$mainMod/SUPER/g')

# use rofi to display the keybinds with the modified content
echo "$display_keybinds" | wofi --dmenu -i --prompt "$msg" --style "$HOME/.config/wofi/style.css" --conf "$HOME/.config/hypr/scripts/woficonfig" --width 1500 --height 1000
