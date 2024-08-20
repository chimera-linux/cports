pkgname = "metee"
pkgver = "4.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["linux-headers"]
pkgdesc = "Intel CSME HECI interface access library"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/intel/metee"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ca4a4b67f8e07ad6bc892f8ce15bd8ecdfb29c04563170f6256e7269e62afce6"


@subpackage("metee-devel")
def _(self):
    return self.default_devel()
