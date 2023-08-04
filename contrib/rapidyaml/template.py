pkgname = "rapidyaml"
pkgver = "0.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DRYML_BUILD_API=ON",
]
hostmakedepends = [
    "cmake",
    "git",
    "ninja",
    "pkgconf",
    "python",
    "swig",
]
makedepends = [
    "python-devel",
]
pkgdesc = "Library to parse and emit yaml"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/biojppm/rapidyaml"
_c4core = "869f64593421835930c582973c6c6d30889ac955"
_cmake = "95b2410e31ebf28b56a4fffffef52c7d13d657ad"
_debugbreak = "5dcbe41d2bd4712c8014aa7e843723ad7b40fd74"
_fast_float = "v5.2.0"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/biojppm/c4core/archive/{_c4core}.tar.gz",
    f"https://github.com/biojppm/cmake/archive/{_cmake}.tar.gz",
    f"https://github.com/biojppm/debugbreak/archive/{_debugbreak}.tar.gz",
    f"https://github.com/fastfloat/fast_float/archive/refs/tags/{_fast_float}.tar.gz",
]
source_paths = [
    ".",
    "ext/c4core",
    "ext/c4core/cmake",
    "ext/c4core/src/c4/ext/debugbreak",
    "ext/c4core/src/c4/ext/fast_float",
]
sha256 = [
    "8cad74d721ebab6f6e4909a9622ca27491c3b742782f55db4991a0b9de7422f3",
    "3f18ba1eec3b59329aefe03728a694abe858f88289f5d3fd162f55f6923af73f",
    "6b124fda0f4774123c002b2099b9513987062cdef1f9cb635cf4b95d967ac91b",
    "4b424d23dad957937c57c142648d32571a78a6c6b2e473709748e5c1bb8a0f92",
    "72bbfd1914e414c920e39abdc81378adf910a622b62c45b4c61d344039425d18",
]
# vis breaks the symbols
hardening = []
# FIXME: needs even more submodules..
options = ["!check"]


def post_install(self):
    dd = self.destdir
    self.install_license("LICENSE.txt")
    # not linked from submodule..
    for f in (dd / "usr/lib").glob("libc4core*"):
        f.unlink()
    # trash
    self.rm(dd / "usr/ryml.py")
    self.rm(dd / "usr/_ryml.so")


@subpackage("rapidyaml-devel")
def _devel(self):
    return self.default_devel()
