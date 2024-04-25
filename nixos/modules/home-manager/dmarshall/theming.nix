{ config, pkgs, ... }:

{
    gtk = {
        enable = true;
        theme = {
            name = "Catppuccin-Mocha-Standard-Lavender-Dark";
            package = pkgs.catppuccin-gtk.override {
                accents = [ "lavender" ];
                size = "standard";
                variant = "mocha";
            };
        };
        iconTheme = {
          package = pkgs.gnome.adwaita-icon-theme;
          name = "Adwaita";
        };
    };

    # Now symlink the `~/.config/gtk-4.0/` folder declaratively:
    xdg.configFile = {
      "gtk-4.0/assets".source = "${config.gtk.theme.package}/share/themes/${config.gtk.theme.name}/gtk-4.0/assets";
      "gtk-4.0/gtk.css".source = "${config.gtk.theme.package}/share/themes/${config.gtk.theme.name}/gtk-4.0/gtk.css";
      "gtk-4.0/gtk-dark.css".source = "${config.gtk.theme.package}/share/themes/${config.gtk.theme.name}/gtk-4.0/gtk-dark.css";
    };
}
