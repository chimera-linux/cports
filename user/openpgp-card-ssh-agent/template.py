pkgname = "openpgp-card-ssh-agent"
pkgver = "0.3.4"
pkgrel = 2
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["dinit-chimera", "rust-std", "pcsc-lite-devel", "dbus-devel"]
depends = ["ccid"]
pkgdesc = "SSH-agent backed by OpenPGP card authentication keys"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/ssh-agent"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b210f0d55e070b0e1024cc1d3a1317afb663929411b05443ec0ce79afd0c0a6a"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
    self.install_service(self.files_path / "openpgp-card-ssh-agent.user")
