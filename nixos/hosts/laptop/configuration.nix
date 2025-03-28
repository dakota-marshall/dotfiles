# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running ‘nixos-help’).

{ inputs, config, pkgs, ... }:

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
      inputs.home-manager.nixosModules.default
    ];

  # import home-manager config
  home-manager = {
    extraSpecialArgs = {inherit inputs; };
    users = {
        dmarshall = import ../../modules/home-manager/dmarshall/main.nix;
    };
  }; 

  networking.hostName = "dmarshall-laptop"; # Define your hostname.
  # Enable touchpad support (enabled default in most desktopManager).
  services.xserver.libinput.enable = true;
  system.stateVersion = "23.11"; # Did you read the comment?

   environment.systemPackages = with pkgs; [
     vim # Do not forget to add an editor to edit configuration.nix! The Nano editor is also installed by default.
     wget
     git
     blender
   ];
}
