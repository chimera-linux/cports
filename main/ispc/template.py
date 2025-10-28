pkgname = "ispc"
pkgver = "1.28.2"
pkgrel = 0
archs = ["x86_64", "aarch64", "armv7"]
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
make_check_target = "check-all"
hostmakedepends = [
    "bison",
    "cmake",
    "flex",
    "llvm-tools",
    "ninja",
    "python",
]
makedepends = [
    "clang-devel",
    "llvm-devel",
    "ncurses-devel",
    "onetbb-devel",
    "python-devel",
    "python-nanobind-devel",
]
pkgdesc = "Implicit SPMD program compiler"
license = "BSD-3-Clause"
url = "https://ispc.github.io"
source = f"https://github.com/ispc/ispc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0b7d1d73afa93c015814b99c97b88fa45bce822d7904e8fc4a95666ba8e3fb92"
tool_flags = {
    # `warning: '_FORTIFY_SOURCE' macro redefined` noise
    "CXXFLAGS": ["-Wno-macro-redefined"],
}


def pre_check(self):
    # expects a commit id in the output
    self.rm("tests/lit-tests/llvm_ident.ispc")
    # fails to compile
    self.rm("tests/lit-tests/ispc-jit-error-handling.cpp")


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("ispc-libs")
def _(self):
    return self.default_libs()


@subpackage("ispc-devel")
def _(self):
    return self.default_devel()
