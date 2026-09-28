pkgname = "libharu"
pkgver = "2.4.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "libpng-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "C library for generating pdfs"
license = "Zlib"
url = "https://github.com/libharu/libharu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0ed3eacf3ceee18e40b6adffbc433f1afbe3c93500291cd95f1477bffe6f24fc"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libharu-devel")
def _(self):
    return self.default_devel()
