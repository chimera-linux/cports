pkgname = "libclc"
pkgver = "20.1.4"
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
sha256 = "08d792747dd08aa0fb3378f5dd4275d7fcb4b286db54eb3f6f9ce3548e13397a"
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
