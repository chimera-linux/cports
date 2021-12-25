pkgname = "orc"
pkgver = "0.4.32"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=disabled",
]
hostmakedepends = [
    "meson", "pkgconf", "gtk-doc-tools",
]
makedepends = ["linux-headers"]
pkgdesc = "Optimized Inner Loop Runtime Compiler"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a66e3d8f2b7e65178d786a01ef61f2a0a0b4d0b8370de7ce134ba73da4af18f0"

def post_install(self):
    self.install_license("COPYING")

@subpackage("orc-static")
def _static(self):
    return self.default_static()

@subpackage("orc-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share/gtk-doc"])
