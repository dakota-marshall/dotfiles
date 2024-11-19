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
    wezterm.url = "github:wez/wezterm?dir=nix";
};

  outputs = { self, nixpkgs, home-manager, nix-flatpak, ... }@inputs:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      nixosConfigurations = {
          # default = nixpkgs.lib.nixosSystem {
          #   specialArgs = {inherit inputs;};
          #   modules = [
          #       nix-flatpak.nixosModules.nix-flatpak
          #       catppuccin.nixosModules.catppuccin
          #       ./hosts/default/configuration.nix
          #       home-manager.nixosModules.home-manager {
          #          home-manager.extraSpecialArgs = {inherit inputs; };
          #          home-manager.users.dmarshall = { 
          #            imports = [
          #              catppuccin.homeManagerModules.catppuccin
          #              ./modules/home-manager/dmarshall.nix
          #            ];
          #          };
          #       }
          #   ];
          # };
          desktop = nixpkgs.lib.nixosSystem {
            specialArgs = {inherit inputs;};
            modules = [
                nix-flatpak.nixosModules.nix-flatpak
                ./hosts/desktop/configuration.nix
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
