pkgname = "openpgp-card-ssh-agent"
pkgver = "0.3.6"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["dinit-chimera", "rust-std", "pcsc-lite-devel", "dbus-devel"]
depends = ["ccid"]
pkgdesc = "SSH-agent backed by OpenPGP card authentication keys"
license = "Apache-2.0 OR MIT"
url = "https://codeberg.org/openpgp-card/ssh-agent"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b2605357346189593972eed3e42791a729c24cbab871b776884f4cc1f5030d0a"


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
    self.install_service(self.files_path / "openpgp-card-ssh-agent.user")
