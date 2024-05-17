pkgname = "eza"
pkgver = "0.18.16"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
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
sha256 = "dd713474b902568cb2c7c8ea7db8e08db5818617e34908ae7142e9da9cefd17b"


def post_install(self):
    self.install_license("LICENCE")
    self.install_completion("completions/bash/eza", "bash")
    self.install_completion("completions/zsh/_eza", "zsh")
    self.install_completion("completions/fish/eza.fish", "fish")
