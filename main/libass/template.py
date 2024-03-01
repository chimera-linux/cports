pkgname = "libass"
pkgver = "0.17.1"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "nasm",
]
makedepends = [
    "fontconfig-devel",
    "fribidi-devel",
    "harfbuzz-devel",
    "libunibreak-devel",
]
pkgdesc = "Portable library for SSA/ASS subtitle rendering"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/libass/libass"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "d653be97198a0543c69111122173c41a99e0b91426f9e17f06a858982c2fb03d"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libass-devel")
def _devel(self):
    return self.default_devel()
