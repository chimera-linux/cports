pkgname = "lensfun"
pkgver = "0.3.4"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DINSTALL_HELPER_SCRIPTS=OFF", "-DBUILD_TESTS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python-setuptools"]
makedepends = ["glib-devel", "libomp-devel"]
pkgdesc = "Photographic lens distortion library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-only AND CC-BY-SA-3.0"
url = "https://lensfun.github.io"
source = (
    f"https://github.com/lensfun/lensfun/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "dafb39c08ef24a0e2abd00d05d7341b1bf1f0c38bfcd5a4c69cf5f0ecb6db112"

# tests segfault with altivec simd
match self.profile().arch:
    case "x86_64":
        configure_args += ["-DBUILD_FOR_SSE=OFF", "-DBUILD_FOR_SSE2=OFF"]


@subpackage("lensfun-devel")
def _devel(self):
    return self.default_devel()
