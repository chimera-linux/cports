pkgname = "openpgp-card-tools"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "pcsc-lite-devel", "nettle-devel", "bzip2-devel"]
depends = ["ccid"]
pkgdesc = "CLI tool for inspecting, configuring and using OpenPGP cards"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/openpgp-card-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2bea380d0038208d5b6bd93cb7580e6522d4f43bc1e429cc977cb678adb061fb"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
