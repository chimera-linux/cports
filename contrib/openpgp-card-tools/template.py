pkgname = "openpgp-card-tools"
pkgver = "0.11.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "pcsc-lite-devel"]
depends = ["ccid"]
pkgdesc = "CLI tool for inspecting, configuring and using OpenPGP cards"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/openpgp-card-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "083fe2e127baaee5dc799274d7208db5a3b7debde433f762263b8e4912af1d3c"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
