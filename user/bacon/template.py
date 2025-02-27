pkgname = "bacon"
pkgver = "3.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "12f7bf631cccd1fb847741d0a2841fd6bda6b4fe6f650bde34fd47d94bfe88ca"


def post_install(self):
    self.install_license("LICENSE")
