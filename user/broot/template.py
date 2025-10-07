pkgname = "broot"
pkgver = "1.51.0"
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
sha256 = "66099aa66fd1b41a30b20e9c20a24b30ebadba78a68527ab33debdc9b119b6a1"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/broot")
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
