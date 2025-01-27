{ config, pkgs, ...}:
{

  fonts.packages = with pkgs; [
    noto-fonts
    ipafont
  ] ++ builtins.filter lib.attrsets.isDerivation (builtins.attrValues pkgs.nerd-fonts);

}
