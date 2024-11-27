pkgname = "freecell-solver"
pkgver = "6.12.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/shlomif/fc-solve"
source = f"https://fc-solve.shlomifish.org/downloads/fc-solve/freecell-solver-{pkgver}.tar.xz"
sha256 = "a2b89e804ce4b918ef749031676210f2095fea3a8cb129805602843c7c4884a0"


def post_install(self):
    self.install_license("COPYING.txt")


@subpackage("freecell-solver-devel")
def _(self):
    return self.default_devel()
