pkgname = "openpgp-card-ssh-agent"
pkgver = "0.3.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "pcsc-lite-devel"]
depends = ["ccid"]
pkgdesc = "SSH-agent backed by OpenPGP card authentication keys"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/ssh-agent"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3a916e09f46539d18bcc443e78bd14d19c490f5312325920e074e114a1454e5d"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
    self.install_service(self.files_path / "openpgp-card-ssh-agent.user")
