pkgname = "neocmakelsp"
pkgver = "0.8.15"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CMake language server"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://neocmakelsp.github.io"
source = f"https://github.com/neocmakelsp/neocmakelsp/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "355b7bc05c0ee44e12e4827e1d4d43ba7d1009802f5ff7aab8f681e20717278c"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("completions/bash/neocmakelsp", "bash")
    self.install_completion("completions/fish/neocmakelsp.fish", "fish")
    self.install_completion("completions/zsh/_neocmakelsp", "zsh")
