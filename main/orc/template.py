pkgname = "orc"
pkgver = "0.4.37"
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
sha256 = "85638c0d447d989cd0d7e03406adbfbc380e67db2a622a4727a0ce3d440b2974"


def post_install(self):
    self.install_license("COPYING")


@subpackage("orc-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/gtk-doc"])
