# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running ‘nixos-help’).

{ config, pkgs, ... }:

{
  imports = let customModules = "../../modules/"; in [ 
          # Include the results of the hardware scan.
          ./hardware-configuration.nix
          ( customModules + "nixos/defaults.nix" )
          ( customModules + "nixos/users.nix" )
          ( customModules + "nixos/yubikey.nix" )
          ( customModules + "nixos/packages.nix" )
          ( customModules + "nixos/flatpaks.nix" )
  ];
  

  networking.hostName = "dmarshall-laptop"; # Define your hostname.
  # Enable touchpad support (enabled default in most desktopManager).
  services.xserver.libinput.enable = true;
  system.stateVersion = "23.11"; # Did you read the comment?

}
