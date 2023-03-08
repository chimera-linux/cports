pkgname = "opencl-clang"
pkgver = "15.0.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "clang-tools-extra"]
makedepends = ["llvm-devel", "zlib-devel", "libffi-devel", "spirv-llvm-translator-devel", "clang-devel"]
pkgdesc = "Wrapper around clang for compiling OpenCL C kernels to SPIR-V modules"
maintainer = "eater <=@eater.me>"
license = "NCSA"
url = "https://github.com/intel/opencl-clang"
source = f"https://github.com/intel/opencl-clang/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ea179674e52bc8c658e2655f76be467f7052f7d2c37ebcfdb102dce645ad1411"
# Not available
options = ["!check"]


@subpackage("opencl-clang-devel")
def _devel(self):
    return self.default_devel()
