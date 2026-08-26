pkgname = "libmbim"
pkgver = "1.34.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=true",
]
hostmakedepends = [
    "bash-completion",
    "glib-devel",
    "gobject-introspection",
    "help2man",
    "libgudev-devel",
    "meson",
    "pkgconf",
]
makedepends = ["glib-devel", "libgudev-devel", "linux-headers"]
pkgdesc = "MBIM modem protocol helper library"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/libmbim"
source = f"https://gitlab.freedesktop.org/mobile-broadband/libmbim/-/archive/{pkgver}/libmbim-{pkgver}.tar.gz"
sha256 = "55bb88df358f8a36b6e01e63877500d7c6420f5907d2d3101812b4912eabe08f"


@subpackage("libmbim-devel")
def _(self):
    return self.default_devel()
