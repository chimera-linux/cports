pkgname = "garcon"
pkgver = "4.18.2"
pkgrel = 1
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext",
    "glib-devel",
    "gmake",
    "gobject-introspection",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
]
pkgdesc = "Xfce implementation of the freedesktop compliant menu spec"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/garcon/start"
source = f"$(XFCE_SITE)/xfce/garcon/{pkgver[:-2]}/garcon-{pkgver}.tar.bz2"
sha256 = "1b8c9292e131968fbfc8987bbc62c5ba47186dd45ef4e47c5d8c5088bb2d434d"
options = ["!cross"]


@subpackage("garcon-devel")
def _devel(self):
    return self.default_devel()
