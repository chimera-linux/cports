pkgname = "openpgp-card-tools"
pkgver = "0.10.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "pcsc-lite-devel", "nettle-devel", "bzip2-devel"]
depends = ["ccid"]
pkgdesc = "CLI tool for inspecting, configuring and using OpenPGP cards"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/openpgp-card-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fb8cd1c95c558f1e16a749746dadc6040deca54f4e3aa7735ffa5f082cdfcc01"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
