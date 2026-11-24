pkgname = "ispc"
pkgver = "1.32.0"
pkgrel = 0
archs = ["x86_64", "aarch64", "armv7"]
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
make_check_target = "check-all"
hostmakedepends = [
    "bison",
    "cmake",
    "flex",
    "ninja",
    "python",
]
makedepends = [
    "llvm-clang-devel",
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
sha256 = "705b818062602a0c6b62965a8aa011508ef7f9decce716cf1645f2b04ba1e9f8"
tool_flags = {
    # `warning: '_FORTIFY_SOURCE' macro redefined` noise
    "CXXFLAGS": ["-Wno-macro-redefined"],
}
options = ["llvmflags"]


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
