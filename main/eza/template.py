pkgname = "eza"
pkgver = "0.20.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "rust-std",
    "zlib-ng-compat-devel",
]
pkgdesc = "Directory listing utility"
maintainer = "psykose <alice@ayaya.dev>"
license = "EUPL-1.2"
url = "https://eza.rocks"
source = (
    f"https://github.com/eza-community/eza/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "51a61bba14d1e4043981cabc5cf3d14352bf6a4ca0e308f437d0c8d00f42c2f7"


def post_install(self):
    self.install_completion("completions/bash/eza", "bash")
    self.install_completion("completions/zsh/_eza", "zsh")
    self.install_completion("completions/fish/eza.fish", "fish")
