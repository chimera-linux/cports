pkgname = "xdg-user-dirs"
pkgver = "0.20"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext",
    "libxslt-progs",
    "meson",
    "pkgconf",
]
pkgdesc = "Tool to help manage user directories"
license = "GPL-2.0-or-later"
url = "http://www.freedesktop.org/wiki/Software/xdg-user-dirs"
source = f"https://gitlab.freedesktop.org/xdg/xdg-user-dirs/-/archive/v{pkgver}/xdg-user-dirs-v{pkgver}.tar.gz"
sha256 = "988d3f3274cb2b69796ace22ddbb0abfc2c0157fff65258045f055cfba024d6e"
options = ["etcfiles"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
