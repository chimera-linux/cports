pkgname = "libxfce4util"
pkgver = "4.20.1"
pkgrel = 1
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
license = "LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/libxfce4util/start"
source = f"$(XFCE_SITE)/xfce/libxfce4util/{pkgver[:-2]}/libxfce4util-{pkgver}.tar.bz2"
sha256 = "84bfc4daab9e466193540c3665eee42b2cf4d24e3f38fc3e8d1e0a2bebe3b8f1"
# introspection
options = ["!cross"]


@subpackage("libxfce4util-devel")
def _(self):
    return self.default_devel()
