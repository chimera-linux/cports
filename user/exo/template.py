pkgname = "exo"
pkgver = "4.20.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gtk-doc-tools",
    "pkgconf",
    "python",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = ["glib-devel", "gtk+3-devel", "libxfce4ui-devel"]
pkgdesc = "Xfce extensions library"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://docs.xfce.org/xfce/exo/start"
source = f"$(XFCE_SITE)/xfce/exo/{pkgver[:-2]}/exo-{pkgver}.tar.bz2"
sha256 = "4277f799245f1efde01cd917fd538ba6b12cf91c9f8a73fe2035fd5456ec078d"
options = ["!lintpixmaps"]


@subpackage("exo-devel")
def _(self):
    return self.default_devel()
