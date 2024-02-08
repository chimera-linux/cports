pkgname = "eza"
pkgver = "0.18.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "rust-std",
    "zlib-devel",
]
pkgdesc = "Directory listing utility"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://eza.rocks"
source = (
    f"https://github.com/eza-community/eza/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "f4ac88d8304bf0e403f922f05cd2ad9f87fd6b034de07228e4248edd9c9d0220"


def post_install(self):
    self.install_license("LICENCE")
    self.install_completion("completions/bash/eza", "bash")
    self.install_completion("completions/zsh/_eza", "zsh")
    self.install_completion("completions/fish/eza.fish", "fish")
