pkgname = "libclc"
pkgver = "14.0.6"
pkgrel = 0
build_wrksrc = f"{pkgname}-{pkgver}.src"
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
sha256 = "c9b183160ec093b4bd4a24517ab97b30110418b8d904a849c415dc647b345f95"
# external-calls-clspv broken
options = ["!check"]

# configure with host toolchain
def do_configure(self):
    from cbuild.util import cmake

    with self.profile("host"):
        cmake.configure(self, self.cmake_dir)
