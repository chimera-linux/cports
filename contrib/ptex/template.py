pkgname = "ptex"
pkgver = "2.4.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DPTEX_BUILD_STATIC_LIBS=OFF"]
make_check_args = ["-j1"]
hostmakedepends = ["cmake", "ninja", "doxygen"]
makedepends = ["zlib-devel"]
pkgdesc = "Texture mapping library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://ptex.us"
source = f"https://github.com/wdas/ptex/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c8235fb30c921cfb10848f4ea04d5b662ba46886c5e32ad5137c5086f3979ee1"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("ptex-devel")
def _devel(self):
    return self.default_devel()
