pkgname = "broot"
pkgver = "1.46.5"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "oniguruma-devel",
    "rust-std",
    "zlib-ng-compat-devel",
]
pkgdesc = "Filesystem visualization and traversal tool"
license = "MIT"
url = "https://dystroy.org/broot"
source = f"https://github.com/Canop/broot/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "730f07fd8450476204878f42c27b1db4f965053c2da5a602eae8f2764c5b92ce"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/broot")
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
