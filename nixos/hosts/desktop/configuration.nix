# Edit this configuration file to define what should be installed on
# your system. Help is available in the configuration.nix(5) man page, on
# https://search.nixos.org/options and in the NixOS manual (`nixos-help`).

{ inputs, config, lib, pkgs, ... }:

{
  imports =
    [ # Include the results of the hardware scan.
      ./hardware-configuration.nix
      ../../modules/nixos/defaults.nix
      ../../modules/nixos/users.nix
      ../../modules/nixos/yubikey.nix
      ../../modules/nixos/packages/main.nix
      ../../modules/nixos/flatpaks.nix
      ../../modules/nixos/fonts.nix
      ../../modules/nixos/udev.nix
      ../../modules/nixos/cron.nix
      inputs.home-manager.nixosModules.default
    ];

  # import home-manager config
  home-manager = {
    extraSpecialArgs = {inherit inputs; };
    users = {
        dmarshall = import ../../modules/home-manager/dmarshall/main.nix;
    };
  }; 

  # Needed for AMD 7000 GPU
  boot.kernelPackages = pkgs.linuxPackages_latest;
  networking.hostName = "dmarshall-desktop"; # Define your hostname.

  services.logrotate.checkConfig = false;

  #Enable ratbagd for mouse configuration 
  services.ratbagd.enable = true;

  # Disable Networking
  networking.firewall.enable = false;

  services.xserver.videoDrivers = [ "modesetting" ];

   environment.systemPackages = with pkgs; [
     vim # Do not forget to add an editor to edit configuration.nix! The Nano editor is also installed by default.
     wget
     git
     # Build failing
     # blender-hip
     v4l-utils
     linuxPackages_latest.v4l2loopback
   ];

  system.stateVersion = "23.11"; # Did you read the comment?

}

