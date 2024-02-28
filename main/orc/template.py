pkgname = "orc"
pkgver = "0.4.38"
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
sha256 = "a55a98d4772567aa3faed8fb84d540c3db77eaba16d3e2e10b044fbc9228668d"


def post_install(self):
    self.install_license("COPYING")


@subpackage("orc-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/gtk-doc"])
