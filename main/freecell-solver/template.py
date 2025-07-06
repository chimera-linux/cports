pkgname = "freecell-solver"
pkgver = "6.14.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # needs a million more perl things
    "-DFCS_WITH_TEST_SUITE=OFF",
]
hostmakedepends = [
    "cmake",
    "gperf",
    "ninja",
    "perl-moo",
    "perl-path-tiny",
    "perl-template-toolkit",
    "pkgconf",
    "python-cffi",
    "python-pysol_cards",
    "python-random2",
    "python-six",
]
makedepends = [
    "gmp-devel",
    "rinutils",
]
depends = [
    "python-pysol_cards",
    "python-six",
]
pkgdesc = "Solver for various Freecell-based solitaire games"
license = "MIT"
url = "https://github.com/shlomif/fc-solve"
source = f"https://fc-solve.shlomifish.org/downloads/fc-solve/freecell-solver-{pkgver}.tar.xz"
sha256 = "1d1125d85422bcd521102d7cb1e7c84b76863fe445dd21879f9779dc6b2ce7dc"


def post_install(self):
    self.install_license("COPYING.txt")


@subpackage("freecell-solver-devel")
def _(self):
    return self.default_devel()
