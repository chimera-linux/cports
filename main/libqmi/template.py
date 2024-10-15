pkgname = "libqmi"
pkgver = "1.34.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dqrtr=true",
    "-Dintrospection=true",
]
hostmakedepends = [
    "bash-completion",
    "glib-devel",
    "gobject-introspection",
    "help2man",
    "libgudev-devel",
    "libmbim-devel",
    "libqrtr-glib-devel",
    "meson",
    "pkgconf",
]
makedepends = ["glib-devel", "libgudev-devel", "linux-headers"]
pkgdesc = "QMI modem protocol helper library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/libqmi"
source = f"https://gitlab.freedesktop.org/mobile-broadband/libqmi/-/archive/{pkgver}/libqmi-{pkgver}.tar.gz"
sha256 = "8690d25b4d110b6df28b31da0a8bf16c7e966d31abcfeeb854f2753451e7a400"


@subpackage("libqmi-devel")
def _(self):
    return self.default_devel()
