pkgname = "iir1"
pkgver = "1.9.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DIIR1_BUILD_DEMO=OFF", "-DIIR1_INSTALL_STATIC=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "DSP IIR realtime filter library written in C++"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://berndporr.github.io/iir1"
source = f"https://github.com/berndporr/iir1/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "beb16142e08e5f68010c6e5014dea2276ea49b71a258439eff09c5ee3f781d88"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("iir1-devel")
def _(self):
    return self.default_devel()
