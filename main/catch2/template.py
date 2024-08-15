pkgname = "catch2"
pkgver = "3.7.0"
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
sha256 = "5b10cd536fa3818112a82820ce0787bd9f2a906c618429e7c4dea639983c8e88"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("catch2-devel")
def _devel(self):
    return self.default_devel()
