pkgname = "thunar"
pkgver = "4.21.7"
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
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/thunar/start"
source = f"$(XFCE_SITE)/xfce/thunar/{pkgver[: pkgver.rfind('.')]}/thunar-{pkgver}.tar.xz"
sha256 = "fcb196b2f89cbcb8a3f5130fa9a1a11bc49d66a6403bc91aff7676648d95d51f"
options = ["etcfiles", "!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("thunar-devel")
def _(self):
    return self.default_devel()
