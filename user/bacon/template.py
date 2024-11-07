pkgname = "bacon"
pkgver = "3.2.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d8b516b0af8564fbd470513bd6420ba077e74a3860d655efaf9ec12fda47e7a1"


def post_install(self):
    self.install_license("LICENSE")
