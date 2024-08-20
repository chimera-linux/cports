pkgname = "libass"
pkgver = "0.17.3"
pkgrel = 0
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
source = f"{url}/releases/download/{pkgver}/libass-{pkgver}.tar.gz"
sha256 = "da7c348deb6fa6c24507afab2dee7545ba5dd5bbf90a137bfe9e738f7df68537"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libass-devel")
def _(self):
    return self.default_devel()
