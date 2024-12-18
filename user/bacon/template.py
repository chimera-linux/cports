pkgname = "bacon"
pkgver = "3.6.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e8b49e95f40c050ef684b94fadc3ff55e1d4a694e215ea68ea82ea5e676c1e9c"


def post_install(self):
    self.install_license("LICENSE")
