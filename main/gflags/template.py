pkgname = "gflags"
pkgver = "2.2.2"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_STATIC_LIBS=ON",
    "-DBUILD_TESTING=ON",
    "-DREGISTER_INSTALL_PREFIX=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Google C++ argparse library"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/gflags/gflags"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "34af2f15cf7367513b352bdcd2493ab14ce43692d2dcd9dfc499492966c64dcf"
# FIXME: cfi fails half the tests, vis breaks some symbols
hardening = []


def post_install(self):
    self.install_license("COPYING.txt")
    # useless completion script
    self.uninstall("usr/bin/gflags_completions.sh")


@subpackage("gflags-devel")
def _devel(self):
    return self.default_devel()
