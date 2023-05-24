pkgname = "xdg-utils"
pkgver = "1.1.3"
pkgrel = 0
_commit = "d11b33ec7f24cfb1546f6b459611d440013bdc72"
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["xmlto", "lynx", "gmake"]
depends = ["xset"]
pkgdesc = "Basic desktop integration scripts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/xdg-utils"
source = (
    f"https://gitlab.freedesktop.org/xdg/{pkgname}/-/archive/{_commit}.tar.gz"
)
sha256 = "cc7f8b1292a4c1fa2054594642ff90e3740269033a32d97bcf9bd04322d5555c"
hardening = ["vis", "cfi"]
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


configure_gen = []
