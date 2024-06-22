pkgname = "broot"
pkgver = "1.39.0"
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
sha256 = "d1d2ccc11543ff4ea645d57a5e78639542a6f510b585a78c31ddb3a24399bf61"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
