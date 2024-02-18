pkgname = "openpgp-card-ssh-agent"
pkgver = "0.2.3"
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
sha256 = "afbb3620a361eb541d0a289ee9789f68c04db2dc07135f42ac989b92a4f149b0"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
    self.install_service(self.files_path / "openpgp-card-ssh-agent.user")
