pkgname = "openpgp-card-ssh-agent"
pkgver = "0.3.2"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "pcsc-lite-devel"]
depends = ["ccid"]
pkgdesc = "SSH-agent backed by OpenPGP card authentication keys"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/ssh-agent"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9bec8182763050eeaddc6ca9ebecaefa3f2f0f8fe4e74d6f2dd9fdd95d5f00bd"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
    self.install_service(self.files_path / "openpgp-card-ssh-agent.user")
