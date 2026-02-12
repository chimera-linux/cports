pkgname = "broot"
pkgver = "1.55.0"
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
sha256 = "3049d055f37bfdc3b2057a3e2186cfdb58b596e1586b6b129698b350a80cfda3"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/broot")
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
