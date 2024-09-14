pkgname = "broot"
pkgver = "1.44.0"
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
sha256 = "a235f9e326d39416b484ea5e677642194f726b7683bd2d5dcd1520ba37afb34d"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
