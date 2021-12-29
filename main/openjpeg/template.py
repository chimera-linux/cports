pkgname = "openjpeg"
pkgver = "2.4.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTING=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libpng-devel", "libtiff-devel", "lcms2-devel"]
pkgdesc = "Open-source JPEG 2000 codec written in C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://www.openjpeg.org"
source = f"https://github.com/uclouvain/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "8702ba68b442657f11aaeb2b338443ca8d5fb95b0d845757968a7be31ef7f16d"
# missing test data
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("openjpeg-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/lib/openjpeg-2.*"])

@subpackage("openjpeg-progs")
def _progs(self):
    return self.default_progs()
