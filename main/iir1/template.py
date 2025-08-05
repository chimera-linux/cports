pkgname = "iir1"
pkgver = "1.10.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DIIR1_BUILD_DEMO=OFF", "-DIIR1_INSTALL_STATIC=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "DSP IIR realtime filter library written in C++"
license = "MIT"
url = "https://berndporr.github.io/iir1"
source = f"https://github.com/berndporr/iir1/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "13b53f14d276adf6cafd3564fcda1d4b3e72342108d1c40ec4b4f0c7fc3ac95a"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("iir1-devel")
def _(self):
    return self.default_devel()
