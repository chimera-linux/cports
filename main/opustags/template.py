pkgname = "opustags"
pkgver = "1.10.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/fmang/opustags"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "703096e9c41481e30ab90eefdd8fafc4c3a138998b3f8281aa4f023e7058bc86"
hardening = ["vis", "cfi"]
# TODO: unpackaged perl modules
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
