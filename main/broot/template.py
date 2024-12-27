pkgname = "broot"
pkgver = "1.44.3"
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
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://dystroy.org/broot"
source = f"https://github.com/Canop/broot/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1b68c6d4a21974d5e3c14bf22e067607113afc3ea152b1ec225fe19ffe127348"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/broot")
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
