pkgname = "eza"
pkgver = "0.18.13"
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
sha256 = "679fd3b5b389553aa77a2bce496e8658848ef0f4624968fd1a330dbe92032438"


def post_install(self):
    self.install_license("LICENCE")
    self.install_completion("completions/bash/eza", "bash")
    self.install_completion("completions/zsh/_eza", "zsh")
    self.install_completion("completions/fish/eza.fish", "fish")
