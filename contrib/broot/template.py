pkgname = "broot"
pkgver = "1.41.1"
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
sha256 = "a784f31833b4cd11386309c2816c8e2f48594cc7658feca63bc57886cd7a566c"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
