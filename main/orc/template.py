pkgname = "orc"
pkgver = "0.4.35"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=disabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gtk-doc-tools",
]
makedepends = ["linux-headers"]
pkgdesc = "Optimized Inner Loop Runtime Compiler"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "718cdb60db0d5f7d4fc8eb955cd0f149e0ecc78dcd5abdc6ce3be95221b793b9"


def post_install(self):
    self.install_license("COPYING")


@subpackage("orc-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/gtk-doc"])
