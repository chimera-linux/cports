pkgname = "xdg-desktop-portal-xapp"
pkgver = "1.1.2"
pkgrel = 0
build_style = "meson"
# XXX: drop libexec
configure_args = ["--libexecdir=/usr/lib", "-Dsystemduserunitdir=/tmp"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["gtk+3-devel", "xdg-desktop-portal-devel"]
depends = ["xapp", "xdg-desktop-portal"]
pkgdesc = "Backend implementation for xdg-desktop-portal for Cinnamon and Xfce"
license = "LGPL-2.1-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/xdg-desktop-portal-xapp/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7bd4d0439218d00d9fe55c308292b1dc70716cb8464970fe8d2245769a7dd18a"
hardening = ["vis"]


def post_install(self):
    self.uninstall("tmp")
