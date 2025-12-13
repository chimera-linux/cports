pkgname = "thunar"
pkgver = "4.20.6"
pkgrel = 1
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
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/thunar/start"
source = f"$(XFCE_SITE)/xfce/thunar/{pkgver[: pkgver.rfind('.')]}/thunar-{pkgver}.tar.bz2"
sha256 = "e815e034c073d634d0e77566837e1d9417b65c886924e3678e3325d5466c784d"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("thunar-devel")
def _(self):
    return self.default_devel()
