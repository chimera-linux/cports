pkgname = "libmysofa"
pkgver = "1.3.1"
pkgrel = 0
build_style = "cmake"
# TODO cunit
configure_args = ["-DBUILD_TESTS=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Reader for AES SOFA files to get better HRTFs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/hoene/libmysofa"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a8a8cbf7b0b2508a6932278799b9bf5c63d833d9e7d651aea4622f3bc6b992aa"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libmysofa-devel")
def _devel(self):
    return self.default_devel()
