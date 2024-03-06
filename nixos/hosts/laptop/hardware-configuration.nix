# Do not modify this file!  It was generated by ‘nixos-generate-config’
# and may be overwritten by future invocations.  Please make changes
# to /etc/nixos/configuration.nix instead.
{ config, lib, pkgs, modulesPath, ... }:

{
  imports =
    [ (modulesPath + "/installer/scan/not-detected.nix")
    ];

  boot.initrd.availableKernelModules = [ "xhci_pci" "nvme" "usb_storage" "sd_mod" "sr_mod" ];
  boot.initrd.kernelModules = [ ];
  boot.kernelModules = [ "kvm-intel" ];
  boot.extraModulePackages = [ ];

  fileSystems."/" =
    { device = "/dev/disk/by-uuid/4308b0eb-4408-4bf2-ad41-7a8de75dadc8";
      fsType = "btrfs";
      options = [ "subvol=nixos" ];
    };
  fileSystems."/home" =
    { device = "/dev/disk/by-uuid/4308b0eb-4408-4bf2-ad41-7a8de75dadc8";
      fsType = "btrfs";
      options = [ "subvol=home" ];
    };

  boot.initrd.luks.devices."data".device = "/dev/disk/by-uuid/6b572b5d-9c22-42ec-8a75-8c1bb218fbdc";
  boot.initrd.luks.devices."swap".device = "/dev/disk/by-uuid/264c16c9-f72f-4b0a-9ca7-5ec3a400dc82";

  fileSystems."/boot" =
    { device = "/dev/disk/by-uuid/9191-8ABF";
      fsType = "vfat";
    };

  swapDevices = [ {
          device = "/dev/disk/by-uuid/774380fa-f968-4660-a0e8-380b375dca92";
          size = 18200;
      } ];

  # Enables DHCP on each ethernet and wireless interface. In case of scripted networking
  # (the default) this is the recommended approach. When using systemd-networkd it's
  # still possible to use this option, but it's recommended to use it in conjunction
  # with explicit per-interface declarations with `networking.interfaces.<interface>.useDHCP`.
  networking.useDHCP = lib.mkDefault true;
  # networking.interfaces.wlp60s0.useDHCP = lib.mkDefault true;

  nixpkgs.hostPlatform = lib.mkDefault "x86_64-linux";
  hardware.cpu.intel.updateMicrocode = lib.mkDefault config.hardware.enableRedistributableFirmware;
}
