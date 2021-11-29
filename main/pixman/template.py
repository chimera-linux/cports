pkgname = "pixman"
pkgver = "0.40.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgnu-inline-asm=enabled",
    "-Dlibpng=enabled",
    "-Dgtk=disabled",
    "-Dopenmp=disabled",
    "-Diwmmxt=disabled",
]
hostmakedepends = ["meson", "pkgconf", "perl"]
makedepends = ["linux-headers", "libpng-devel"]
pkgdesc = "Library of low-level pixel manipulation routines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pixman.org"
source = f"https://www.cairographics.org/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "6d200dec3740d9ec4ec8d1180e25779c00bc749f94278c8b9021f5534db223fc"
# needs a lot larger stack than musl default
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}

def post_install(self):
    self.install_license("COPYING")

@subpackage("pixman-static")
def _static(self):
    return self.default_static()

@subpackage("pixman-devel")
def _devel(self):
    return self.default_devel()
