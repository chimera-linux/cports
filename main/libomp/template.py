pkgname = "libomp"
pkgver = "21.1.8"
pkgrel = 0
archs = ["aarch64", "loongarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DLIBOMP_ENABLE_SHARED=ON",
    "-DLIBOMP_INSTALL_ALIASES=ON",
    "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
]
hostmakedepends = ["clang-tools-extra", "cmake", "ninja", "perl", "python"]
makedepends = [
    "libffi8-devel",
    "linux-headers",
    "llvm-devel",
    "ncurses-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "LLVM OpenMP runtime"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "4633a23617fa31a3ea51242586ea7fb1da7140e426bd62fc164261fe036aa142"
# no lit
options = ["!check"]

cmake_dir = "openmp"


def post_install(self):
    for f in (self.destdir / "usr/lib").glob("libomp.so.*"):
        self.install_link("usr/lib/libomp.so", f.name)
    self.install_license("LICENSE.TXT")


@subpackage("libomp-devel-static")
def _(self):
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]


@subpackage("libomp-devel")
def _(self):
    self.depends = [self.with_pkgver("libomp-devel-static")]

    # keep libomptarget symlinks in main
    return [
        "usr/include",
        "usr/lib/libomp.so",
        "usr/lib/libgomp.so",
        "usr/lib/libiomp5.so",
        "usr/lib/cmake/openmp",
    ]
