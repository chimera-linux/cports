pkgname = "spirv-llvm-translator"
pkgver = "13.0.0"
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
makedepends = ["llvm-devel", "llvm-static"]
pkgdesc = "API and commands for processing SPIR-V modules"
maintainer = "q66 <q66@chimera-linux.org>"
license = "NCSA"
url = "https://github.com/KhronosGroup/SPIRV-LLVM-Translator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b416c06525c8724be628327565956c418755fbb471b4fe23d040ca56e1a79061"
# tests disabled
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_bin("build/tools/llvm-spirv/llvm-spirv")

@subpackage("spirv-llvm-translator-devel")
def _devel(self):
    return self.default_devel()
