pkgname = "libass"
pkgver = "0.17.5"
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
sha256 = "caab4b993dd7be6187c55623b789ed75dddefea6e65938af134637c732fe094a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libass-devel")
def _(self):
    return self.default_devel()
