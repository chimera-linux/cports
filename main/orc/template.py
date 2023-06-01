pkgname = "orc"
pkgver = "0.4.34"
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
sha256 = "8f47abb3f097171e44eb807adcdabd860fba2effd37d8d3c4fbd5f341cadd41f"


def post_install(self):
    self.install_license("COPYING")


@subpackage("orc-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/gtk-doc"])
