pkgname = "openpgp-card-tool-git"
pkgver = "0.1.5"
pkgrel = 1
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
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/tool-git"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "4d8bba39568c5bdad36cc987f4acd5faa958fde595693a049182eb88b9821d01"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
