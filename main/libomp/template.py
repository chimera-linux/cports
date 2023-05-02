pkgname = "libomp"
pkgver = "16.0.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIBOMP_ENABLE_SHARED=YES",
    "-DLIBOMP_INSTALL_ALIASES=YES",
]
hostmakedepends = ["cmake", "ninja", "python", "perl", "clang-tools-extra"]
makedepends = [
    "llvm-devel", "libffi-devel", "zlib-devel", "elftoolchain-devel",
    "ncurses-devel", "linux-headers"
]
pkgdesc = "LLVM OpenMP runtime"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "6d8acae041ccd34abe144cda6eaa76210e1491f286574815b7261b3f2e58734c"
# no lit
options = ["!check"]

cmake_dir = "openmp"

tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC"],
}

def post_install(self):
    for f in (self.destdir / "usr/lib").glob("libomp.so.*"):
        self.install_link(f.name, "usr/lib/libomp.so")

@subpackage("libomp-devel-static")
def _devel_static(self):
    self.pkgdesc = f"{pkgdesc} (static libraries)"
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]

@subpackage("libomp-devel")
def _devel(self):
    self.depends = [
        f"libomp-devel-static={pkgver}-r{pkgrel}"
    ]

    return [
        "usr/include",
        "usr/lib/libomp.so",
        "usr/lib/libgomp.so",
        "usr/lib/libiomp5.so",
        "usr/lib/libomptarget*.bc",
        "usr/lib/cmake/openmp",
    ]
