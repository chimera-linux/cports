pkgname = "libclc"
pkgver = "21.1.8"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
hostmakedepends = [
    "clang-tools-extra",
    "cmake",
    "libedit-devel",
    "libffi8-devel",
    "llvm-devel",
    "ncurses-devel",
    "ninja",
    "pkgconf",
    "python",
    "spirv-llvm-translator",
    "zlib-ng-compat-devel",
]
pkgdesc = "Open implementation of the OpenCL C programming language"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://libclc.llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/libclc-{pkgver}.src.tar.xz"
sha256 = "6c2677362a53531c35edf482bdc9171ea0471ca0a1e9138ac9b5a1782925616f"
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
