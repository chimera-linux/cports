pkgname = "metee"
pkgver = "4.3.0"
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
sha256 = "6652c3a1a3877a5912096a6e137a9c93230704132e17d31a3a91a730c8fda8fd"


@subpackage("metee-devel")
def _(self):
    return self.default_devel()
