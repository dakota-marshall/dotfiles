{ inputs, config, pkgs, lib,  ... }:

let
  firefox-profile-switcher-connector = pkgs.callPackage ./firefox-profile-switcher-connector.nix { };

in {

  environment.systemPackages = with pkgs; [
    (firefox.override { nativeMessagingHosts = [ firefox-profile-switcher-connector ]; })
  ];

  # xdg.configFile = {
  #   "firefoxprofileswitcher/config.json".text = ''
  #     {"browser_binary": "${firefox-package}/bin/firefox"}
  #   '';
  # };
}
