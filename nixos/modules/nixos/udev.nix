
{ config, pkgs, ...}:
{

    # udev rules for Betaflight, adds drone devices to plugdev group for write access
    services.udev.extraRules = ''
                                    SUBSYSTEM=="usb", ATTRS{idVendor}=="2e3c", ATTRS{idProduct}=="df11", MODE="0664", GROUP="plugdev"
                                    SUBSYSTEM=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="df11", MODE="0664", GROUP="plugdev"
                               '';

}
