{ config, pkgs, ...}:
{

  # Allow unfree packages
  nixpkgs.config.allowUnfree = true;

  programs.zsh = {
    enable = true;
    histSize = 10000;
    autosuggestions.enable = true;
    syntaxHighlighting.enable = true;
    ohMyZsh = {
      enable = true;
        theme = "steeef";
        plugins = [
          "git"
          "sudo"
        ];
    };
  };
  programs.steam.enable = true;
  programs.hyprland = {
    enable = true;
    xwayland.enable = true;
  };
  programs.git.enable = true;
  programs.neovim.enable = true;
  programs.waybar.enable = true;
  programs.dconf.enable = true;
  environment.systemPackages = [ gnome.adwaita-icon-theme ];
  services.udev.packages = with pkgs; [ gnome.gnome-settings-daemon ];
  # List packages installed in system profile. To search, run:
  # $ nix search wget
  environment.systemPackages = with pkgs; [
    ansible
    audacity
    bat
    blender
    blueman
    btop
    catppuccin-gtk
    clang
    cliphist
    distrobox
    docker
    fd
    fzf
    gamescope
    gnomeExtensions.appindicator
    go
    helmfile
    hyprpaper
    hyprshot
    kubernetes-helm
    libgcc
    libnotify
    libsForQt5.filelight
    libsForQt5.okular
    lutris
    mako
    nerdfonts
    networkmanagerapplet
    obs-studio
    openfortivpn
    openrgb
    openshot-qt
    picard
    pipewire
    polkit-kde-agent
    python3
    python311Packages.psutil
    python311Packages.pydbus
    qbittorrent
    quickemu
    quickgui
    remmina
    ripgrep
    steam-tui
    swayidle
    swaylock
    swaylock-effects
    swaynotificationcenter
    syncthing
    telegram-desktop
    terminator
    vlc
    wireplumber
    wireshark
    wl-clip-persist
    wofi
    xdg-desktop-portal-gtk
    xdg-desktop-portal-hyprland
    yt-dlp
    zoxide
  ];
 
}
