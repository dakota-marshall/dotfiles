{ config, pkgs, ...}:
{

  services.flatpak.enable = true;
  # https://github.com/gmodena/nix-flatpak
  # services.flatpak.update.auto = {
  #     enable = true;
  #     onCalendar = "weekly"; # Default value
  #   };
  # Declare flatpaks to install
  # Requires flatpak flake source
  services.flatpak.packages = [
    "com.calibre_ebook.calibre"
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
    "org.expresslrs.ExpressLRSConfigurator"
    "org.gnome.design.Emblem"
    "org.kde.krita"
    "org.rncbc.qpwgraph"
    "org.signal.Signal"
    "us.zoom.Zoom"
  ];


}
