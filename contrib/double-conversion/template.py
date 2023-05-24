pkgname = "double-conversion"
pkgver = "3.2.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTING=ON", "-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Efficient binary-decimal and decimal-binary routines for doubles"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/google/double-conversion"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e40d236343cad807e83d192265f139481c51fc83a1c49e406ac6ce0a0ba7cd35"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("double-conversion-devel")
def _devel(self):
    return self.default_devel()
