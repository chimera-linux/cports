pkgname = "openpgp-card-tool-git"
pkgver = "0.1.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl-devel", "pcsc-lite-devel", "sqlite-devel"]
depends = ["ccid"]
pkgdesc = "Drop in replacement for gpg in git for usage with OpenPGP cards"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/tool-git"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e0994fb2135343905a45b741b34a2ba76671ba01a04adb8231e7865d2ed7151e"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
