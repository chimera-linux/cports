pkgname = "eza"
pkgver = "0.20.6"
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
sha256 = "bf7c30789be7866a36fda9d2b1bb351f41675f4c8bb8c89e7ff85619cc894bfa"


def post_install(self):
    self.install_completion("completions/bash/eza", "bash")
    self.install_completion("completions/zsh/_eza", "zsh")
    self.install_completion("completions/fish/eza.fish", "fish")
