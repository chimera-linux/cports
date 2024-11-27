pkgname = "libsbsms"
pkgver = "2.3.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Library for high quality time and pitch scale modification"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/claytonotey/libsbsms"
source = (
    f"https://github.com/claytonotey/libsbsms/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "4f88d152bc06fedbda9d5d65517d40254a7310c9050601a93122309d45afd2c9"
# vis breaks symbols
hardening = []


@subpackage("libsbsms-devel")
def _(self):
    return self.default_devel()
