pkgname = "neocmakelsp"
pkgver = "0.8.19"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CMake language server"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://neocmakelsp.github.io"
source = f"https://github.com/neocmakelsp/neocmakelsp/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e63cf9a59f818c61196ae41136c164d62fe1fe42116c7dd51bee0f9df2ce55ac"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("completions/bash/neocmakelsp", "bash")
    self.install_completion("completions/fish/neocmakelsp.fish", "fish")
    self.install_completion("completions/zsh/_neocmakelsp", "zsh")
