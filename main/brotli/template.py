pkgname = "brotli"
pkgver = "1.0.9"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "General-purpose lossless compression algorithm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/google/brotli"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f9e8d81d0405ba66d181529af42a3354f838c939095ff99930da6aa9cdf6fe46"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("brotli-devel")
def _devel(self):
    return self.default_devel()
