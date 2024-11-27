pkgname = "black-hole-solver"
pkgver = "1.12.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/shlomif/black-hole-solitaire"
source = f"https://fc-solve.shlomifish.org/downloads/fc-solve/black-hole-solver-{pkgver}.tar.xz"
sha256 = "d32f32536f7573292588f41bb0d85ae42d561376c218dc4ab6badfe4904a37a7"
# needs another 10 perl modules
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("black-hole-solver-devel")
def _(self):
    return self.default_devel()
