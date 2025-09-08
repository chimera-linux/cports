pkgname = "vectorscan"
pkgver = "5.4.11"
pkgrel = 6
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
license = "BSD-3-Clause"
url = "https://www.vectorcamp.gr/vectorscan"
source = f"https://github.com/vectorcamp/vectorscan/archive/refs/tags/vectorscan/{pkgver}.tar.gz"
sha256 = "905f76ad1fa9e4ae0eb28232cac98afdb96c479666202c5a4c27871fb30a2711"


def check(self):
    self.do("build/bin/unit-hyperscan")


def post_install(self):
    self.install_bin("build/bin/hsbench")
    self.install_bin("build/bin/hscheck")
    self.install_license("LICENSE")


@subpackage("vectorscan-devel")
def _(self):
    return self.default_devel()


@subpackage("vectorscan-progs")
def _(self):
    self.subdesc = "command line tools"
    return self.default_progs()
