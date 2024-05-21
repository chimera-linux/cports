pkgname = "libclc"
pkgver = "18.1.6"
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
    "libffi-devel",
    "ncurses-devel",
    "zlib-devel",
    "spirv-llvm-translator",
    "clang-tools-extra",
]
pkgdesc = "Open implementation of the OpenCL C programming language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://libclc.llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/libclc-{pkgver}.src.tar.xz"
sha256 = "adb73f49798cc271216ca7368da6991d5562efe7cffe2ad42d411bfa4a5c66dc"
# should not matter much but FIXME
hardening = ["vis", "!cfi"]
# external-calls-clspv broken
options = ["!check"]


# configure with host toolchain
def do_configure(self):
    from cbuild.util import cmake

    with self.profile("host"):
        cmake.configure(self, "build", self.cmake_dir)
