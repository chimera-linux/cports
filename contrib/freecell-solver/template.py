pkgname = "freecell-solver"
pkgver = "6.8.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/shlomif/fc-solve"
source = f"https://fc-solve.shlomifish.org/downloads/fc-solve/freecell-solver-{pkgver}.tar.xz"
sha256 = "95f78a4b15d2fa340271fe4fcc5354065968191ba22db0d40e81b291b8d53d32"


def post_install(self):
    self.install_license("COPYING.txt")


@subpackage("freecell-solver-devel")
def _devel(self):
    return self.default_devel()
