pkgname = "broot"
pkgver = "1.43.0"
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
sha256 = "64e1b4e2c57373b85ef358241655739f5bb8dedd6600ce0347a6b40640614326"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
