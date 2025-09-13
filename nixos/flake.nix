{
  description = "Nixos config flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    home-manager = {
      url = "github:nix-community/home-manager";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    nix-flatpak.url = "github:gmodena/nix-flatpak/?ref=v0.4.1";
    # catppuccin.url = "github:catppuccin/nix";
    wezterm.url = "github:wez/wezterm?dir=nix&rev=54675c9c35788466f7828f5d722832bd1f310a62";
    # umu= {
    #   url = "git+https://github.com/Open-Wine-Components/umu-launcher/?dir=packaging\/nix&submodules=1&tag=1.2.5";
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };
    legends-viewer.url = "github:dakota-marshall/LegendsViewer-Next?dir=nix&ref=add-nix-flake";
    musnix.url = "github:musnix/musnix";
};

  outputs = { self, nixpkgs, home-manager, nix-flatpak, musnix, ... }@inputs:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      nixosConfigurations = {
          desktop = nixpkgs.lib.nixosSystem {
            specialArgs = {inherit inputs;};
            modules = [
                nix-flatpak.nixosModules.nix-flatpak
                ./hosts/desktop/configuration.nix
                # umu.nixosModules.umu
                musnix.nixosModules.musnix
                home-manager.nixosModules.home-manager {
                   # home-manager.extraSpecialArgs = {inherit inputs; };
                   home-manager.users.dmarshall = {
                     imports = [
                       ./modules/home-manager/dmarshall/main.nix

                     ];
                   };  
                }
                # home-manager.nixosModules.default
            ];
          };

          laptop = nixpkgs.lib.nixosSystem {
            specialArgs = {inherit inputs;};
            modules = [
                nix-flatpak.nixosModules.nix-flatpak
                ./hosts/laptop/configuration.nix
                home-manager.nixosModules.default
            ];
          };
      };
    };
}
