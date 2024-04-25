# Edit this configuration file to define what should be installed on
# your system. Help is available in the configuration.nix(5) man page, on
# https://search.nixos.org/options and in the NixOS manual (`nixos-help`).

{ config, lib, pkgs, ... }:

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
    ];

  # Needed for AMD 7000 GPU
  boot.kernelPackages = pkgs.linuxPackages_latest;
  networking.hostName = "dmarshall-desktop"; # Define your hostname.

  services.logrotate.checkConfig = false;

  services.xserver.videoDrivers = [ "modesetting" ];

   environment.systemPackages = with pkgs; [
     vim # Do not forget to add an editor to edit configuration.nix! The Nano editor is also installed by default.
     wget
     git
     blender-hip
     v4l-utils
     linuxPackages.v4l2loopback
   ];

  system.stateVersion = "23.11"; # Did you read the comment?

}

