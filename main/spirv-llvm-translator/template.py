pkgname = "spirv-llvm-translator"
pkgver = "18.1.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=/usr/include/spirv",
    "-DLLVM_LINK_LLVM_DYLIB=ON",
    "-DBUILD_SHARED_LIBS=ON",
    "-DCMAKE_SKIP_RPATH=ON",
    "-DLLVM_SPIRV_INCLUDE_TESTS=OFF",
]
make_build_target = "llvm-spirv"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "clang-tools-extra",
    "spirv-headers",
    "spirv-tools-devel",
]
makedepends = ["llvm-devel"]
pkgdesc = "API and commands for processing SPIR-V modules"
maintainer = "q66 <q66@chimera-linux.org>"
license = "NCSA"
url = "https://github.com/KhronosGroup/SPIRV-LLVM-Translator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6e41f6ebe3ef61c159e47303a97a9631ba9bc00db68a1bb370cc1589df5c73f9"
# FIXME int: crashes libclc build
hardening = ["!int"]
# tests disabled
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.TXT")


@subpackage("spirv-llvm-translator-devel")
def _(self):
    return self.default_devel()
