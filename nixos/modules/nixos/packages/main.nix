
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
  programs.steam = {
    enable = true;
    # remotePlay.openFirewall = true;
    # dedicatedServer.openFirewall = true;
  };
  services.sunshine = {
    enable = true;
    capSysAdmin = true;
    autoStart = false;
    settings = {
        output_name = 1;

    };
    applications = {
        # env = {
        #     PATH = "$(PATH):$(HOME)/.local/bin";
        # };
        apps = [
          {
             name = "Steam";
             output = "steam.txt";
             detached = ["${pkgs.util-linux}/bin/setsid ${pkgs.steam}/bin/steam steam://open/bigpicture"];
             image-path = "steam.png";
          }
        ];
    };
  };
  programs.hyprland = {
    enable = true;
    xwayland.enable = true;
  };
  programs.git.enable = true;
  programs.neovim.enable = true;
  programs.waybar.enable = true;
  programs.dconf.enable = true;
  services.accounts-daemon.enable = true;
  services.udev.packages = with pkgs; [ gnome.gnome-settings-daemon ];
  # List packages installed in system profile. To search, run:
  # $ nix search wget
  
  # Enable pam service for swaylock
  # https://github.com/NixOS/nixpkgs/issues/158025 
  security.pam.services.swaylock = {};

  # Enable Docker
  virtualisation.docker.enable = true;

  # OpenTabletDriver
  hardware.opentabletdriver = {
  
    enable = true;
    daemon.enable = true;

  };

  environment.systemPackages = with pkgs; [
    ansible
    audacity
    bat 
    betaflight-configurator
    blueman
    btop
    bruno
    cargo
    catppuccin-gtk
    clang
    cryptomator
    cliphist
    darktable
    distrobox
    docker
    fd
    ffmpeg-full
    fzf
    gamescope
    gamemode
    gnome.adwaita-icon-theme
    gnomeExtensions.appindicator
    go
    go-swagger
    gimp
    gyroflow
    helmfile
    # heroic
    hyprpaper
    hyprshot
    jq
    kcc
    killall
    kubernetes-helm
    kubectl 
    kubernetes-helmPlugins.helm-diff
    libgcc
    libnotify
    libsForQt5.filelight
    libsForQt5.okular
    kdePackages.qt6ct
    lutris
    mako
    nfs-utils
    nerdfonts
    networkmanagerapplet
    nodejs_22
    obs-studio
    openfortivpn
    openrgb
    openshot-qt
    oh-my-posh
    pavucontrol
    picard
    piper
    pipewire
    pidgin
    polkit-kde-agent
    python3
    python311Packages.psutil
    python311Packages.pydbus
    qbittorrent
    qFlipper
    quickemu
    quickgui
    r2modman
    remmina
    ripgrep
    runelite
    sesh
    steam-tui
    swayidle
    swaylock-effects
    swaynotificationcenter
    syncthing
    talosctl
    telegram-desktop
    terminator
    terraform
    tenv
    tmux
    vlc
    sunshine
    pika-backup
    playerctl
    wireplumber
    wireshark
    wine
    winetricks
    wl-clip-persist
    wl-clipboard
    wofi
    xdg-desktop-portal-gtk
    xdg-desktop-portal-hyprland
    yt-dlp
    zoxide
    szyszka
  ];
 
}
