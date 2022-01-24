pkgname = "libqmi"
pkgver = "1.30.2"
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
makedepends = ["libglib-devel", "libgudev-devel", "linux-headers"]
pkgdesc = "QMI modem protocol helper library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/libqmi"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "be01ece0ea2c2194cbea5744bf5aaf06c04ba5fb7ec7887a13116c76d114fedd"

@subpackage("libqmi-devel")
def _devel(self):
    return self.default_devel()
