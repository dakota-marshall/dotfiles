{ config, pkgs, ... }:
{
  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users.dmarshall = {
    isNormalUser = true;
    description = "Dakota Marshall";
    extraGroups = [ "networkmanager" "wheel" "docker" "uucp" "vboxusers" ];
    shell = pkgs.zsh;
    packages = with pkgs; [
    ];
  };
}
