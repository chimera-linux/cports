pkgname = "openpgp-card-tool-git"
pkgver = "0.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "openssl-devel", "pcsc-lite-devel", "sqlite-devel"]
depends = ["ccid"]
pkgdesc = "Drop in replacement for gpg in git for usage with OpenPGP cards"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/tool-git"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "44cdc304884772fe31e66c35e8f536bd4bd8e41331689e165d8b06b43d7b5347"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
