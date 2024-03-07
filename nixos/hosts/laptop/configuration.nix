# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running ‘nixos-help’).

{ config, pkgs, ... }:

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
    ];


  networking.hostName = "dmarshall-laptop"; # Define your hostname.
  # Enable touchpad support (enabled default in most desktopManager).
  services.xserver.libinput.enable = true;
  system.stateVersion = "23.11"; # Did you read the comment?

}
