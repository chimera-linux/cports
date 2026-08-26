pkgname = "libqmi"
pkgver = "1.38.0"
pkgrel = 0
build_style = "meson"
configure_args = [
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
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/libqmi"
source = f"https://gitlab.freedesktop.org/mobile-broadband/libqmi/-/archive/{pkgver}/libqmi-{pkgver}.tar.gz"
sha256 = "8ee3b3a9002f2b45c825deade85710db006e01674f5f9359d351c192cc926015"


@subpackage("libqmi-devel")
def _(self):
    return self.default_devel()
