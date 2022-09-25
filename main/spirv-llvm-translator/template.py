pkgname = "spirv-llvm-translator"
pkgver = "15.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    "-DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=/usr/include/spirv",
    "-DLLVM_LINK_LLVM_DYLIB=ON",
    "-DBUILD_SHARED_LIBS=ON",
    "-DCMAKE_SKIP_RPATH=ON",
    "-DLLVM_SPIRV_INCLUDE_TESTS=OFF",
]
make_build_args = ["llvm-spirv"]
hostmakedepends = [
    "cmake", "ninja", "pkgconf", "clang-tools-extra", "spirv-headers"
]
makedepends = ["llvm-devel"]
pkgdesc = "API and commands for processing SPIR-V modules"
maintainer = "q66 <q66@chimera-linux.org>"
license = "NCSA"
url = "https://github.com/KhronosGroup/SPIRV-LLVM-Translator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b1bebd77f72988758c00852e78c2ddc545815a612169a0cb377d021e2f846d88"
# tests disabled
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.TXT")

@subpackage("spirv-llvm-translator-devel")
def _devel(self):
    return self.default_devel()
