pkgname = "embree"
pkgver = "4.3.3"
pkgrel = 0
# embree really doesn't want to build outside of these without ragepatching
archs = ["aarch64", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DEMBREE_TUTORIALS=OFF",
]
hostmakedepends = ["cmake", "ninja"]
makedepends = ["onetbb-devel"]
pkgdesc = "Ray tracing library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://www.embree.org"
source = f"https://github.com/embree/embree/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8a3bc3c3e21aa209d9861a28f8ba93b2f82ed0dc93341dddac09f1f03c36ef2d"
# guilty until proven otherwise
hardening = ["!int"]


def post_install(self):
    self.uninstall("usr/embree-vars.*", glob=True)


@subpackage("embree-devel")
def _(self):
    return self.default_devel()
