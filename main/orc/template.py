pkgname = "orc"
pkgver = "0.4.44"
pkgrel = 0
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
license = "BSD-2-Clause"
url = "https://gstreamer.freedesktop.org/modules/orc.html"
source = f"https://gstreamer.freedesktop.org/src/orc/orc-{pkgver}.tar.xz"
sha256 = "4aeb97aea2b58224029dc2b23d7d064cfa990cb4fb8c4da440bcbe9c95bc5d2d"


def post_install(self):
    self.install_license("COPYING")


@subpackage("orc-devel")
def _(self):
    return self.default_devel()
