pkgname = "libcerf"
pkgver = "3.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "perl", "pkgconf"]
pkgdesc = "Complex error function library"
license = "MIT"
url = "https://jugit.fz-juelich.de/mlz/libcerf"
source = f"{url}/-/archive/v{pkgver}/libcerf-v{pkgver}.tar.gz"
sha256 = "c6108fbda89af37f588119c0c542b6c1e824845a36bea2fa31f7ed2cc1a246db"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libcerf-devel")
def _(self):
    return self.default_devel()
