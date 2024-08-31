pkgname = "xdg-desktop-portal-xapp"
pkgver = "1.0.9"
pkgrel = 0
build_style = "meson"
# XXX: drop libexec
configure_args = ["--libexecdir=/usr/lib", "-Dsystemduserunitdir=/tmp"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["glib-devel", "gtk+3-devel", "xdg-desktop-portal-devel"]
depends = ["xapp", "xdg-desktop-portal"]
pkgdesc = "Backend implementation for xdg-desktop-portal for Cinnamon and Xfce"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "LGPL-2.1-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/xdg-desktop-portal-xapp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4d767025ba3389ce25b4f3ab0ac3447fac4ff05a5f00bf72fe95384105d9afe2"
hardening = ["vis"]


def post_install(self):
    self.uninstall("tmp")
