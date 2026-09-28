pkgname = "libqrtr-glib"
pkgver = "1.4.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gobject-introspection"]
makedepends = ["glib-devel", "linux-headers"]
pkgdesc = "Qualcomm IPC Router protocol helper library"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib"
source = f"{url}/-/archive/{pkgver}/libqrtr-glib-{pkgver}.tar.gz"
sha256 = "9e5f988c6005af347f6d0ac95c872e473c9c10c3ec3714ee0b73d896db7d5766"


@subpackage("libqrtr-glib-devel")
def _(self):
    return self.default_devel()
