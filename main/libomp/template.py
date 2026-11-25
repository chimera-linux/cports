pkgname = "libomp"
pkgver = "23.1.6"
pkgrel = 0
archs = ["aarch64", "loongarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DLIBOMP_ENABLE_SHARED=ON",
    "-DLIBOMP_INSTALL_ALIASES=ON",
    "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
    "-DLLVM_ENABLE_RUNTIMES=openmp",
]
cmake_dir = "runtimes"
hostmakedepends = ["cmake", "ninja", "perl", "python"]
makedepends = [
    "libffi8-devel",
    "linux-headers",
    "llvm-devel",
    "llvm-runtimes-devel-static",
    "ncurses-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "LLVM OpenMP runtime"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "d3b86ab29cfb4445a6652e5c2642ccc75e04e38084dde3701d323320f35a31da"
# no lit
options = ["!check", "llvmflags"]


def post_install(self):
    for f in (self.destdir / "usr/lib").glob("libomp.so.*"):
        self.install_link("usr/lib/libomp.so", f.name)
    self.install_license("LICENSE.TXT")


@split("devel-static")
def _(self):
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]


@split("devel")
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
