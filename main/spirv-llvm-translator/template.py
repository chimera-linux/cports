# not abi-stable in patch versions
# rebuild library consumers on updates (mesa)
pkgname = "spirv-llvm-translator"
pkgver = "21.1.1"
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
    "clang-tools-extra",
    "cmake",
    "ninja",
    "pkgconf",
    "spirv-headers",
    "spirv-tools-devel",
]
makedepends = ["llvm-devel"]
pkgdesc = "API and commands for processing SPIR-V modules"
license = "NCSA"
url = "https://github.com/KhronosGroup/SPIRV-LLVM-Translator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dda46febdb060a1d5cc2ceeb9682ccaf33e55ae294fd0793274531b54f07c46b"
# FIXME int: crashes libclc build
hardening = ["!int"]
# tests disabled
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.TXT")


@subpackage("spirv-llvm-translator-devel")
def _(self):
    return self.default_devel()
