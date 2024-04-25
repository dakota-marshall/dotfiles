{
  description = "Nixos config flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    home-manager = {
      url = "github:nix-community/home-manager";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    nix-flatpak.url = "github:gmodena/nix-flatpak/?ref=v0.3.0";
};

  outputs = { self, nixpkgs, home-manager, nix-flatpak, ... }@inputs:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      nixosConfigurations = {
          default = nixpkgs.lib.nixosSystem {
            specialArgs = {inherit inputs;};
            modules = [
                nix-flatpak.nixosModules.nix-flatpak
                ./hosts/default/configuration.nix
                home-manager.nixosModules.home-manager {
                   home-manager.extraSpecialArgs = {inherit inputs; };
                   home-manager.users.dmarshall = import ./modules/home-manager/dmarshall.nix; 
                }
            ];
          };
          desktop = nixpkgs.lib.nixosSystem {
            specialArgs = {inherit inputs;};
            modules = [
                nix-flatpak.nixosModules.nix-flatpak
                ./hosts/desktop/configuration.nix
                home-manager.nixosModules.home-manager {
                   home-manager.extraSpecialArgs = {inherit inputs; };
                   home-manager.users.dmarshall = import ./modules/home-manager/dmarshall.nix; 
                }
            ];
          };

          laptop = nixpkgs.lib.nixosSystem {
            specialArgs = {inherit inputs;};
            modules = [
                nix-flatpak.nixosModules.nix-flatpak
                ./hosts/laptop/configuration.nix
                # inputs.home-manager.nixosModules.default
            ];
          };
      };
    };
}
