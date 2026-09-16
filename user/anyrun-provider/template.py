pkgname = "anyrun-provider"
pkgver = "25.12.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
pkgdesc = "Backend for anyrun"
license = "GPL-3.0-or-later"
url = "https://github.com/anyrun-org/anyrun-provider"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d9b4afcb7bafc4e4d43c64bd6ec8110ae3b858964d68d164c24c0c6505831dd6"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "anyrun-provider"))
