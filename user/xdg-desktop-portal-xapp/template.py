pkgname = "xdg-desktop-portal-xapp"
pkgver = "1.1.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemduserunitdir=/tmp"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["gtk+3-devel", "xdg-desktop-portal-devel"]
depends = ["xapp", "xdg-desktop-portal"]
pkgdesc = "Backend implementation for xdg-desktop-portal for Cinnamon and Xfce"
license = "LGPL-2.1-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/xdg-desktop-portal-xapp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0c163f39a33746aec14a12ebe30f13e0f210e3b383979e7597512eabddca64b6"
hardening = ["vis"]


def post_install(self):
    self.uninstall("tmp")
