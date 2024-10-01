{ config, pkgs, ... }:
{
  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users.dmarshall = {
    isNormalUser = true;
    description = "Dakota Marshall";
    extraGroups = [ "networkmanager" "wheel" "docker" "uucp" "vboxusers" "dialout" "plugdev" "gamemode" "kvm" "adbusers"];
    shell = pkgs.zsh;
    packages = with pkgs; [
    ];
  };

  # Create plugdev group
  users.groups.plugdev = {};

  systemd.user.services.playerctld = {
    enable = true;

    wantedBy = [ "default.target" ];

    serviceConfig = {
      ExecStart = "${pkgs.playerctl}/bin/playerctld";
      Type = "dbus";
      BusName = "org.mpris.MediaPlayer2.playerctld";
    };
  };
}
