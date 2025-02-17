pkgname = "metee"
pkgver = "4.3.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["linux-headers"]
pkgdesc = "Intel CSME HECI interface access library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/intel/metee"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "21c31c754421b0beb71e8f6a88fa4829c0c6d530f14c39f4a30d37cc216340b7"


@subpackage("metee-devel")
def _(self):
    return self.default_devel()
