pkgname = "libclc"
pkgver = "20.1.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "llvm-devel",
    "python",
    "libedit-devel",
    "libffi8-devel",
    "ncurses-devel",
    "zlib-ng-compat-devel",
    "spirv-llvm-translator",
    "clang-tools-extra",
]
pkgdesc = "Open implementation of the OpenCL C programming language"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://libclc.llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/libclc-{pkgver}.src.tar.xz"
sha256 = "bc5050fd1bcb7383da37fa13f9d7c075cfa0de2d7f86a6385a62517fdb815630"
hardening = ["vis", "!cfi"]
# external-calls-clspv broken
options = ["!check"]


# configure with host toolchain
def configure(self):
    from cbuild.util import cmake

    with self.profile("host"):
        cmake.configure(self, "build", self.cmake_dir)


def post_install(self):
    self.install_license("LICENSE.TXT")
