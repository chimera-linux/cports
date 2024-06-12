pkgname = "iir1"
pkgver = "1.9.4"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DIIR1_BUILD_DEMO=OFF", "-DIIR1_INSTALL_STATIC=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "DSP IIR realtime filter library written in C++"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://berndporr.github.io/iir1"
source = f"https://github.com/berndporr/iir1/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "67d0982356f33fd37522e4711cda12f70a981a9c83de332386f89de3d7601d2b"
# FIXME: vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("iir1-devel")
def _devel(self):
    return self.default_devel()
