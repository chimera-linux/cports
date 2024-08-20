pkgname = "orc"
pkgver = "0.4.39"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dexamples=disabled",
]
hostmakedepends = [
    "gtk-doc-tools",
    "meson",
    "pkgconf",
]
makedepends = ["linux-headers"]
pkgdesc = "Optimized Inner Loop Runtime Compiler"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/orc/orc-{pkgver}.tar.xz"
sha256 = "33ed2387f49b825fa1b9c3b0072e05f259141b895474ad085ae51143d3040cc0"


def post_install(self):
    self.install_license("COPYING")


@subpackage("orc-devel")
def _(self):
    return self.default_devel(extra=["usr/share/gtk-doc"])
