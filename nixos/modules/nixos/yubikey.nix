{ config, pkgs, ... }:
{
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
    origin = "pam://dmarshall-endeavour";
    appid = "pam://dmarshall-endeavour";
    control = "sufficient";
    interactive = true;
    cue = true;

  };
}
