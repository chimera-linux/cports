pkgname = "libqmi"
pkgver = "1.36.0"
pkgrel = 0
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
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/libqmi"
source = f"https://gitlab.freedesktop.org/mobile-broadband/libqmi/-/archive/{pkgver}/libqmi-{pkgver}.tar.gz"
sha256 = "e254fafdd916a78a27126e6d72ae436662487f59c7de84d4d40286059af89093"


@subpackage("libqmi-devel")
def _(self):
    return self.default_devel()
