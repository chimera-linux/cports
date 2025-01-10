pkgname = "thunar"
pkgver = "4.20.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gobject-introspection",
    "gtk-doc-tools",
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
source = f"$(XFCE_SITE)/xfce/thunar/{pkgver[: pkgver.rfind('.')]}/thunar-{pkgver}.tar.bz2"
sha256 = "e5a83ccd2992b4c4e5ada3563ce92ebcbc222e13bb53d45ec350923ce1a51b6a"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("thunar-devel")
def _(self):
    return self.default_devel()
