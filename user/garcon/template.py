pkgname = "garcon"
pkgver = "4.20.0"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
]
pkgdesc = "Xfce implementation of the freedesktop compliant menu spec"
license = "LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/garcon/start"
source = f"$(XFCE_SITE)/xfce/garcon/{pkgver[:-2]}/garcon-{pkgver}.tar.bz2"
sha256 = "7fb8517c12309ca4ddf8b42c34bc0c315e38ea077b5442bfcc4509415feada8f"
options = ["!cross"]


@subpackage("garcon-devel")
def _(self):
    return self.default_devel()
