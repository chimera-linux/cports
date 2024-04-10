pkgname = "catch2"
pkgver = "3.5.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DCATCH_BUILD_EXTRA_TESTS=ON",
    "-DCATCH_DEVELOPMENT_BUILD=ON",
    "-DCATCH_ENABLE_WERROR=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
checkdepends = ["python"]
pkgdesc = "C++-based test framework"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSL-1.0"
url = "https://github.com/catchorg/Catch2"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b7754b711242c167d8f60b890695347f90a1ebc95949a045385114165d606dbb"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("catch2-devel")
def _devel(self):
    return self.default_devel()
