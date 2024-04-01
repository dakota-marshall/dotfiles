
{ config, pkgs, ...}:
{

    # udev rules for Betaflight, adds drone devices to plugdev group for write access
    services.udev.extraRules = ''
                                    # Betaflight udev rules
                                    SUBSYSTEM=="usb", ATTRS{idVendor}=="2e3c", ATTRS{idProduct}=="df11", MODE="0664", GROUP="plugdev"
                                    SUBSYSTEM=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="df11", MODE="0664", GROUP="plugdev"

                                    
                                    #Flipper Zero serial port 
                                    SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5740", ATTRS{manufacturer}=="Flipper Devices Inc.", TAG+="uaccess", GROUP="dialout" 
                                    #Flipper Zero DFU 
                                    SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="df11", ATTRS{manufacturer}=="STMicroelectronics", TAG+="uaccess", GROUP="dialout" 
                                    #Flipper ESP32s2 BlackMagic 
                                    SUBSYSTEMS=="usb", ATTRS{idVendor}=="303a", ATTRS{idProduct}=="40??", ATTRS{manufacturer}=="Flipper Devices Inc.", TAG+="uaccess", GROUP="dialout" 
                                    #Flipper U2F 
                                    SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5741", ATTRS{manufacturer}=="Flipper Devices Inc.", ENV{ID_SECURITY_TOKEN}="1"
                               '';

}
