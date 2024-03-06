{ config, pkgs, ...}:
{
  
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

  services.flatpak.enable = true;
  # https://github.com/gmodena/nix-flatpak
  # services.flatpak.update.auto = {
  #     enable = true;
  #     onCalendar = "weekly"; # Default value
  #   };
  # Declare flatpaks to install
  services.flatpak.packages = [
    "com.discordapp.Discord"
    "com.feaneron.Boatswain"
    "com.github.tchx84.Flatseal"
    "com.jagex.RuneScape"
    "com.mongodb.Compass"
    "com.plexamp.Plexamp"
    "com.ultimaker.cura"
    "de.shorsh.discord-screenaudio"
    "md.obsidian.Obsidian"
    "net.davidotek.pupgui2"
    "org.chromium.Chromium"
    "org.kde.krita"
    "org.signal.Signal"
    "us.zoom.Zoom"
  ];

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
