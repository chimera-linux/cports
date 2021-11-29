pkgname = "libclc"
pkgver = "13.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
hostmakedepends = [
    "cmake", "ninja", "pkgconf", "llvm-devel", "python", "libedit-devel",
    "libffi-devel", "ncurses-devel", "zlib-devel", "spirv-llvm-translator",
]
pkgdesc = "Open implementation of the OpenCL C programming language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://libclc.llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/{pkgname}-{pkgver}.src.tar.xz"
sha256 = "7dc0131f05842a8ed29997362de260c82e188aa0639e482683ece8b47cca21b2"
# external-calls-clspv broken
options = ["!check", "lto"]

# configure with host toolchain
def do_configure(self):
    from cbuild.util import cmake

    with self.profile("host"):
        cmake.configure(self, self.cmake_dir)
