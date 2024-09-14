pkgname = "terminology"
pkgver = "1.13.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext"]
makedepends = ["efl-devel"]
depends = ["xdg-utils"]
pkgdesc = "EFL-based terminal emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://enlightenment.org"
source = f"http://download.enlightenment.org/rel/apps/terminology/terminology-{pkgver}.tar.xz"
sha256 = "16a37fecd7bbd63ec9de3ec6c0af331cee77d6dfda838a1b1573d6f298474da5"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")
