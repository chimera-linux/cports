pkgname = "metee"
pkgver = "4.2.1"
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
sha256 = "bc796f6f07e98106d0303711302633046d6b918f16b3cbce4a49dc406a9a1090"


@subpackage("metee-devel")
def _(self):
    return self.default_devel()
