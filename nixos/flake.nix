{
  description = "Nixos config flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    # home-manager = {
    #   url = "github:nix-community/home-manager";
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };
    nix-flatpak.url = "github:gmodena/nix-flatpak/?ref=v0.3.0";
};

  outputs = { self, nixpkgs, nix-flatpak, ... }@inputs:
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
                # inputs.home-manager.nixosModules.default
            ];
          };
      };
    };
}
