pkgname = "libclc"
pkgver = "16.0.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
hostmakedepends = [
    "cmake", "ninja", "pkgconf", "llvm-devel", "python", "libedit-devel",
    "libffi-devel", "ncurses-devel", "zlib-devel", "spirv-llvm-translator",
    "clang-tools-extra",
]
pkgdesc = "Open implementation of the OpenCL C programming language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://libclc.llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/{pkgname}-{pkgver}.src.tar.xz"
sha256 = "6d13cd1d4c1e5dbde90a67b1c5aa2545cddeb50b6f821f0ad9acc6f525bccf4e"
# should not matter much but FIXME
hardening = ["vis", "!cfi"]
# external-calls-clspv broken
options = ["!check"]

# configure with host toolchain
def do_configure(self):
    from cbuild.util import cmake

    with self.profile("host"):
        cmake.configure(self, self.cmake_dir)
