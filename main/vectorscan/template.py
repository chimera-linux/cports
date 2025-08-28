pkgname = "vectorscan"
pkgver = "5.4.12"
pkgrel = 0
archs = ["aarch64", "ppc64le", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_CXX_FLAGS=-Wno-error=deprecated-declarations",
    "-DCMAKE_SKIP_INSTALL_RPATH=ON",
    "-DBUILD_SHARED_LIBS=ON",
    "-DFAT_RUNTIME=OFF",
    "-DBUILD_BENCHMARKS=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "ragel"]
makedepends = ["boost-devel", "sqlite-devel"]
pkgdesc = "High-performance regular expression matching library"
license = "BSD-3-Clause"
url = "https://www.vectorcamp.gr/vectorscan"
source = f"https://github.com/vectorcamp/vectorscan/archive/refs/tags/vectorscan/{pkgver}.tar.gz"
sha256 = "1ac4f3c038ac163973f107ac4423a6b246b181ffd97fdd371696b2517ec9b3ed"


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
