pkgname = "lensfun"
pkgver = "0.3.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DINSTALL_HELPER_SCRIPTS=OFF", "-DBUILD_TESTS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = ["glib-devel", "libomp-devel"]
pkgdesc = "Photographic lens distortion library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-only AND CC-BY-SA-3.0"
url = "https://lensfun.github.io"
source = (
    f"https://github.com/{pkgname}/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "57ba5a0377f24948972339e18be946af12eda22b7c707eb0ddd26586370f6765"

# tests segfault with altivec simd
match self.profile().arch:
    case "x86_64":
        configure_args += ["-DBUILD_FOR_SSE=OFF", "-DBUILD_FOR_SSE2=OFF"]


@subpackage("lensfun-devel")
def _devel(self):
    return self.default_devel()
