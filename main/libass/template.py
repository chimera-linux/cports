pkgname = "libass"
pkgver = "0.17.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "nasm",
    "pkgconf",
]
makedepends = [
    "fontconfig-devel",
    "fribidi-devel",
    "harfbuzz-devel",
    "libunibreak-devel",
]
pkgdesc = "Portable library for SSA/ASS subtitle rendering"
license = "MIT"
url = "https://github.com/libass/libass"
source = f"{url}/releases/download/{pkgver}/libass-{pkgver}.tar.gz"
sha256 = "a886b3b80867f437bc55cff3280a652bfa0d37b43d2aff39ddf3c4f288b8c5a8"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libass-devel")
def _(self):
    return self.default_devel()
