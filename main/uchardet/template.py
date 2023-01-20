pkgname = "uchardet"
pkgver = "0.0.7"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Encoding detector library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-1.1"
url = "https://www.freedesktop.org/wiki/Software/uchardet"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "3fc79408ae1d84b406922fa9319ce005631c95ca0f34b205fad867e8b30e45b1"
# unmarked api
hardening = ["!vis"]

@subpackage("uchardet-devel")
def _devel(self):
    return self.default_devel()

@subpackage("uchardet-progs")
def _progs(self):
    return self.default_progs()
