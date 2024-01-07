pkgname = "libmbim"
pkgver = "1.30.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/libmbim"
source = f"https://gitlab.freedesktop.org/mobile-broadband/libmbim/-/archive/{pkgver}/libmbim-{pkgver}.tar.gz"
sha256 = "cfc729d23b9bf699b23a7ef2f5d732d6eff96234e31fed36b778771a6e3d3ee5"


@subpackage("libmbim-devel")
def _devel(self):
    return self.default_devel()
