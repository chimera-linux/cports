pkgname = "vectorscan"
pkgver = "5.4.11"
pkgrel = 0
archs = ["aarch64", "ppc64le", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_SKIP_INSTALL_RPATH=ON",
    "-DBUILD_SHARED_LIBS=ON",
    "-DFAT_RUNTIME=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "ragel"]
makedepends = ["boost-devel", "sqlite-devel"]
pkgdesc = "High-performance regular expression matching library"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "BSD-3-Clause"
url = "https://www.vectorcamp.gr/vectorscan"
source = f"https://github.com/vectorcamp/vectorscan/archive/refs/tags/vectorscan/{pkgver}.zip"
sha256 = "f9c342eb067d69826481a40dd5c674373f2fa64d88e58d1cabc052070a70255b"


def do_check(self):
    self.do("build/bin/unit-hyperscan")


def post_install(self):
    self.install_bin("build/bin/hsbench")
    self.install_bin("build/bin/hscheck")
    self.install_license("LICENSE")


@subpackage("vectorscan-devel")
def _devel(self):
    return self.default_devel()


@subpackage("vectorscan-progs")
def _subpkg(self):
    self.pkgdesc = f"{pkgdesc} (command line tools)"
    return self.default_progs()
