pkgname = "neocmakelsp"
pkgver = "0.8.14"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CMake language server"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://neocmakelsp.github.io"
source = f"https://github.com/neocmakelsp/neocmakelsp/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b20ab4aead9cfd8b0da40bc5a3ff449dd26a005c771aceb6e5468808321b7bc1"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("completions/bash/neocmakelsp", "bash")
    self.install_completion("completions/fish/neocmakelsp.fish", "fish")
    self.install_completion("completions/zsh/_neocmakelsp", "zsh")
