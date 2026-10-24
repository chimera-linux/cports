pkgname = "broot"
pkgver = "1.61.0"
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
sha256 = "458f1be5d78fe3b062618e9b1dbc32cf53171b0ca0769b3f32dfae65e753c264"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "broot"))
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
