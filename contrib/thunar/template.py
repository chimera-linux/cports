pkgname = "thunar"
pkgver = "4.18.11"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "exo-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gtk+3-devel",
    "libgudev-devel",
    "libnotify-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "pango-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce file manager"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/thunar/start"
source = f"$(XFCE_SITE)/xfce/thunar/{pkgver[:pkgver.rfind('.')]}/thunar-{pkgver}.tar.bz2"
sha256 = "7d0bdae2076a568c137d403ab5600e06a7a4f7a02514d486da7b8414aa75d612"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("thunar-devel")
def _(self):
    return self.default_devel()
