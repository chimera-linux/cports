pkgname = "terminology"
pkgver = "1.12.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext-tiny"]
makedepends = ["efl-devel"]
depends = ["xdg-utils"]
pkgdesc = "EFL-based terminal emulator"
license = "BSD-2-Clause"
url = "https://enlightenment.org"
source = f"http://download.enlightenment.org/rel/apps/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f8ced9584c2e9ae87452ce7425fd25b2d3e122c7489785d2917890215c6b5aa9"

def post_install(self):
    self.install_license("COPYING")
