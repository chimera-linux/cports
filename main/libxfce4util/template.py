pkgname = "libxfce4util"
pkgver = "4.20.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "pkgconf",
    "slibtool",
    "vala",
    "xfce4-dev-tools",
]
makedepends = ["glib-devel"]
pkgdesc = "Utility library for Xfce"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/libxfce4util/start"
source = f"$(XFCE_SITE)/xfce/libxfce4util/{pkgver[:-2]}/libxfce4util-{pkgver}.tar.bz2"
sha256 = "21493f9c9995a282823db93839f6b9f06ae31edb094191ba9acf04d932a2b592"
options = ["!cross"]


@subpackage("libxfce4util-devel")
def _(self):
    return self.default_devel()
