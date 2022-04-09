pkgname = "libqmi"
pkgver = "1.30.4"
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
sha256 = "00d7da30a4f8d1185f37cba289cfaf1dfcd04a58f2f76d6acfdf5b85312d6ed6"

@subpackage("libqmi-devel")
def _devel(self):
    return self.default_devel()
