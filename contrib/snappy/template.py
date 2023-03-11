pkgname = "snappy"
pkgver = "1.1.10"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=1", "-DSNAPPY_BUILD_TESTS=0",
    "-DSNAPPY_BUILD_BENCHMARKS=0"
]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Fast compressor/decompressor"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://google.github.io/snappy"
source = f"https://github.com/google/snappy/archive/{pkgver}.tar.gz"
sha256 = "49d831bffcc5f3d01482340fe5af59852ca2fe76c3e05df0e67203ebbe0f1d90"
tool_flags = {'CXXFLAGS': ['-Wno-sign-compare']}
# tests depend on in-tree gtest
options = ["!check"]

@subpackage("snappy-devel")
def _devel(self):
    return self.default_devel()
