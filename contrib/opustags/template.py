pkgname = "opustags"
pkgver = "1.9.0"
pkgrel = 0
build_style = "cmake"
make_check_target = "check"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["libogg-devel"]
checkdepends = [
    "perl",
    "perl-list-moreutils",
    "perl-test-deep",
]
pkgdesc = "Ogg Opus tag editor"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/fmang/opustags"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ea937f48a011bbacf37324c159149625c1ab66110e6d279693a92659bd38cf02"
hardening = ["vis", "cfi"]
# TODO: unpackaged perl modules
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
