# Dotfiles

These are all my dotfiles and my NixOS config. 

- NixOS config is obciously in `nixos/`
- Currently using [dotbot](https://github.com/anishathalye/dotbot) to symlink dotfiles out (Will likely be switching over to NixOS home-manager eventually)

These files are *not* generalized, so they probably will only work for me.

## Install

### Dotfiles

Symlinked just using the `./install` script

### Nix Config

Conifg is configured using flakes, so you can apply the config as follows:

```bash
sudo nixos-rebuild switch --flake nixos/.#default
```

## Needed packages

### NixOS

All my packages are defines in `nixos/modules/nixos/packages.nix`

### Arch

I dont use Arch anymore so this list will likely be out of date

```bash
yay -S zsh zoxide fzf hyprland terminator \
swaync waybar wofi swaylock swayidle pipewire \
wireplumber xdg-desktop-portal-hyprland \
xdg-desktop-portal-gtk polkit-kde-agent \
hyprpaper cliphist wl-clip-persist \
nerd-fonts hyprshot swaylock-effects \
mako python-psutil python-pydbus \
network-manager-applet blueman \
catppuccin-gtk-theme-mocha \
ripgrep fd
```
