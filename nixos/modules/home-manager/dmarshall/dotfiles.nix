{ config, pkgs, ... }:

{

  # Creates symlinks from the XDG config location (~/.config normally) to the specified source location
  # These must be full paths, or else they are copied into the Nix store and linked as read only
  xdg.configFile = {
    "obs-studio".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/obs-studio";
    "terminator".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/terminator";
    "hypr".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/hypr";
    "swayidle".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/swayidle";
    "waybar".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/waybar";
    "wofi".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/wofi";
    "swaync".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/swaync";
    "nvim".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/nvim";
    "Yubico".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/yubico";
    "OpenTabletDriver".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/OpenTabletDriver";
    "openfortivpn".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/openfortivpn";
    "blender".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/blender";
    "omp".source = config.lib.file.mkOutOfStoreSymlink "/home/dmarshall/gitlab/dakota.marshall/dotfiles/dotfiles/omp";
  };
}
