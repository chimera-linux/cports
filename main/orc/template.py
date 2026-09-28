pkgname = "orc"
pkgver = "0.4.41"
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
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/orc/orc-{pkgver}.tar.xz"
sha256 = "cb1bfd4f655289cd39bc04642d597be9de5427623f0861c1fc19c08d98467fa2"


def post_install(self):
    self.install_license("COPYING")


@subpackage("orc-devel")
def _(self):
    return self.default_devel(extra=["usr/share/gtk-doc"])
