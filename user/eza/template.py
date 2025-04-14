pkgname = "eza"
pkgver = "0.21.0"
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
license = "EUPL-1.2"
url = "https://eza.rocks"
source = (
    f"https://github.com/eza-community/eza/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "885ae7a12c7ed68dd3a7cca76d4e8beaa100c9e9d6b7ad136b5bb6785e16b28b"


def post_install(self):
    self.install_completion("completions/bash/eza", "bash")
    self.install_completion("completions/zsh/_eza", "zsh")
    self.install_completion("completions/fish/eza.fish", "fish")
