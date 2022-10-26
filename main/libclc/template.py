pkgname = "libclc"
pkgver = "15.0.3"
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
sha256 = "07e8a2b31e07a8cc8a976a6bfd87797d2543d5a9530f449755bf5119acbdbe8e"
# external-calls-clspv broken
options = ["!check"]

# configure with host toolchain
def do_configure(self):
    from cbuild.util import cmake

    with self.profile("host"):
        cmake.configure(self, self.cmake_dir)
