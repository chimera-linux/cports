pkgname = "broot"
pkgver = "1.56.2"
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
sha256 = "3e7be4252c76565f6d71b34bd07d26e1444b9ac2e1c8271c724f6e866fe75565"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "broot"))
    self.install_license("LICENSE")
    self.install_man("man/page", cat=1, name="broot")
