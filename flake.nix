{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    devshell.url = "github:numtide/devshell";
    cadquery.url = "github:vinszent/cq-flake";
  };

  outputs =
    inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [ inputs.devshell.flakeModule ];
      systems = [ "x86_64-linux" ];
      perSystem =
        { system, ... }:
        let
          cqpkgs = inputs.cadquery.packages.${system};
          cqpy = cqpkgs.python.pkgs;
        in
        {
          devshells.default = {
            packages = [
              cqpkgs.cq-editor
              (cqpkgs.python.withPackages (py: [
                cqpy.cadquery
                cqpy.cq-kit
                cqpy.cq-warehouse
                cqpy.ocp-stubs
                cqpy.pywrap
                cqpy.pybind11-stubgen
              ]))
            ];
          };
        };
    };
}
