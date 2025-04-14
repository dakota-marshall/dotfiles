
{ config, inputs, pkgs, lib, ...}:
{

  # imports = [
  #   ./firefox/firefox.nix
  # ]; 

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
  programs.adb.enable = true;
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
# Tailscale
  services.tailscale.enable = true;
# Teamspeak
  # services.teamspeak3 = {
  #   enable = true;
  # };
  programs.hyprland = {
    enable = true;
    xwayland.enable = true;
  };
  programs.git.enable = true;
  programs.neovim.enable = true;
  programs.waybar.enable = true;
  programs.dconf.enable = true;
  services.accounts-daemon.enable = true;
  services.udev.packages = with pkgs; [ gnome-settings-daemon ];
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
    airshipper
    ansible
    anki
    audacity
    bat 
    beets
    betaflight-configurator
    bitwarden-cli
    bitwarden-desktop
    bitwarden-menu
    blueman
    blockbench
    btop
    bruno
    cargo
    catppuccin-gtk
    clang
    # Package marked broken
    # cryptomator
    cliphist
    clonehero
    darktable
    distrobox
    docker
    fd
    ffmpeg-full
    fzf
    firefox
    gamescope
    gamemode
    adwaita-icon-theme
    gnomeExtensions.appindicator
    go
    go-swagger
    gimp
    # Build Failing
    # gyroflow
    helmfile
    # heroic
    hyprpaper
    hyprshot
    hyprcursor
    jq
    kcc
    # kdePackages.elisa
    killall
    kubectl
    kubernetes-helm
    kubectl 
    kubernetes-helmPlugins.helm-diff
    libgcc
    libnotify
    libsForQt5.filelight
    libsForQt5.okular
    libsForQt5.elisa
    kdePackages.qt6ct
    lutris
    mako
    nfs-utils
    nil
    networkmanagerapplet
    nodejs_22
    obs-studio
    openfortivpn
    openrgb
    # openshot-qt #https://github.com/NixOS/nixpkgs/issues/345314
    oh-my-posh
    pavucontrol
    picard
    piper
    pipewire
    kdePackages.polkit-kde-agent-1
    python3
    python311Packages.psutil
    python311Packages.pydbus
    qbittorrent
    qFlipper
    quickemu
    # quickgui # Build error
    r2modman
    remmina
    ripgrep
    runelite
    rhythmbox
    rclone
    lollypop
    librewolf
    amberol
    museeks
    sesh
    starsector
    swayidle
    swaylock-effects
    swaynotificationcenter
    syncthing
    strawberry
    talosctl
    teamspeak5_client
    teamspeak3
    telegram-desktop
    terminator
    thunderbird
    terraform
    xfce.thunar
    tenv
    tmux
    vlc
    sunshine
    pika-backup
    playerctl
    wireplumber
    wireshark
    clementine
    wine
    wine64
    winetricks
    wl-clip-persist
    wl-clipboard
    wofi
    xdg-desktop-portal-gtk
    xdg-desktop-portal-hyprland
    onlyoffice-desktopeditors
    yt-dlp
    zoxide
    umu-launcher
    steamtinkerlaunch
    # From wezterm github flake
    inputs.wezterm.packages.${pkgs.system}.default
    inputs.legends-viewer.packages.${pkgs.system}.default
    # (inputs.umu.packages.${pkgs.system}.umu.override {
    #     version = "${inputs.umu.shortRev}";
    # })
  ];
 
}
