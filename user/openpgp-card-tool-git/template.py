pkgname = "openpgp-card-tool-git"
pkgver = "0.1.6"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "dbus-devel",
    "openssl3-devel",
    "pcsc-lite-devel",
    "rust-std",
    "sqlite-devel",
]
depends = ["ccid"]
pkgdesc = "Drop in replacement for gpg in git for usage with OpenPGP cards"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/tool-git"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fc0f3ba974a5020f844580781cc52c342a9ff93ab877a3a7e2a281d0d2899737"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
