pkgname = "anyrun-provider"
pkgver = "25.12.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = []
pkgdesc = "Simple program to load Anyrun plugins and interact with them"
license = "GPL-3.0-or-later"
url = "https://github.com/anyrun-org/anyrun-provider"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d9b4afcb7bafc4e4d43c64bd6ec8110ae3b858964d68d164c24c0c6505831dd6"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/{pkgname}")
    self.install_license("LICENSE")
