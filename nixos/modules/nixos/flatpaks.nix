{ config, pkgs, ...}:
{

  services.flatpak.enable = true;
  # https://github.com/gmodena/nix-flatpak
  services.flatpak.remotes = [
    {
        name = "flathub";
        location = "https://dl.flathub.org/repo/flathub.flatpakrepo";
    }
    {
        name = "JagexLauncher";
        location = "https://jagexlauncher.flatpak.mcswain.dev/JagexLauncher.flatpakrepo";
    }
  ];
  services.flatpak.update.auto = {
      enable = true;
      onCalendar = "weekly"; # default value
    };
  # Declare flatpaks to install
  # Requires flatpak flake source
  services.flatpak.packages = [
    "com.calibre_ebook.calibre"
    "com.feaneron.Boatswain"
    "com.github.tchx84.Flatseal"
    "com.mongodb.Compass"
    "com.plexamp.Plexamp"
    "com.adamcake.Bolt"
    "com.ultimaker.cura"
    "community.pathofbuilding.PathOfBuilding"
    "io.github.dgsasha.Remembrance"
    "md.obsidian.Obsidian"
    "net.davidotek.pupgui2"
    "org.chromium.Chromium"
    "org.expresslrs.ExpressLRSConfigurator"
    "org.freedesktop.Platform.Compat.i386/x86_64/23.08"
    "org.freedesktop.Platform.GL32.default/x86_64/23.08"
    "org.gnome.design.Emblem"
    "com.heroicgameslauncher.hgl"
    "org.kde.krita"
    "org.localsend.localsend_app"
    "org.rncbc.qpwgraph"
    "org.signal.Signal"
    "us.zoom.Zoom"
    "org.prismlauncher.PrismLauncher"
    "dev.vencord.Vesktop"
    "com.logseq.Logseq"
    "dev.deedles.Trayscale"
    "org.openshot.OpenShot"
    "org.shotcut.Shotcut"
    # Official Jagex Launcher, not needed because of Bolt
    { appId = "com.jagex.Launcher"; origin = "JagexLauncher"; }
    { appId = "com.jagex.Launcher.ThirdParty.RuneLite"; origin = "JagexLauncher"; }
  ];


}
