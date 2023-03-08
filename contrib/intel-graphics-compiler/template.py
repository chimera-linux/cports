pkgname = "intel-graphics-compiler"
pkgver = "1.0.12812.26"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # Use LLVM 15
    "-DIGC_OPTION__LLVM_PREFERRED_VERSION=15",
    # make IGC use system libs and headers
    "-DIGC_OPTION__SPIRV_TOOLS_MODE=Prebuilds", "-DIGC_OPTION__USE_PREINSTALLED_SPRIV_HEADERS=ON",
    "-DIGC_OPTION__VC_INTRINSICS_MODE=Prebuilds"
]
hostmakedepends = ["cmake", "ninja", "clang-tools-extra", "pkgconf", "bison", "flex", "python"]
makedepends = ["vc-intrinsics-devel-static", "opencl-clang-devel", "spirv-llvm-translator-devel", "llvm-devel",
               "spirv-headers", "spirv-tools-devel", "zlib-devel", "lld-devel", "linux-headers"]
pkgdesc = "Intel® Graphics Compiler for OpenCL™"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://github.com/intel/intel-graphics-compiler"
source = f"https://github.com/intel/intel-graphics-compiler/archive/refs/tags/igc-{pkgver}.tar.gz"
sha256 = "d1a8ff080ea3836b4dd5bba4b49774abe0970c40e4becbd0a7d74f665bda3d83"
# generates some fun UD opcodes
hardening = ["!int"]
# needs lit
options = ["!check"]


@subpackage("intel-graphics-compiler-devel")
def _devel(self):
    return self.default_devel()
