pkgname = "libclc"
pkgver = "22.1.6"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
hostmakedepends = [
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
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "6e0b376a1f6d9873e7dfb09ae6e04b9c7024400f01733fa4c29be69d5c138bc2"
hardening = ["vis", "!cfi"]
# external-calls-clspv broken
options = ["!check"]

cmake_dir = "libclc"


# configure with host toolchain
def configure(self):
    from cbuild.util import cmake

    with self.profile("host"):
        cmake.configure(self, "build", self.cmake_dir)


def post_install(self):
    self.install_license("LICENSE.TXT")
