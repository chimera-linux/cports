pkgname = "libqrtr-glib"
pkgver = "1.2.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gobject-introspection"]
makedepends = ["glib-devel", "linux-headers"]
pkgdesc = "Qualcomm IPC Router protocol helper library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c5cdf5ea91cbd2cf2758b2896064c7b1dfe7156063267df905f957ac69b6b763"


@subpackage("libqrtr-glib-devel")
def _devel(self):
    return self.default_devel()
