pkgname = "libqrtr-glib"
pkgver = "1.2.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection"
]
makedepends = ["libglib-devel", "linux-headers"]
pkgdesc = "Qualcomm IPC Router protocol helper library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "1f97dc3e3e24ff8cdf26eef671169cc21d715cc63cf065bb24b215a487d56867"

@subpackage("libqrtr-glib-devel")
def _devel(self):
    return self.default_devel()
