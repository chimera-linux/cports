pkgname = "rsop-oct"
pkgver = "0.1.5"
pkgrel = 0
build_wrksrc = "rsop-oct"
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "dbus-devel", "pcsc-lite-devel"]
pkgdesc = "Stateless OpenPGP CLI tool backed by rpgp and OpenPGP smartcards"
license = "MIT OR Apache-2.0"
url = "https://codeberg.org/heiko/rsop"
source = f"{url}/archive/rsop-oct/v{pkgver}.tar.gz"
sha256 = "c2a38933a642b393310c0eb0b335cced04910b4325806775c6057e77b34e31d2"


def post_install(self):
    self.install_license("../LICENSES/MIT.txt")
