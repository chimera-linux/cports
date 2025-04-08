pkgname = "embree"
pkgver = "4.4.0"
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
license = "Apache-2.0"
url = "https://www.embree.org"
source = f"https://github.com/embree/embree/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "acb517b0ea0f4b442235d5331b69f96192c28da6aca5d5dde0cbe40799638d5c"
# guilty until proven otherwise
hardening = ["!int"]


def post_install(self):
    self.uninstall("usr/embree-vars.*", glob=True)


@subpackage("embree-devel")
def _(self):
    return self.default_devel()
