pkgname = "opustags"
pkgver = "1.10.0"
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
sha256 = "761d3ac036205b9193bc6a610c3610c401d89fde2c955acfa7e26b1328e190b7"
hardening = ["vis", "cfi"]
# TODO: unpackaged perl modules
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
