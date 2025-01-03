pkgname = "ptex"
pkgver = "2.4.3"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DPTEX_BUILD_STATIC_LIBS=OFF"]
make_check_args = ["-j1"]
hostmakedepends = ["cmake", "ninja", "doxygen", "pkgconf"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "Texture mapping library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://ptex.us"
source = f"https://github.com/wdas/ptex/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "435aa2ee1781ff24859bd282b7616bfaeb86ca10604b13d085ada8aa7602ad27"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("ptex-devel")
def _(self):
    return self.default_devel()
