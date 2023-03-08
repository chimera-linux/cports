pkgname = "vc-intrinsics"
pkgver = "0.12.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DLLVM_DIR=/usr/lib/cmake/llvm/"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "clang-tools-extra", "python"]
makedepends = ["llvm-devel"]
pkgdesc = "Simple package"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://foo.software"
source = f"https://github.com/intel/vc-intrinsics/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "062a31ef35c77aa4ae6d07a73d0c0741ce0703e7c8fa1e59b91ea2addc987e2d"
# needs lit
options = ["!check"]

@subpackage("vc-intrinsics-devel")
def _devel(self):
    return self.default_devel()

