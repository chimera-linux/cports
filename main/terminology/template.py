pkgname = "terminology"
pkgver = "1.11.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext-tiny"]
makedepends = ["efl-devel"]
depends = ["xdg-utils"]
pkgdesc = "EFL-based terminal emulator"
license = "BSD-2-Clause"
url = "https://enlightenment.org"
source = f"http://download.enlightenment.org/rel/apps/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4fd884bd2ffbbc86d87163063074fbd969be04b17bb8d7e23cd1f6708fd86a2d"

def post_install(self):
    self.install_license("COPYING")
