pkgname = "xdg-desktop-portal-xapp"
pkgver = "1.1.0"
pkgrel = 0
build_style = "meson"
# XXX: drop libexec
configure_args = ["--libexecdir=/usr/lib", "-Dsystemduserunitdir=/tmp"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["glib-devel", "xdg-desktop-portal-devel"]
depends = ["xapp", "xdg-desktop-portal"]
pkgdesc = "Backend implementation for xdg-desktop-portal for Cinnamon and Xfce"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "LGPL-2.1-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/xdg-desktop-portal-xapp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2d0746ad1021d8848fb60f1444d09c81c5a4da90df334b44418d6533e6811c13"
hardening = ["vis"]


def post_install(self):
    self.uninstall("tmp")
