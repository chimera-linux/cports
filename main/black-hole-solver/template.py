pkgname = "black-hole-solver"
pkgver = "1.14.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUSE_SYSTEM_XXHASH=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "perl",
    "perl-path-tiny",
    "pkgconf",
    "python",
]
makedepends = [
    "rinutils",
    "xxhash-devel",
]
checkdepends = ["perl-env-path"]
pkgdesc = "Solver for various solitaire card games"
license = "MIT"
url = "https://github.com/shlomif/black-hole-solitaire"
source = f"https://fc-solve.shlomifish.org/downloads/fc-solve/black-hole-solver-{pkgver}.tar.xz"
sha256 = "5c47bd093dbb160f4b090fd670ab7c12b4371d39b17b3bbd8c6c4a12975557c0"
# needs another 10 perl modules
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("black-hole-solver-devel")
def _(self):
    return self.default_devel()
