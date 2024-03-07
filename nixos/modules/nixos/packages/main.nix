
{ config, pkgs, ...}:
{

  imports = [
    ./firefox/firefox.nix
  ]; 

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
  services.udev.packages = with pkgs; [ gnome.gnome-settings-daemon ];
  # List packages installed in system profile. To search, run:
  # $ nix search wget
  
  # Enable pam service for swaylock
  # https://github.com/NixOS/nixpkgs/issues/158025 
  security.pam.services.swaylock = {};

  environment.systemPackages = with pkgs; [
    ansible
    audacity
    bat
    blender
    blueman
    btop
    cargo
    catppuccin-gtk
    clang
    cliphist
    distrobox
    docker
    fd
    fzf
    gamescope
    gnome.adwaita-icon-theme
    gnomeExtensions.appindicator
    go
    helmfile
    hyprpaper
    hyprshot
    killall
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
    swaylock-effects
    swaynotificationcenter
    syncthing
    telegram-desktop
    terminator
    vlc
    waybar-mpris
    pika-backup
    wireplumber
    wireshark
    wl-clip-persist
    wl-clipboard
    wofi
    xdg-desktop-portal-gtk
    xdg-desktop-portal-hyprland
    yt-dlp
    zoxide
  ];
 
}
