pkgname = "bacon"
pkgver = "3.12.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "729d4672793369a2de7e120232e39c656f15745e4403cb7af6bafc17a6781b4c"


def post_install(self):
    self.install_license("LICENSE")
