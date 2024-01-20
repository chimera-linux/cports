pkgname = "libcerf"
pkgver = "2.4"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "perl", "pkgconf"]
pkgdesc = "Complex error function library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://jugit.fz-juelich.de/mlz/libcerf"
source = f"{url}/-/archive/v{pkgver}/libcerf-v{pkgver}.tar.gz"
sha256 = "080b30ae564c3dabe3b89264522adaf5647ec754021572bee54929697b276cdc"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libcerf-devel")
def _devel(self):
    return self.default_devel()
