pkgname = "spirv-llvm-translator"
pkgver = "14.0.0_pre0"
pkgrel = 0
_commit = "e95eb30ace4954a3a7e8e17a3cc22f7382d4a47e"
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
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "00ef6119686965c224317aa26c2c4efa8d72907399e852d69b009cfb993fb861"
# tests disabled
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_bin("build/tools/llvm-spirv/llvm-spirv")

@subpackage("spirv-llvm-translator-devel")
def _devel(self):
    return self.default_devel()
