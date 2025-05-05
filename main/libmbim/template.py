pkgname = "libmbim"
pkgver = "1.32.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true"]
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
sha256 = "7eca9f5af2eecfdb5e3a2a865a7f29d0ac9532ab187a9c6adce4d85f897eb385"


@subpackage("libmbim-devel")
def _(self):
    return self.default_devel()
