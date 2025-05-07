pkgname = "terminology"
pkgver = "1.14.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext"]
makedepends = ["efl-devel"]
depends = ["xdg-utils"]
pkgdesc = "EFL-based terminal emulator"
license = "BSD-2-Clause"
url = "https://enlightenment.org"
source = f"http://download.enlightenment.org/rel/apps/terminology/terminology-{pkgver}.tar.xz"
sha256 = "f354057051b05cffb699e33836a1135db1d4ed8bf954f9b57dc0e93bc307514d"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")
