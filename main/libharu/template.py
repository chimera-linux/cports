pkgname = "libharu"
pkgver = "2.4.4"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Zlib"
url = "https://github.com/libharu/libharu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "227ab0ae62979ad65c27a9bc36d85aa77794db3375a0a30af18acdf4d871aee6"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libharu-devel")
def _(self):
    return self.default_devel()
