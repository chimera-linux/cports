pkgname = "catch2"
pkgver = "3.11.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DCATCH_BUILD_EXTRA_TESTS=ON",
    "-DCATCH_DEVELOPMENT_BUILD=ON",
    "-DCATCH_ENABLE_WERROR=OFF",
]
# differing outputs due to the failed test build patch
make_check_args = ["-E", "(ApprovalTests)"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
checkdepends = ["python"]
pkgdesc = "C++-based test framework"
license = "BSL-1.0"
url = "https://github.com/catchorg/Catch2"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "82fa1cb59dc28bab220935923f7469b997b259eb192fb9355db62da03c2a3137"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("catch2-devel")
def _(self):
    return self.default_devel()
