pkgname = "eza"
pkgver = "0.19.1"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "rust-std",
    "zlib-ng-compat-devel",
]
pkgdesc = "Directory listing utility"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://eza.rocks"
source = (
    f"https://github.com/eza-community/eza/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "a256ecdb9996933300bb54e19a68df61e27385e5df20ba1f780f2e454a7f8e8a"


def post_install(self):
    self.install_license("LICENCE")
    self.install_completion("completions/bash/eza", "bash")
    self.install_completion("completions/zsh/_eza", "zsh")
    self.install_completion("completions/fish/eza.fish", "fish")
