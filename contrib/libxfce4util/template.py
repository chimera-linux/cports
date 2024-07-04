pkgname = "libxfce4util"
pkgver = "4.18.2"
pkgrel = 1
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "gobject-introspection",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "vala",
    "xfce4-dev-tools",
]
makedepends = ["glib-devel"]
pkgdesc = "Utility library for Xfce"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/libxfce4util/start"
source = f"$(XFCE_SITE)/xfce/libxfce4util/{pkgver[:-2]}/libxfce4util-{pkgver}.tar.bz2"
sha256 = "d9a329182b78f7e2520cd4aafcbb276bbbf162f6a89191676539ad2e3889c353"
options = ["!cross"]


@subpackage("libxfce4util-devel")
def _devel(self):
    return self.default_devel()
