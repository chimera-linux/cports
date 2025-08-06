pkgname = "libcerf"
pkgver = "3.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "perl", "pkgconf"]
pkgdesc = "Complex error function library"
license = "MIT"
url = "https://jugit.fz-juelich.de/mlz/libcerf"
source = f"{url}/-/archive/v{pkgver}/libcerf-v{pkgver}.tar.gz"
sha256 = "4c07e2a8e2b4d0e4d48db9e0fc9191b43a0e120e577d55d87e26dee8745c6fab"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libcerf-devel")
def _(self):
    return self.default_devel()
