{ config, pkgs, ...}:
{

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


}
