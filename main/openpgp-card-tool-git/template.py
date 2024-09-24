pkgname = "openpgp-card-tool-git"
pkgver = "0.1.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "dbus-devel",
    "openssl-devel",
    "pcsc-lite-devel",
    "rust-std",
    "sqlite-devel",
]
depends = ["ccid"]
pkgdesc = "Drop in replacement for gpg in git for usage with OpenPGP cards"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/tool-git"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1bf653e40f6ceea03e0dad3c6e8b89c2c099ec580b249a5e2936904388e49507"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
