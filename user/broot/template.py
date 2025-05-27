pkgname = "broot"
pkgver = "1.46.4"
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
sha256 = "d0080fb6f959ca8978b3930513f72df7a6ef6bc9c204ff499458961c5671c67b"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/broot")
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
