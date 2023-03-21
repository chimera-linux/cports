pkgname = "libqmi"
pkgver = "1.30.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static", "--enable-mbim-qmux", "--enable-qrtr",
    "--enable-introspection"
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "glib-devel", "libgudev-devel", "libmbim-devel",
    "libqrtr-glib-devel", "gobject-introspection"
]
makedepends = ["glib-devel", "libgudev-devel", "linux-headers"]
pkgdesc = "QMI modem protocol helper library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/libqmi"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "862482ce9e3ad0bd65d264334ee311cdb94b9df2863b5b7136309b41b8ac1990"

@subpackage("libqmi-devel")
def _devel(self):
    return self.default_devel()
