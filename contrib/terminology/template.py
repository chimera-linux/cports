pkgname = "terminology"
pkgver = "1.13.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext-tiny"]
makedepends = ["efl-devel"]
depends = ["xdg-utils"]
pkgdesc = "EFL-based terminal emulator"
license = "BSD-2-Clause"
url = "https://enlightenment.org"
source = f"http://download.enlightenment.org/rel/apps/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "16a37fecd7bbd63ec9de3ec6c0af331cee77d6dfda838a1b1573d6f298474da5"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")
