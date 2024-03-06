# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running ‘nixos-help’).

{ config, pkgs, ... }:

{
  imports =
    [ # Include the results of the hardware scan.
      ./hardware-configuration.nix
    ];

  # Enable Flakes
  nix.settings.experimental-features = ["nix-command" "flakes"];

  # Bootloader.
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;

  networking.hostName = "dmarshall-laptop"; # Define your hostname.
  # networking.wireless.enable = true;  # Enables wireless support via wpa_supplicant.

  # Configure network proxy if necessary
  # networking.proxy.default = "http://user:password@proxy:port/";
  # networking.proxy.noProxy = "127.0.0.1,localhost,internal.domain";

  # Enable networking
  networking.networkmanager.enable = true;

  # Set your time zone.
  time.timeZone = "America/New_York";

  # Select internationalisation properties.
  i18n.defaultLocale = "en_US.UTF-8";

  i18n.extraLocaleSettings = {
    LC_ADDRESS = "en_US.UTF-8";
    LC_IDENTIFICATION = "en_US.UTF-8";
    LC_MEASUREMENT = "en_US.UTF-8";
    LC_MONETARY = "en_US.UTF-8";
    LC_NAME = "en_US.UTF-8";
    LC_NUMERIC = "en_US.UTF-8";
    LC_PAPER = "en_US.UTF-8";
    LC_TELEPHONE = "en_US.UTF-8";
    LC_TIME = "en_US.UTF-8";
  };

  # Enable the X11 windowing system.
  services.xserver.enable = true;

  # Enable the GNOME Desktop Environment.
  services.xserver.displayManager.gdm.enable = true;
  services.xserver.desktopManager.gnome.enable = true;
  services.xserver.displayManager.gdm.wayland = true;

  # Configure keymap in X11
  services.xserver.xkb = {
    layout = "us";
    variant = "";
  };

  # Enable CUPS to print documents.
  services.printing.enable = true;

  # Enable sound with pipewire.
  sound.enable = true;
  hardware.pulseaudio.enable = false;
  security.rtkit.enable = true;
  services.pipewire = {
    enable = true;
    alsa.enable = true;
    alsa.support32Bit = true;
    pulse.enable = true;
    # If you want to use JACK applications, uncomment this
    jack.enable = true;

    # use the example session manager (no others are packaged yet so this is enabled by default,
    # no need to redefine it in your config for now)
    #media-session.enable = true;
  };

  # Enable touchpad support (enabled default in most desktopManager).
  # services.xserver.libinput.enable = true;

  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users.dmarshall = {
    isNormalUser = true;
    description = "Dakota Marshall";
    extraGroups = [ "networkmanager" "wheel" "docker" "uucp" "vboxusers" ];
    shell = pkgs.zsh;
    packages = with pkgs; [
      firefox
    ];
  };

  # Allow unfree packages
  nixpkgs.config.allowUnfree = true;

  
  # Yubikey Settings
  services.udev.packages = [ pkgs.yubikey-personalization ];
  programs.gnupg.agent = {
    enable = true;
    enableSSHSupport = true;
  };
  # Entries in /etc/pam.d
  # login should cover most things
  security.pam.services = {
    login.u2fAuth = true;
    sudo.u2fAuth = true;

  };
  security.pam.u2f = {
    enable = true;
    control = "sufficient";
    interactive = true;
    cue = true;

  };
  # Install and configure packages

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

  # Some programs need SUID wrappers, can be configured further or are
  # started in user sessions.
  # programs.mtr.enable =   systemd.user.services.syncthing.enable = true;
  # programs.gnupg.agent = {
  #   enable = true;
  #   enableSSHSupport = true;
  # };
 
  # List services that you want to enable:
  # Enable the OpenSSH daemon.
  services.openssh.enable = true;
  services.dbus.enable = true;
  services.syncthing = {

    enable = true;
    systemService = false;
    user = "dmarshall";
    group = "dmarshall";
    dataDir = "/home/dmarshall";

  };
  # XDG Portal settings for hyprland
  xdg.portal.enable = true;
  # pkgs.xdg-desktop-portal-gtk # this might need to get added back for when I am on hyprland, not GNOME
  xdg.portal.extraPortals = [  pkgs.xdg-desktop-portal-hyprland];
  # Open ports in the firewall.
  # networking.firewall.allowedTCPPorts = [ ... ];
  # networking.firewall.allowedUDPPorts = [ ... ];
  # Or disable the firewall altogether.
  # networking.firewall.enable = false;

  # This value determines the NixOS release from which the default
  # settings for stateful data, like file locations and database versions
  # on your system were taken. It‘s perfectly fine and recommended to leave
  # this value at the release version of the first install of this system.
  # Before changing this value read the documentation for this option
  # (e.g. man configuration.nix or on https://nixos.org/nixos/options.html).
  system.stateVersion = "23.11"; # Did you read the comment?

}
