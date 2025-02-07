pkgname = "neocmakelsp"
pkgver = "0.8.18"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CMake language server"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://neocmakelsp.github.io"
source = f"https://github.com/neocmakelsp/neocmakelsp/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "41bc9334cc99abb92a1879a240268ffb176423cebddd4db39d9f40e932926adb"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("completions/bash/neocmakelsp", "bash")
    self.install_completion("completions/fish/neocmakelsp.fish", "fish")
    self.install_completion("completions/zsh/_neocmakelsp", "zsh")
