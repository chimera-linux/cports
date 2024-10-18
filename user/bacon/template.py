pkgname = "bacon"
pkgver = "3.1.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f078f2326da81cab31a3196d4ac43d0771d5679c7d5b32ce38309ff89f80559a"


def post_install(self):
    self.install_license("LICENSE")
