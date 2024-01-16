{ pkgs ? import <nixpkgs> {} }:
{
  home.packages = with pkgs; let xpipe-src = pkgs.fetchFromGitHub {
    owner = "xpipe-io";
    repo = "nixpkg";
    rev = "08fefaf79b3a64aab3d2e84931612ade4936a421";
    sha256 = "sha256-0UcW68SFmj6kZsB65KTSNc8/qe65m0lNn5jcWnMijIk=";
  }; [
    # gui
    firefox
    obsidian
    _1password-gui
    blackbox-terminal

    # tools    
    btop
    nvtop
    neofetch
    rnix-lsp
    direnv
    neovim
    bat
    eza
    lazygit
    aha
    unzip
    jq
    ripgrep
    fzf
    httpie

    # languages
    nodejs yarn
    crystal shards
    pyenv poetry
    nim
    zig
    bun
    deno
    
    # zsh stuff
    zsh
    spaceship-prompt

    # xpipe
    (callPackage "${xpipe-src}/xpipe/1.7.14/default.nix" {})
  ];
}

