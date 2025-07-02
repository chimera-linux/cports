pkgname = "libclc"
pkgver = "20.1.7"
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
sha256 = "22b29c1a9f18d8744e5a24f36ce6d4f198d523c126cd7182569c73806e1e1854"
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
