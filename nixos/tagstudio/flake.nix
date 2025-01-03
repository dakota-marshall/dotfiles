{
  description = "TagStudio";

  inputs = {
    devenv.url = "github:cachix/devenv";

    devenv-root = {
      url = "file+file:///dev/null";
      flake = false;
    };

    flake-parts = {
      url = "github:hercules-ci/flake-parts";
      inputs.nixpkgs-lib.follows = "nixpkgs";
    };

    nix2container = {
      url = "github:nlewo/nix2container";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    # Pinned to Qt version 6.7.1
    nixpkgs-qt6.url = "github:NixOS/nixpkgs/e6cea36f83499eb4e9cd184c8a8e823296b50ad5";

    systems.url = "github:nix-systems/default-linux";
  };

  outputs =
    {
      flake-parts,
      nixpkgs,
      nixpkgs-qt6,
      self,
      systems,
      ...
    }@inputs:
    flake-parts.lib.mkFlake { inherit inputs; } {
        
        systems = import systems;

        perSystem = { config, pkgs, system, ... }:
        let
            inherit (nixpkgs) lib;
            inherit (pkgs) stdenv;
            qt6Pkgs = import nixpkgs-qt6 { inherit system; };
            buildInputs = with pkgs; [
                python3Packages.pip
                cmake
                binutils
                coreutils
                dbus
                fontconfig
                freetype
                gdb
                glib
                libGL
                libGLU
                libgcc
                libxkbcommon
                mypy
                ruff
                xorg.libxcb
                xorg.libX11
                zstd
            ]
            ++ (with qt6Pkgs; [
                qt6.full
                qt6.qtbase
                qt6.wayland
                qtcreator
            ]);

            libPath = lib.makeLibraryPath (
                with pkgs;
                [
                    dbus
                    fontconfig
                    freetype
                    gcc-unwrapped
                    glib
                    libglvnd
                    libkrb5
                    libpulseaudio
                    libva
                    libxkbcommon
                    openssl
                    stdenv.cc.cc.lib
                    wayland
                    xorg.libxcb
                    xorg.libX11
                    xorg.libXrandr
                    zlib
                    zstd
                ]
                ++ (with pt6Pkgs.qt6; ) [
                    pqbase
                    qtwayland
                    full
                ];
            );
        in
        {
            
            formatter = pkgs.nixfmt-rfc-style;

            packages.default = pkgs.python312Packages.buildPythonPackage rec {
                inherit buildInputs;

                name = "tagstudio";
                version = self.ShortRev or "dev";

                meta = {
                    homepage = "https://github.com/TagStudioDev/TagStudio";
                    description = "A User-Focused Photo & File Management System";
                    license = licenses.gpl3;
                    maintainer = with maintainers; [ dakota-marshall ]
                };

                src = "./"

                postPatch = ''
                    # Install pypi packages
                    runHook preBuild
                    pip install -r ${src}/requirements.txt --target=${pythonSitePackages}
                    runHook postbuild
                '';
            };
        };
    };
