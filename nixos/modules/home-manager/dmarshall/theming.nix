{ config, pkgs, ... }:

{
    # environment.sessionVariables.QT_STYLE_OVERRIDE = "adwaita-dark";
    dconf = {
        enable = true;
        settings = {
            "org/gnome/desktop/interface" = {
                color-scheme = "prefer-dark";
            };
        };
    };
    gtk = {
        enable = true;
        theme = {
            name = "Adwaita";
        };
        iconTheme = {
          package = pkgs.adwaita-icon-theme;
          name = "Adwaita";
        };
        gtk3.extraConfig = {
          gtk-application-prefer-dark-theme = "1";
        };

        gtk4.extraConfig = {
          gtk-application-prefer-dark-theme = "1";
        };
    };
}
