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
    "com.adamcake.Bolt"
    "com.calibre_ebook.calibre"
    "com.feaneron.Boatswain"
    "com.github.tchx84.Flatseal"
    "com.heroicgameslauncher.hgl"
    "com.logseq.Logseq"
    "com.mongodb.Compass"
    "community.pathofbuilding.PathOfBuilding"
    "com.plexamp.Plexamp"
    "com.ultimaker.cura"
    "com.usebottles.bottles"
    "dev.deedles.Trayscale"
    "dev.vencord.Vesktop"
    "io.github.dgsasha.Remembrance"
    "io.mpv.Mpv"
    "md.obsidian.Obsidian"
    "net.davidotek.pupgui2"
    "net.waterfox.waterfox"
    "org.chromium.Chromium"
    "org.expresslrs.ExpressLRSConfigurator"
    "org.freedesktop.Platform.Compat.i386/x86_64/23.08"
    "org.freedesktop.Platform.GL32.default/x86_64/23.08"
    "org.gnome.design.Emblem"
    "org.kde.krita"
    "org.localsend.localsend_app"
    "org.openshot.OpenShot"
    "org.prismlauncher.PrismLauncher"
    "org.rncbc.qpwgraph"
    "org.shotcut.Shotcut"
    "org.signal.Signal"
    "org.strawberrymusicplayer.strawberry"
    "us.zoom.Zoom"
    # Official Jagex Launcher, not needed because of Bolt
    { appId = "com.jagex.Launcher"; origin = "JagexLauncher"; }
    { appId = "com.jagex.Launcher.ThirdParty.RuneLite"; origin = "JagexLauncher"; }
  ];


}
