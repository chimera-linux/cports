pkgname = "libclc"
pkgver = "19.1.7"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://libclc.llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/libclc-{pkgver}.src.tar.xz"
sha256 = "77e2d71f5cea1d0b1014ba88186299d1a0848eb3dc20948baae649db9e7641cb"
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
