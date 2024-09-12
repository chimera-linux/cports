pkgname = "orc"
pkgver = "0.4.40"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/orc/orc-{pkgver}.tar.xz"
sha256 = "3fc2bee78dfb7c41fd9605061fc69138db7df007eae2f669a1f56e8bacef74ab"


def post_install(self):
    self.install_license("COPYING")


@subpackage("orc-devel")
def _(self):
    return self.default_devel(extra=["usr/share/gtk-doc"])
