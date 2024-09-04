{ pkgs }: {
    deps = [
      pkgs./r'rrrrrrrr
      pkgs.nodePackages.vscode-langservers-extracted
      pkgs.nodePackages.typescript-language-server
    ];
  }