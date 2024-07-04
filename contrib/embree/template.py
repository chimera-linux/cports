pkgname = "embree"
pkgver = "4.3.2"
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
sha256 = "dc7bb6bac095b2e7bc64321435acd07c6137d6d60e4b79ec07bb0b215ddf81cb"
# guilty until proven otherwise
hardening = ["!int"]


def post_install(self):
    self.uninstall("usr/embree-vars.*", glob=True)


@subpackage("embree-devel")
def _devel(self):
    return self.default_devel()
