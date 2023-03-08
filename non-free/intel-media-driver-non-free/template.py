# keep this in sync with contrib/intel-media-driver
pkgname = "intel-media-driver-non-free"
pkgver = "22.6.6"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_NONFREE_KERNELS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libva-devel", "gmmlib-devel", "libx11-devel", "linux-headers"]
depends = ["!intel-media-driver"]
pkgdesc = "Intel® Media Driver for VAAPI"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause AND MIT"
url = "https://foo.software"
source = f"https://github.com/intel/media-driver/archive/refs/tags/intel-media-{pkgver}.tar.gz"
sha256 = "b553290e829dfd824eb62295c9f07dbe8062ce7998f7c527cc92856d0792562d"
# no tests
options = ["!check"]


@subpackage("intel-media-driver-non-free-devel")
def _devel(self):
    return self.default_devel()
